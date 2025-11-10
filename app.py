from http.server import BaseHTTPRequestHandler, HTTPServer
import json
import numpy as np

class handler(BaseHTTPRequestHandler):
    def do_POST(self):
        length = int(self.headers.get("Content-Length", 0))
        body = self.rfile.read(length).decode("utf-8")

        try:
            data = json.loads(body)
            a = float(data.get("a", 0))
            b = float(data.get("b", 0))
        except Exception:
            self.send_error(400, "Invalid input")
            return

        result = np.add(a, b)
        self._send_json({"a": a, "b": b, "sum": result})

    def _send_json(self, data):
        res = json.dumps(data).encode()
        self.send_response(200)
        self.send_header("Content-Type", "application/json")
        self.end_headers()
        self.wfile.write(res)

if __name__ == "__main__":
    port = 10000
    print(f"Server running on port {port}")
    HTTPServer(("", port), handler).serve_forever()
