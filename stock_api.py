import json
from http.server import BaseHTTPRequestHandler, HTTPServer
from pathlib import Path
from urllib.parse import parse_qs, urlsplit


STOCK_FILE = Path(__file__).with_name("stock_replies.json")
STOCK = json.loads(STOCK_FILE.read_text(encoding="utf-8"))


class StockHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        request = urlsplit(self.path)
        if request.path != "/stock":
            self.send_json(404, {"error": "route_not_found"})
            return

        part_code = parse_qs(request.query).get("part", [""])[0]
        record = STOCK.get(part_code)
        if record is None:
            self.send_json(404, {"error": "part_not_found"})
            return

        self.send_json(200, record)

    def send_json(self, status, record):
        body = json.dumps(record).encode("utf-8")
        self.send_response(status)
        self.send_header("Content-Type", "application/json")
        self.send_header("Content-Length", str(len(body)))
        self.end_headers()
        self.wfile.write(body)


if __name__ == "__main__":
    with HTTPServer(("127.0.0.1", 8765), StockHandler) as server:
        print("Stock API: http://127.0.0.1:8765", flush=True)
        try:
            server.serve_forever()
        except KeyboardInterrupt:
            pass
