from app import app

if __name__ == '__main__':
    print("🚀 Iniciando servidor de upload de arquivos...")
    print("📱 Acesse: http://10.147.18.132:5678")
    print("🛑 Para parar o servidor, pressione Ctrl+C")
    print("-" * 50)
    
    # Inicia o servidor na porta 5678, acessível por qualquer IP
    app.run(host='0.0.0.0', port=5678, debug=False) 