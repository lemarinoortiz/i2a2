from flask import Flask, request, jsonify, render_template, send_from_directory
import os
import pandas as pd
from datetime import datetime
from principais_funcoes import TratarArquivos

app = Flask(__name__)
UPLOAD_FOLDER = 'uploads'
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

# Página HTML principal - serve o arquivo upload_arquivos.html
@app.route('/')
def index():
    return send_from_directory('.', 'upload_arquivos.html')

# Rota de upload
@app.route('/webhook-test/enviar-csv', methods=['POST'])
def upload_files():
    tratar_arquivos = TratarArquivos()

    try:
        if 'file1' not in request.files or 'file2' not in request.files:
            return jsonify({"erro": "Ambos os arquivos são obrigatórios (file1 e file2)"}), 400

        file1 = request.files['file1']
        file2 = request.files['file2']

        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        filename1 = f"nf_itens_{timestamp}.csv"
        filename2 = f"nf_cabecalho_{timestamp}.csv"
        path1 = os.path.join(UPLOAD_FOLDER, filename1)
        path2 = os.path.join(UPLOAD_FOLDER, filename2)

        file1.save(path1)
        file2.save(path2)

        tratar_arquivos.tratar_arquivo(path1, 'nf_itens')
        tratar_arquivos.tratar_arquivo(path2, 'nf_cabecalho')
        
        # Leitura com pandas
        try:
            df1 = pd.read_csv(path1)
            df2 = pd.read_csv(path2)
            print(df1.head())
            print(df2.head())
        except Exception as e:
            return jsonify({"erro": f"Erro ao processar os arquivos: {str(e)}"}), 500

        # Inserir LOG de sucesso
        tratar_arquivos.inserir_log('SUCESSO', 'upload_arquivos', 'Arquivos processados com sucesso')
        return jsonify({"mensagem": "Arquivos salvos e lidos com sucesso!"}), 200
    except Exception as e:
        # Inserir LOG de erro
        tratar_arquivos.inserir_log('ERRO', 'upload_arquivos', 'Erro ao processar os arquivos')
        return jsonify({"erro": f"Erro ao processar os arquivos: {str(e)}"}), 500

# Roda o servidor
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5679, debug=True)
