#!/usr/bin/python2.7
from BaseHTTPServer import BaseHTTPRequestHandler, HTTPServer
import picamera
import sys

try:
    port = int(sys.argv[-1])
except:
    port = 10009

class WebCammer(BaseHTTPRequestHandler):
    cfg = dict(
        vflip=1,
        iso=400,
        #framerate=0.25,
        shutter_speed=1000000/5,
    )
    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type', 'image/jpeg')
        self.end_headers()
        
        with picamera.PiCamera(resolution=(2592,1944)) as cam:
            for (k, v) in self.cfg.items():
                setattr(cam, k, v)
            #cam.vflip = 1
            #cam.iso = 100
            print cam.shutter_speed, cam.framerate
            cam.capture(self.wfile, format='jpeg')

def serve_one(camclass, port):
    srv = HTTPServer(('0.0.0.0', port), camclass)
    srv.handle_request()


if __name__ == '__main__':
    server = HTTPServer(('0.0.0.0', port), WebCammer)
    server.serve_forever()

