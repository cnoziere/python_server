import SimpleHTTPServer
import SocketServer

PORT = 8000

Handler = SimpleHTTPServer.SimpleHTTPRequestHandler
http_daemon = SocketServer.TCPServer(("", PORT), Handler)

print "serving at port", PORT
http_daemon.serve_forever()
