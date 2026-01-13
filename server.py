import os
import http.server
import socketserver
import random
 
port = random.randint(49152, 65535)

    # Change to the directory containing your HTML file
os.chdir('/workspaces/Calculator/webpage')
Handler = http.server.SimpleHTTPRequestHandler

with socketserver.TCPServer(("", port), Handler) as httpd:
    print(f"Serving at port {port}")
    httpd.serve_forever()
