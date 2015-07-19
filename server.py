import sys
import BaseHTTPServer
import SocketServer

PORT = 8000

class SimpleHTTPHandler(BaseHTTPServer.BaseHTTPRequestHandler):
    def do_GET(self):
        try:
            f = open("chat.html")
            self.send_response(200)
            self.send_header('Content-type', 'text/html')
            self.end_headers()
            #self.wfile.write(f.read())
            f.close()
            return
        except IOError:
            self.send_error(404, 'File Not Found')

def main():
    try:
        HOST, PORT = 'localhost', 8000
        handler = SimpleHTTPHandler
        server = BaseHTTPServer.HTTPServer((HOST, PORT), handler)
        print "serving at port", PORT
        server.serve_forever()
    except:
        pass

if __name__ == "__main__":
    main()
