#!/bin/bash

# Script to run Histograma RGB application on Linux/Mac

echo "=================================="
echo "  Histograma RGB - Inicializando"
echo "=================================="
echo ""

# Check if Python is installed
if ! command -v python3 &> /dev/null; then
    echo "❌ Python 3 no está instalado"
    echo "Por favor instala Python 3.8 o superior"
    exit 1
fi

echo "✅ Python encontrado: $(python3 --version)"
echo ""

# Create virtual environment if it doesn't exist
if [ ! -d "venv" ]; then
    echo "📦 Creando entorno virtual..."
    python3 -m venv venv
    echo "✅ Entorno virtual creado"
else
    echo "✅ Entorno virtual ya existe"
fi

echo ""
echo "⚙️  Activando entorno virtual..."
source venv/bin/activate

echo ""
echo "📥 Instalando dependencias..."
pip install -q --upgrade pip
pip install -q -r requirements.txt
echo "✅ Dependencias instaladas"

echo ""
echo "=================================="
echo "  Iniciando aplicación..."
echo "=================================="
echo "🌐 Abre tu navegador en: http://localhost:8501"
echo "⏹️  Presiona Ctrl+C para detener"
echo ""

streamlit run app.py
