#!/usr/bin/env python3
"""
Servidor HTTP simples para servir o arquivo HTML de upload
"""

import http.server
import socketserver
import os
import webbrowser
from urllib.parse import urlparse

# Configurações
PORT = 9595
DIRETORIO = os.getcwd()

class MyHTTPRequestHandler(http.server.SimpleHTTPRequestHandler):
    def end_headers(self):
        # Adiciona headers CORS para permitir acesso de outros dispositivos
        self.send_header('Access-Control-Allow-Origin', '*')
        self.send_header('Access-Control-Allow-Methods', 'GET, POST, OPTIONS')
        self.send_header('Access-Control-Allow-Headers', 'Content-Type')
        super().end_headers()

def main():
    # Muda para o diretório atual
    os.chdir(DIRETORIO)
    
    # Cria o servidor
    with socketserver.TCPServer(("", PORT), MyHTTPRequestHandler) as httpd:
        print("=" * 50)
        print("🌐 Servidor HTTP Simples Iniciado!")
        print("=" * 50)
        print(f"📁 Diretório: {DIRETORIO}")
        print(f"🔗 URL Local: http://localhost:{PORT}")
        print(f"🌍 URL Rede: http://10.147.18.132:{PORT}")
        print(f"📄 Arquivo: http://10.147.18.132:{PORT}/upload_arquivos.html")
        print("=" * 50)
        print("🛑 Para parar: Ctrl+C")
        print("=" * 50)
        
        try:
            # Abre o navegador automaticamente
            webbrowser.open(f"http://localhost:{PORT}/upload_arquivos.html")
            
            # Inicia o servidor
            httpd.serve_forever()
        except KeyboardInterrupt:
            print("\n🛑 Servidor parado pelo usuário")
        except Exception as e:
            print(f"❌ Erro: {e}")

if __name__ == "__main__":
    main() 