import http.server, os
class H(http.server.SimpleHTTPRequestHandler):
    def guess_type(self, path):
        ctype = super().guess_type(path)
        if ctype == "text/html":
            return "text/html; charset=utf-8"
        return ctype
import socketserver
with socketserver.TCPServer(("0.0.0.0", 3000), H) as httpd:
    httpd.serve_forever()
