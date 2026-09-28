import http.server
import socketserver

PORT = 5500

class Handler(http.server.SimpleHTTPRequestHandler):
    extensions_map = {
        **http.server.SimpleHTTPRequestHandler.extensions_map,
        '.css': 'text/css',
        '.js': 'application/javascript',
        '.mjs': 'application/javascript',
        '.json': 'application/json',
        '.svg': 'image/svg+xml',
    }

    def guess_type(self, path):
        if path.endswith('.css'):
            return 'text/css'
        if path.endswith('.js'):
            return 'application/javascript'
        return super().guess_type(path)

    def end_headers(self):
        self.send_header('Cache-Control', 'no-store, no-cache, must-revalidate')
        super().end_headers()

with socketserver.TCPServer(("", PORT), Handler) as httpd:
    print(f"Serving at http://localhost:{PORT}")
    httpd.serve_forever()
