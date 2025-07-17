import ssl
from flask import Flask
import os
from app import create_app

app = create_app()

@app.route('/')
def index():
        return "Bem vindo a API de NOTAS com FLASK!"

if __name__ == '__main__':
        app.run(host='0.0.0.0', port=5000, debug=True, ssl_context=('cert.pem', 'key.pem'))