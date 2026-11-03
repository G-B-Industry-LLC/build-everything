from __future__ import annotations

import importlib.util
import socket
import sys
import threading
import unittest
from pathlib import Path

MODULE_PATH = Path(__file__).resolve().parents[1] / "server.py"
SPEC = importlib.util.spec_from_file_location("build_everything_http_server", MODULE_PATH)
assert SPEC and SPEC.loader
SERVER = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = SERVER
SPEC.loader.exec_module(SERVER)


class HandlerTests(unittest.TestCase):
    def test_health_route(self) -> None:
        result = SERVER.handle(b"GET /health HTTP/1.1\r\nHost: localhost\r\n\r\n")
        self.assertIn(b"HTTP/1.1 200 OK", result)
        self.assertTrue(result.endswith(b'{"status":"ok"}'))
        self.assertIn(b"Content-Length: 15", result)

    def test_unknown_route(self) -> None:
        result = SERVER.handle(b"GET /missing HTTP/1.1\r\nHost: localhost\r\n\r\n")
        self.assertIn(b"404 Not Found", result)

    def test_unsupported_method(self) -> None:
        result = SERVER.handle(b"POST / HTTP/1.1\r\nHost: localhost\r\n\r\n")
        self.assertIn(b"405 Method Not Allowed", result)

    def test_malformed_request(self) -> None:
        result = SERVER.handle(b"not http")
        self.assertIn(b"400 Bad Request", result)

    def test_real_tcp_round_trip(self) -> None:
        with socket.create_server(("127.0.0.1", 0)) as listener:
            port = listener.getsockname()[1]

            def once() -> None:
                connection, _address = listener.accept()
                with connection:
                    connection.sendall(SERVER.handle(connection.recv(SERVER.MAX_REQUEST)))

            worker = threading.Thread(target=once, daemon=True)
            worker.start()
            with socket.create_connection(("127.0.0.1", port), timeout=2) as client:
                client.sendall(b"GET /health HTTP/1.1\r\nHost: localhost\r\n\r\n")
                payload = client.recv(4096)
            worker.join(timeout=2)

        self.assertIn(b"200 OK", payload)
        self.assertTrue(payload.endswith(b'{"status":"ok"}'))


if __name__ == "__main__":
    unittest.main()

