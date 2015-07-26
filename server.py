''' This simple server handles client HTTP requests '''

import sys, os
import BaseHTTPServer
import mimetypes

DEFAULT_PORT = 8000
SITE_ROOT = os.getcwd()

class SimpleHTTPHandler(BaseHTTPServer.BaseHTTPRequestHandler):
    ''' implement do_X in order to specify the server's behavior when handling
        an HTTP X request '''

    def do_GET(self):
        f = self.load_file()
        if not f:
            return
        file_type = mimetypes.guess_type(f.name, strict=True)[0]
        if file_type == None:
            file_type = 'text/plain'

        self.send_response(200)
        self.send_header('Content-type', file_type)
        self.end_headers()
        self.wfile.write(f.read())
        f.close()

    def load_file(self):
        ''' Determines which file to send as a response based on the request. '''
        try:
            if len(self.path) > 1 and self.path[0] == '/':
                self.path = self.path[1:]
            file_path = os.path.join(SITE_ROOT, self.path)
            if os.path.isfile(file_path):
                return open(file_path)
            else:
                return open('index.html')
        except IOError:
            self.send_error(404, 'File Not Found')
            return None

def main():
    try:
        try:
            PORT = int(sys.argv[1])
        except:
            PORT = DEFAULT_PORT
        HOST = 'localhost'
        handler = SimpleHTTPHandler
        server = BaseHTTPServer.HTTPServer((HOST, PORT), handler)
        print 'serving at port', PORT
        server.serve_forever()
    except Exception as e:
        print 'server failed to start: %s' % e.value

if __name__ == '__main__':
    main()
