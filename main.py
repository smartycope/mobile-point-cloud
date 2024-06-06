#!/usr/bin/env python


import http.server
import socketserver
import ssl
import json
import base64
from io import BytesIO
from PIL import Image
import numpy as np
from flask import Flask, request, jsonify
from flask_cors import CORS
import base64
from io import BytesIO
from PIL import Image
import numpy as np
from http.server import HTTPServer, BaseHTTPRequestHandler
import logging, ngrok
import http.server
import socketserver
import json
import base64
from io import BytesIO
from PIL import Image
import numpy as np


IP = '10.40.132.201'
PORT = 3456
CERT_FILE = '/home/anastasia/cert.pem'
KEY_FILE = '/home/anastasia/key.pem'


# class RequestHandler(http.server.SimpleHTTPRequestHandler):
# class RequestHandler(BaseHTTPRequestHandler):
#     def do_POST(self):
#         if self.path == '/upload':
#             print('recieved image!')
#             content_length = int(self.headers['Content-Length'])
#             post_data = self.rfile.read(content_length)
#             data = json.loads(post_data)
#             image_data = data['image']
#             image_data = image_data.split(",")[1]  # Remove the header of the base64 string
#             image = Image.open(BytesIO(base64.b64decode(image_data)))

#             # Process the image (convert to numpy array, etc.)
#             image_np = np.array(image)

#             # Here you can add your distance calculation logic

#             response = {
#                 "status": "success",
#                 "message": "Image received and processed"
#             }
#             self.send_response(200)
#             self.send_header('Content-Type', 'application/json')
#             self.end_headers()
#             self.wfile.write(json.dumps(response).encode('utf-8'))
#         else:
#             self.send_response(404)
#             self.end_headers()

# # Handler = RequestHandler

# # with socketserver.TCPServer(("", PORT), Handler) as httpd:
# #     print("Serving at port", PORT)
# #     httpd.serve_forever()

# logging.basicConfig(level=logging.INFO)
# server = HTTPServer(("localhost", 0), RequestHandler)
# ngrok.listen(server)
# server.serve_forever()


# PORT = 8000

# class RequestHandler(http.server.SimpleHTTPRequestHandler):
#     def do_POST(self):
#         if self.path == '/upload':
#             # Add CORS headers
#             self.send_header('Access-Control-Allow-Origin', '*')
#             self.send_header('Access-Control-Allow-Methods', 'POST')
#             self.send_header('Access-Control-Allow-Headers', 'Content-Type')

#             content_length = int(self.headers['Content-Length'])
#             post_data = self.rfile.read(content_length)
#             data = json.loads(post_data)
#             image_data = data['image']
#             image_data = image_data.split(",")[1]  # Remove the header of the base64 string
#             image = Image.open(BytesIO(base64.b64decode(image_data)))

#             # Process the image (convert to numpy array, etc.)
#             image_np = np.array(image)

#             # Here you can add your distance calculation logic

#             response = {
#                 "status": "success",
#                 "message": "Image received and processed"
#             }
#             self.send_response(200)
#             self.send_header('Content-Type', 'application/json')
#             self.end_headers()
#             self.wfile.write(json.dumps(response).encode('utf-8'))
#         else:
#             self.send_response(404)
#             self.end_headers()

# Handler = RequestHandler

# # Create an SSL context
# context = ssl.SSLContext(ssl.PROTOCOL_TLS_SERVER)
# context.load_cert_chain(certfile=CERT_FILE, keyfile=KEY_FILE)

# with socketserver.TCPServer(("", PORT), Handler) as httpd:
#     httpd.socket = context.wrap_socket(httpd.socket, server_side=True)
#     print("Serving on https://localhost:", PORT, sep='')
#     try:
#         httpd.serve_forever()
#     except KeyboardInterrupt:
#         exit(0)
#     finally:
#         httpd.server_close()


# class RequestHandler(http.server.SimpleHTTPRequestHandler):
#     def do_POST(self):
#         if self.path == '/upload':
#             content_length = int(self.headers['Content-Length'])
#             post_data = self.rfile.read(content_length)
#             data = json.loads(post_data)
#             image_data = data['image']
#             image_data = image_data.split(",")[1]  # Remove the header of the base64 string
#             image = Image.open(BytesIO(base64.b64decode(image_data)))

#             # Process the image (convert to numpy array, etc.)
#             image_np = np.array(image)

#             # Here you can add your distance calculation logic

#             response = {
#                 "status": "success",
#                 "message": "Image received and processed"
#             }
#             self.send_response(200)
#             self.send_header('Content-Type', 'application/json')
#             self.end_headers()
#             self.wfile.write(json.dumps(response).encode('utf-8'))
#         else:
#             self.send_response(404)
#             self.end_headers()

# Handler = RequestHandler

# with socketserver.TCPServer(("", PORT), Handler) as httpd:
#     httpd.socket = ssl.wrap_socket(httpd.socket,
#                                    keyfile=KEY_FILE,
#                                    certfile=CERT_FILE,
#                                    server_side=True)
#     print("Serving on https://localhost:", PORT)
#     httpd.serve_forever()



app = Flask(__name__)
CORS(app)  # This will enable CORS for all routes

@app.route('/upload', methods=['POST'])
def upload():
    print('Recieved image!')
    data = request.json
    image_data = data['image']
    image_data = image_data.split(",")[1]  # Remove the header of the base64 string
    image = Image.open(BytesIO(base64.b64decode(image_data)))

    # Process the image (convert to numpy array, etc.)
    image_np = np.array(image)
    image.save('photo.png')

    # Here you can add your distance calculation logic

    return jsonify({"status": "success", "message": "Image received and processed"})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=PORT)



# class App(BaseHTTPRequestHandler):
#     def do_POST(self):
#         print('Recieved image!')
#         data = request.json
#         image_data = data['image']
#         image_data = image_data.split(",")[1]  # Remove the header of the base64 string
#         image = Image.open(BytesIO(base64.b64decode(image_data)))

#         # Process the image (convert to numpy array, etc.)
#         image_np = np.array(image)
#         image.save('photo.png')

#         # Here you can add your distance calculation logic

#         # body = bytes("Hello", "utf-8")
#         self.protocol_version = "HTTP/1.1"
#         self.send_response(201)
#         # self.send_header("Content-Length", len(body))
#         # self.end_headers()
#         # self.wfile.write(body)
