# Build a tiny website server

**Level:** Beginner  
**Time:** About 45 minutes  
**Learner:** Ages 12+ with a mentor; teens who can run a terminal command
**You need:** Python 3.11 or newer. Nothing else is downloaded.

## The big idea

When you open a website, your browser asks another computer for a page. The program that listens for that question and sends an answer is called a **server**.

Think of it like a restaurant:

- your browser is the customer;
- the request is the order;
- the server reads the order;
- the response is what comes back to the table.

In this project, both “computers” can be the same computer. Your browser asks, and your Python program answers.

## Where this is used

The same request-and-response idea powers:

- websites sending pages;
- mobile apps loading account information;
- games loading player scores;
- services checking whether another service is awake.

Real servers have many more protections and features. This small version lets you see the important exchange without a framework hiding it.

## What you will make

You will run a local server with three possible answers:

| You ask for | The server answers |
| --- | --- |
| `/` | A tiny HTML home page |
| `/health` | `{"status":"ok"}` |
| anything else | `404 Not Found` |

It also explains bad requests with standard number codes instead of silently failing.

## Before you start

You should know how to open a terminal and run a command. You do not need to know networking yet.

Check Python:

```bash
python --version
```

If that command does not show Python 3.11 or newer, ask a parent, teacher, mentor, or system administrator to help install it.

## Build it

### 1. Meet the program

Open [`server.py`](server.py). Find these three jobs:

- `parse_request` reads the first line of the browser's question;
- `handle` chooses the answer;
- `serve` listens on your computer and sends the answer.

You do not need to memorize the code. First, connect each function name to its job.

### 2. Start the server

From the root of this repository, run:

```bash
python labs/http-server-python/server.py
```

You should see:

```text
Listening on http://127.0.0.1:8080
```

`127.0.0.1` means **this computer**. The number `8080` is the particular door the program listens at.

### 3. Ask for an answer

Open `http://127.0.0.1:8080/health` in a browser. You should see:

```json
{"status":"ok"}
```

Now try `http://127.0.0.1:8080/missing`. The server should answer `not found` because you did not build that path.

Stop the server with `Ctrl+C` when you are done.

## Prove it works

Run:

```bash
python -m unittest discover -s labs/http-server-python/tests -v
```

Five checks should say `ok`. They test the health answer, missing pages, unsupported actions, broken questions, and one real connection through your computer's network system.

If a check fails, read the name of the failed check first. It tells you which behavior changed.

## Try one safe change

In `server.py`, change the words inside the home-page response:

```python
b"<h1>Build Everything</h1>\n"
```

Restart the server and refresh the home page. The words should change while the proof checks still pass.

## Explain it back

You understand the idea when you can answer these in your own words:

1. What does the browser send?
2. What does the server send back?
3. Why does `/missing` return `404`?
4. Why is this project limited to `127.0.0.1`?

## Glossary

- **Browser:** the app that displays a website and sends requests.
- **Server:** a program that listens for a request and sends a response.
- **HTTP:** the shared format browsers and web servers use to describe requests and responses.
- **Route:** a path such as `/health` that selects an answer.
- **Status code:** a number describing the result. `200` means success, `404` means the route was not found, and `400` means the request was malformed.
- **TCP:** the connection that reliably carries the request and response bytes.
- **Localhost / 127.0.0.1:** a private address that points back to your own computer.

## Safety and limits

This is a learning server, not a production server. It has no encryption, request timeouts, traffic limits, simultaneous-user handling, hardened parser, or protection from hostile input.

Keep it on `127.0.0.1`. Do not expose it to the public internet. Younger learners should have adult help with software installation and terminal use.
