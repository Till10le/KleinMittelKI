"""Nachgebaute Ghost Admin API für Tests. Prüft JWT-Signatur, speichert Beiträge im Speicher, protokolliert Anfragen."""
import base64, hashlib, hmac, json, re, sys, threading, time, uuid as _uuid
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from urllib.parse import urlparse, parse_qs

KID, SECRET = "6512abcdef0123456789abcd", "a1" * 32
POSTS = {}
LOG = []


def check_jwt(h):
    assert h.startswith("Ghost "), "kein Ghost-Header"
    tok = h[6:]
    head, payload, sig = tok.split(".")
    pad = lambda s: s + "=" * (-len(s) % 4)
    exp = base64.urlsafe_b64encode(hmac.new(bytes.fromhex(SECRET), f"{head}.{payload}".encode(), hashlib.sha256).digest()).rstrip(b"=").decode()
    assert sig == exp, "Signatur falsch"
    hd = json.loads(base64.urlsafe_b64decode(pad(head)))
    pl = json.loads(base64.urlsafe_b64decode(pad(payload)))
    assert hd["kid"] == KID and pl["aud"] == "/admin/" and pl["exp"] > time.time()


def now():
    time.sleep(0.01)
    return time.strftime("%Y-%m-%dT%H:%M:%S", time.gmtime()) + f".{int(time.time()*1000)%1000:03d}Z"


class H(BaseHTTPRequestHandler):
    def log_message(self, *a):
        pass

    def send(self, code, obj):
        b = json.dumps(obj).encode()
        self.send_response(code); self.send_header("Content-Type", "application/json")
        self.send_header("Content-Length", str(len(b))); self.end_headers(); self.wfile.write(b)

    def handle_any(self, method):
        u = urlparse(self.path); q = parse_qs(u.query)
        try:
            check_jwt(self.headers.get("Authorization", ""))
        except Exception as e:
            return self.send(401, {"errors": [{"message": str(e)}]})
        n = int(self.headers.get("Content-Length") or 0)
        raw = self.rfile.read(n) if n else b""
        LOG.append({"method": method, "path": u.path, "query": q})
        p = u.path.replace("/ghost/api/admin", "")
        if p == "/site/":
            return self.send(200, {"site": {"title": "KLEIN. MITTEL. KI.", "url": "https://www.kleinmittelki.de/"}})
        if p == "/newsletters/" and method == "GET":
            return self.send(200, {"newsletters": [{"slug": "default-newsletter", "status": "active"}]})
        if p == "/images/upload/" and method == "POST":
            assert b'name="file"' in raw
            return self.send(201, {"images": [{"url": f"https://storage.example/{_uuid.uuid4().hex}.png"}]})
        if p == "/posts/" and method == "GET":
            posts = list(POSTS.values())
            return self.send(200, {"posts": posts, "meta": {"pagination": {"total": len(posts)}}})
        if p == "/posts/" and method == "POST":
            d = json.loads(raw)["posts"][0]
            pid = _uuid.uuid4().hex[:24]
            d.update({"id": pid, "uuid": str(_uuid.uuid4()), "updated_at": now(), "status": d.get("status", "draft"),
                      "tags": d.get("tags", []), "url": f"https://www.kleinmittelki.de/{d['slug']}/", "html": "<h2>Was ist passiert?</h2><p>57 Prozent der Unternehmen nutzen KI.</p>"})
            POSTS[pid] = d
            return self.send(201, {"posts": [d]})
        m = re.match(r"^/posts/slug/([^/]+)/$", p)
        if m and method == "GET":
            hit = [x for x in POSTS.values() if x["slug"] == m.group(1)]
            return self.send(200, {"posts": hit}) if hit else self.send(404, {"errors": [{"message": "Post not found."}]})
        m = re.match(r"^/posts/([0-9a-f]{24})/$", p)
        if m:
            pid = m.group(1)
            if pid not in POSTS:
                return self.send(404, {"errors": [{"message": "Post not found."}]})
            if method == "GET":
                return self.send(200, {"posts": [POSTS[pid]]})
            if method == "PUT":
                d = json.loads(raw)["posts"][0]
                if d.get("updated_at") != POSTS[pid]["updated_at"]:
                    return self.send(409, {"errors": [{"message": "Saving failed! Someone else is editing this post."}]})
                POSTS[pid].update(d); POSTS[pid]["updated_at"] = now()
                return self.send(200, {"posts": [POSTS[pid]]})
        return self.send(404, {"errors": [{"message": f"unbekannt {method} {p}"}]})

    def do_GET(self): self.handle_any("GET")
    def do_POST(self): self.handle_any("POST")
    def do_PUT(self): self.handle_any("PUT")
    def do_DELETE(self): self.handle_any("DELETE")


if __name__ == "__main__":
    srv = ThreadingHTTPServer(("127.0.0.1", int(sys.argv[1])), H)
    srv.serve_forever()
