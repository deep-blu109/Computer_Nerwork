from http.server import HTTPServer, BaseHTTPRequestHandler
from socketserver import ThreadingMixIn
import threading

class MyHandler(BaseHTTPRequestHandler):

    def do_GET(self):
        if self.path == '/index.html':
            if self.request_version == 'HTTP/1.0':
                self.send_response(400)
            else:
                self.send_response(200)                
                self.send_header('Content-length', 37)
                self.send_header('Content-type', 'text/html')
                self.end_headers()
                self.wfile.write(b'<html><body>hello world</body></html>')

        elif self.path == '/image.jpg':
            if self.request_version == 'HTTP/1.0':
                self.send_response(400)
            else:
                self.send_response(200)
                self.send_header('Content-length', 37)
                self.send_header('Content-type', 'image/jpg')
                self.end_headers()
                self.wfile.write(b'<html><body>hello world</body></html>')
        
        else:
            self.send_response(404)

    def do_POST(self):
        if self.request_version == 'HTTP/1.0':
            self.send_response(400)
        else:
            self.send_response(200)
            self.send_header('Content-Type', 'text/html')
            self.end_headers()

            dataLength = int(self.headers.get("Content-Length"))
            data = self.rfile.read(dataLength)

            print(data)

            self.wfile.write(b'hello client!')            
        
class ThreadingServer(ThreadingMixIn, HTTPServer):
    pass

if __name__ == '__main__':
    HOST, PORT = '192.168.0.19', 8000
    server = ThreadingServer((HOST, PORT), MyHandler)
    print('Started WebServer on port 8000')
    print('Press Crtl + c to quit webserver')
    server.serve_forever()
