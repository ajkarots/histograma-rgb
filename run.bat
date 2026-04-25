@echo off
REM Script to run Histograma RGB application on Windows

echo ==================================
echo   Histograma RGB - Inicializando
echo ==================================
echo.

REM Check if Python is installed
python --version >nul 2>&1
if errorlevel 1 (
    echo X Python no esta instalado
    echo Por favor instala Python 3.8 o superior
    pause
    exit /b 1
)

for /f "tokens=*" %%i in ('python --version') do echo ^/  %%i
echo.

REM Create virtual environment if it doesn't exist
if not exist "venv" (
    echo - Creando entorno virtual...
    python -m venv venv
    echo ^/  Entorno virtual creado
) else (
    echo ^/  Entorno virtual ya existe
)

echo.
echo - Activando entorno virtual...
call venv\Scripts\activate.bat

echo.
echo - Instalando dependencias...
pip install -q --upgrade pip
pip install -q -r requirements.txt
echo ^/  Dependencias instaladas

echo.
echo ==================================
echo   Iniciando aplicacion...
echo ==================================
echo - Abre tu navegador en: http://localhost:8501
echo - Presiona Ctrl+C para detener
echo.

streamlit run app.py

pause
