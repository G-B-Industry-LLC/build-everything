# Build an HTTP server from sockets

**Level:** Beginner  
**Time:** About 45 minutes  
**Dependencies:** Python 3.11+ and the standard library

## What you are rebuilding

An HTTP server accepts a TCP connection, reads a request, applies HTTP semantics, and returns a correctly framed response. Frameworks normally hide all four steps.

This lab implements three routes:

- `GET /` returns a small HTML page;
- `GET /health` returns JSON;
- any other path returns `404 Not Found`.

Unsupported methods return `405 Method Not Allowed`. Malformed requests return `400 Bad Request`.

## Run it

```bash
python labs/http-server-python/server.py
```

In another terminal:

```bash
curl -i http://127.0.0.1:8080/health
```

## Prove it

```bash
python -m unittest discover -s labs/http-server-python/tests -v
```

The tests exercise response framing, routes, unsupported methods, malformed requests, and a real TCP round trip.

## What this lab intentionally omits

This is not a production server. It has no TLS, request-body streaming, chunked transfer encoding, keep-alive pooling, timeouts, concurrency limits, proxy trust model, or hardened parser. Bind it only to localhost and never expose it to untrusted traffic.

