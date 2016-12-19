from BaseHTTPServer import HTTPServer

from os import curdir, sep
from BaseHTTPServer import BaseHTTPRequestHandler

PORT_NUMBER = 8080


class RequestHandler(BaseHTTPRequestHandler):
    mime_type = ""
    html_version = True
    send_image = False
    send_reply = False

    def __init__(self, request, client_address, serv):
        BaseHTTPRequestHandler.__init__(self, request, client_address, serv)
        self.path = '/'

    def _check_accept_header(self, accept_dict):
        if accept_dict[0]['accept'] == 'text/plain':
            self.html_version = False

    def _map_response(self, end, mime_type, img_flag):
        if self.path.endswith(end):
            self.mime_type = mime_type
            self.send_image = img_flag

    def _send_reply_or_image(self, img_flag):
        f = open(curdir + sep + self.path, "rb") if img_flag else open(curdir + sep + self.path)
        data = f.read()
        self.send_response(200)
        self.send_header('Content-length', len(data))
        self.send_header('Content-type', self.mime_type)
        self.end_headers()
        self.wfile.write(data)
        f.close()

    def _process_path_request(self):
        if self.path == '/' or self.path == '/index.html' or not self.path.__contains__('.'):
            self.path = 'index.html'

    def do_GET(self):

        try:
            self._process_path_request()
            self._map_response(".txt", "text/plain", False)
            self._map_response(".html", "text/html", False)
            self._map_response(".js", "application/javascript", False)
            self._map_response(".css", "text/css", False)
            self._map_response(".jpg", "image/jpg", True)
            self._map_response(".png", "image/png", True)
            self._map_response(".gif", "image/gif", True)
            self._map_response(".svg", "image/svg+xml", True)
            self._map_response(".ico", "image/x-icon", True)
            self._send_reply_or_image(self.send_image)
            return

        except IOError:
            self.send_error(404, 'File Not Found: %s' % self.path)


server = HTTPServer(('', PORT_NUMBER), RequestHandler)

try:
    print 'Webserver running on port ', PORT_NUMBER
    server.serve_forever()

except KeyboardInterrupt:
    print '^C received, shutting down the web server'
    server.socket.close()
