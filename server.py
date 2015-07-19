import sys
import BaseHTTPServer

PORT = 8000

class SimpleHTTPHandler(BaseHTTPServer.BaseHTTPRequestHandler):
    def do_GET(self):
        print self.command
        print self.headers
        message = 'Hello {}.'.format(self.address_string())
        self.send_response(200, message)
        self.send_header("Content-type", "text/plain")
        self.end_headers()
        return message

if __name__ == "__main__":
    if len(sys.argv) > 1:
        try:
            PORT = int(sys.argv[1])
        except:
            PORT = 8000
    HOST = '10.211.200.242'
    handler = SimpleHTTPHandler
    http_daemon = BaseHTTPServer.HTTPServer((HOST, PORT), handler)

    print "serving at port", PORT
    http_daemon.serve_forever()
