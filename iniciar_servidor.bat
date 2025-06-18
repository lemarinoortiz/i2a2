@echo off
echo ========================================
echo    Servidor de Upload de Arquivos CSV
echo ========================================
echo.
echo Instalando dependencias...
pip install -r requirements.txt
echo.
echo Iniciando servidor...
echo Acesse: http://10.147.18.132:5678
echo.
python iniciar_servidor.py
pause 