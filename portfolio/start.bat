@echo off
cd /d "%~dp0"
start "Portfolio Server" python serve.py
timeout /t 2 /nobreak >nul
start "" http://localhost:5500/index.html
