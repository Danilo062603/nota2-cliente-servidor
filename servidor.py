from http.server import HTTPServer, BaseHTTPRequestHandler
import json
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

mascotas = [
    {"id": 1, "nombre": "Luna", "especie": "Perro", "edad": 3},
    {"id": 2, "nombre": "Milo", "especie": "Gato", "edad": 2},
    {"id": 3, "nombre": "Rocky", "especie": "Perro", "edad": 5}
]

class Servidor(BaseHTTPRequestHandler):

    def do_GET(self):

        if self.path == "/":

            with open(os.path.join(BASE_DIR, "index.html"), "rb") as f:
                contenido = f.read()

            self.send_response(200)
            self.send_header("Content-Type", "text/html")
            self.end_headers()
            self.wfile.write(contenido)

        elif self.path == "/api/mascotas":

            datos = json.dumps(mascotas).encode()

            self.send_response(200)
            self.send_header("Content-Type", "application/json")
            self.end_headers()
            self.wfile.write(datos)

        else:
            self.send_response(404)
            self.end_headers()


servidor = HTTPServer(("localhost", 8000), Servidor)

print("Servidor de Veterinaria corriendo en http://localhost:8000")

servidor.serve_forever()