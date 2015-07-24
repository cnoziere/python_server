import sys
import BaseHTTPServer

PORT = 8000

class SimpleHTTPHandler(BaseHTTPServer.BaseHTTPRequestHandler):
    def do_GET(self):
        print self.path
        try:
            f = self.load_file()
        except IOError:
            self.send_error(404, 'File Not Found')
            return
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()
        self.wfile.write(f.read())
        f.close()

    def load_file(self):
        ''' Determines which file to send as a response based on the request. '''
        if self.path == "/style.css" :
            return open("style.css")
        elif self.path == "/favicon.ico" :
            return open("favicon.ico")
        else:
            return open("chat.html")

def main():
    try:
        if len(sys.argv) > 1:
            try:
                PORT = int(sys.argv[1])
            except:
                PORT = 8000
        else:
            PORT = 8000
        HOST = 'localhost'
        handler = SimpleHTTPHandler
        server = BaseHTTPServer.HTTPServer((HOST, PORT), handler)
        print "serving at port", PORT
        server.serve_forever()
    except:
        pass

if __name__ == "__main__":
    main()
