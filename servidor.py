from http.server import BaseHTTPRequestHandler, HTTPServer
import json
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

class MiServidor(BaseHTTPRequestHandler):

    def do_GET(self):

        if self.path == "/":
            ruta = os.path.join(BASE_DIR, "index.html")

            with open(ruta, "rb") as f:
                contenido = f.read()

            self.send_response(200)
            self.send_header("Content-type", "text/html")
            self.end_headers()
            self.wfile.write(contenido)

        elif self.path == "/api/mascotas":

            mascotas = [
                {"nombre": "Luna", "tipo": "Perro", "edad": 3},
                {"nombre": "Milo", "tipo": "Gato", "edad": 2},
                {"nombre": "Rocky", "tipo": "Perro", "edad": 5}
            ]

            datos = json.dumps(mascotas).encode()

            self.send_response(200)
            self.send_header("Content-type", "application/json")
            self.end_headers()
            self.wfile.write(datos)

servidor = HTTPServer(("localhost", 8000), MiServidor)

print("Servidor corriendo en http://localhost:8000")

servidor.serve_forever()