import sys
import BaseHTTPServer
import SocketServer

PORT = 8000

class SimpleHTTPHandler(BaseHTTPServer.BaseHTTPRequestHandler):
    def do_GET(self):
        print self.command, self.headers
        message = 'Hello {}.'.format(self.address_string())
        self.send_response(1, message)


HOST, PORT = '10.211.200.242', 8000
handler = SimpleHTTPHandler
http_daemon = SocketServer.TCPServer((HOST, PORT), handler)

print "serving at port", PORT

if __name__ == "__main__":
    http_daemon.serve_forever()
