from __future__ import annotations

import json
import socket
from dataclasses import dataclass

HOST = "127.0.0.1"
PORT = 8080
MAX_REQUEST = 16 * 1024


@dataclass(frozen=True)
class Request:
    method: str
    target: str
    version: str


def parse_request(data: bytes) -> Request:
    try:
        first_line = data.decode("ascii").split("\r\n", 1)[0]
        method, target, version = first_line.split(" ")
    except (UnicodeDecodeError, ValueError) as exc:
        raise ValueError("malformed request line") from exc
    if version != "HTTP/1.1" or not target.startswith("/"):
        raise ValueError("unsupported request target or version")
    return Request(method=method, target=target, version=version)


def response(status: str, body: bytes, content_type: str) -> bytes:
    headers = [
        f"HTTP/1.1 {status}",
        f"Content-Length: {len(body)}",
        f"Content-Type: {content_type}",
        "Connection: close",
        "X-Content-Type-Options: nosniff",
        "",
        "",
    ]
    return "\r\n".join(headers).encode("ascii") + body


def handle(data: bytes) -> bytes:
    try:
        request = parse_request(data)
    except ValueError:
        return response("400 Bad Request", b"bad request\n", "text/plain; charset=utf-8")

    if request.method != "GET":
        return response("405 Method Not Allowed", b"method not allowed\n", "text/plain; charset=utf-8")
    if request.target == "/health":
        body = json.dumps({"status": "ok"}, separators=(",", ":")).encode("utf-8")
        return response("200 OK", body, "application/json")
    if request.target == "/":
        return response("200 OK", b"<h1>Build Everything</h1>\n", "text/html; charset=utf-8")
    return response("404 Not Found", b"not found\n", "text/plain; charset=utf-8")


def serve(host: str = HOST, port: int = PORT) -> None:
    with socket.create_server((host, port)) as listener:
        print(f"Listening on http://{host}:{port}")
        while True:
            connection, _address = listener.accept()
            with connection:
                data = connection.recv(MAX_REQUEST)
                connection.sendall(handle(data))


if __name__ == "__main__":
    serve()

