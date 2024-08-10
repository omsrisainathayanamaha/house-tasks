
from http.server import BaseHTTPRequestHandler, HTTPServer
import json
import os

hostName = "MY IP HERE"  # replace with the IP of the runner
serverPort = 8080
#myGame = Game(Player("default"), Player("default2"))
class MyServer(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()
        print("Starting to write")
        self.wfile.write(bytes(self.html_content(), "utf-8"))
        print("written")
    def do_POST(self):
        if self.path == "/submit":
            content_length = int(self.headers['Content-Length'])
            post_data = self.rfile.read(content_length)
            data = json.loads(post_data)
            print("Received data:", data)
            # accessing the "x" element is data["x"]
            self.send_response(200)
            self.send_header("Content-type", "text/html")
            self.end_headers()
            self.wfile.write(bytes("WHAT YOU WANT TO WRITE HERE", "utf-8"))
    def html_content(self):
        file_path = os.path.join(os.path.dirname(__file__), 'index.html')
        try:
            with open(file_path, "r") as file:
                content = file.read()
            return content
        except FileNotFoundError:
            return "File not found."
        except Exception as e:
            return f"An error occurred: {e}"

if __name__ == "__main__":
    webServer = HTTPServer((hostName, serverPort), MyServer)
    print("Server started http://%s:%s" % (hostName, serverPort))

    try:
        webServer.serve_forever()
    except KeyboardInterrupt:
        pass

    webServer.server_close()
    print("Server stopped.")