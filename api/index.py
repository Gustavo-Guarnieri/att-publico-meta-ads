from http.server import BaseHTTPRequestHandler
import json
import os

from pipeline import executaPipeline

class handler(BaseHTTPRequestHandler):

    def do_POST(self):
        
        print("HEADERS RECEBIDOS:")
        for k, v in self.headers.items():
            print(k, v)

        # 1. Validação do header x-api-key
        api_key_request = self.headers.get("x-api-key")
        api_key_env = os.getenv("API_KEY")

        '''if not api_key_request or api_key_request != api_key_env:
            self.send_response(401)
            self.send_header("Content-Type", "application/json")
            self.end_headers()

            response = {
                "status": "error",
                "message": "Unauthorized"
            }

            self.wfile.write(json.dumps(response).encode())
            return'''

        try:
            # 2. Executa pipeline
            resultado = executaPipeline()

            self.send_response(200)
            self.send_header("Content-Type", "application/json")
            self.end_headers()
            self.wfile.write(json.dumps({
                "status": "success",
                "data": resultado
            }).encode())

        except Exception as e:
            # 3. Tratamento de erro
            self.send_response(500)
            self.send_header("Content-Type", "application/json")
            self.end_headers()

            response = {
                "status": "error",
                "message": str(e)
            }

            self.wfile.write(json.dumps(response).encode())
