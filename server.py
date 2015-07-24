import sys
import BaseHTTPServer

PORT = 8000

class SimpleHTTPHandler(BaseHTTPServer.BaseHTTPRequestHandler):
    def do_GET(self):
        print self.path
        f = self.load_file()
        if not f:
            return
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()
        self.wfile.write(f.read())
        f.close()

    def load_file(self):
        ''' Determines which file to send as a response based on the request. '''
        try:
            if self.path == '/':
                return open('chat.html')
            else :
                return open(self.path[1:])

        except IOError:
            self.send_error(404, 'File Not Found')
            return None

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
