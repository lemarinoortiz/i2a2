# 📁 Servidor de Upload de Arquivos CSV

Este projeto permite acessar o formulário de upload de arquivos CSV via rede local.

## 🚀 Como usar

### Opção 1: Servidor Flask (Recomendado)
O servidor Flask já está configurado para processar os uploads.

```bash
# Instalar dependências
pip install -r requirements.txt

# Iniciar servidor
python iniciar_servidor.py
```

**Ou no Windows:**
```cmd
iniciar_servidor.bat
```

**Acesse:** `http://10.147.18.132:5678`

### Opção 2: Servidor HTTP Simples
Para apenas visualizar o HTML sem processamento:

```bash
python servidor_simples.py
```

**Acesse:** `http://10.147.18.132:8080/upload_arquivos.html`

## 📱 URLs de Acesso

- **Local:** `http://localhost:5678` (Flask) ou `http://localhost:8080` (HTTP simples)
- **Rede:** `http://10.147.18.132:5678` (Flask) ou `http://10.147.18.132:8080` (HTTP simples)

## 🔧 Configuração de Rede

Para que outros dispositivos na rede possam acessar:

1. **Verifique o firewall do Windows:**
   - Abra "Firewall do Windows Defender"
   - Permita o Python através do firewall

2. **Verifique a rede:**
   - Certifique-se de que todos os dispositivos estão na mesma rede
   - O IP `10.147.18.132` deve estar acessível

## 📋 Arquivos

- `upload_arquivos.html` - Formulário de upload
- `app.py` - Servidor Flask com processamento
- `servidor_simples.py` - Servidor HTTP simples
- `requirements.txt` - Dependências Python
- `iniciar_servidor.bat` - Script para Windows

## 🛠️ Solução de Problemas

**Erro de conexão recusada:**
- Verifique se a porta não está sendo usada por outro programa
- Verifique as configurações de firewall

**Não consegue acessar pela rede:**
- Verifique se o IP está correto: `ipconfig` no Windows
- Teste com `localhost` primeiro
- Verifique se o antivírus não está bloqueando

**Erro de módulo não encontrado:**
- Execute: `pip install -r requirements.txt` 