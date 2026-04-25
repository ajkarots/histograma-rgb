# 🎨 Histograma RGB - Procesador Interactivo de Imágenes

![Python 3.8+](https://img.shields.io/badge/Python-3.8%2B-blue)
![Streamlit](https://img.shields.io/badge/Streamlit-1.28.0-red)
![License](https://img.shields.io/badge/License-MIT-green)

Aplicación interactiva para procesamiento de imágenes con control en tiempo real de canales RGB. Diseñada para análisis y educación en tratamiento de imágenes e inteligencia artificial.

## 🎯 Características Principales

- ✅ **Carga de imágenes** - Soporta JPG, PNG, BMP, GIF
- ✅ **3 Sliders RGB** - Control independiente de saturación (0.0 a 2.0x)
- ✅ **6 Histogramas** - Visualización de 3 canales (original + procesado)
- ✅ **Descomposición de canales** - Visualización individual R, G, B
- ✅ **Escala de grises** - Conversión a B&N automática
- ✅ **Estadísticas** - Media y desviación estándar por canal
- ✅ **Tiempo real** - Actualización instantánea de cambios
- ✅ **Exportación** - Descarga de resultados en PNG

## 🚀 Inicio Rápido

### Opción 1: Script Automático (Recomendado)

**Windows:**
```bash
run.bat
```

**Linux/Mac:**
```bash
bash run.sh
```

### Opción 2: Manual

```bash
# Clonar repositorio
git clone https://github.com/ajkarots/histograma-rgb.git
cd histograma-rgb

# Crear entorno virtual
python -m venv venv

# Activar entorno
# Windows:
venv\Scripts\activate
# Linux/Mac:
source venv/bin/activate

# Instalar dependencias
pip install -r requirements.txt

# Ejecutar
streamlit run app.py
```

## 📖 Uso

1. **Inicia la aplicación** usando uno de los métodos anteriores
2. **Se abre en el navegador** (generalmente http://localhost:8501)
3. **Carga una imagen** usando el widget en la barra lateral
4. **Ajusta los sliders RGB** para modificar la saturación
5. **Observa los cambios** en tiempo real:
   - Imágenes lado a lado
   - Histogramas comparativos
   - Descomposición de canales
   - Escala de grises
6. **Descarga los resultados** en PNG cuando termines

## 📊 Ejemplo de Uso

### Potenciar Rojo
- Rojo: 1.8x
- Verde: 1.0x
- Azul: 1.0x
→ Imagen con tonos rojos más intensos

### Efecto Azul Frío
- Rojo: 0.7x
- Verde: 0.8x
- Azul: 1.5x
→ Imagen con predominancia azul

### Oscurecer Imagen
- Rojo: 0.5x
- Verde: 0.5x
- Azul: 0.5x
→ Imagen 50% más oscura

## 📁 Estructura del Proyecto

```
histograma-rgb/
├── app.py                      # Aplicación principal
├── requirements.txt            # Dependencias
├── README.md                   # Este archivo
├── DOCUMENTACION_TECNICA.md   # Documentación completa
├── run.sh                      # Script para Linux/Mac
├── run.bat                     # Script para Windows
├── .gitignore                  # Configuración git
└── utils/
    ├── __init__.py
    ├── image_processor.py      # Procesamiento de imágenes
    └── histogram.py            # Cálculo de histogramas
```

## 🛠️ Tecnologías

| Librería | Versión | Propósito |
|----------|---------|----------|
| Python | 3.8+ | Lenguaje base |
| Streamlit | 1.28.0 | Interfaz web |
| OpenCV | 4.8.0 | Procesamiento de imágenes |
| NumPy | 1.24.3 | Computación numérica |
| Matplotlib | 3.7.2 | Visualización de histogramas |
| Pillow | 10.0.0 | Manejo de formatos |

## 📚 Documentación

Para más detalles sobre la implementación técnica, fundamentos matemáticos y limitaciones, consulta:

- **[DOCUMENTACION_TECNICA.md](DOCUMENTACION_TECNICA.md)** - Documentación completa

## 🧮 Fundamentos Matemáticos

### Saturación de Canal
```
Canal_procesado[i] = min(255, max(0, Canal_original[i] × factor))
```

### Histograma
```
H[i] = cantidad de píxeles con intensidad i
Donde: i ∈ [0, 255]
```

### Escala de Grises
```
Gris[i] = 0.299×R + 0.587×G + 0.114×B
```

## 🔧 Requisitos

- Python 3.8 o superior
- pip (gestor de paquetes Python)
- 100 MB de espacio en disco
- Navegador web moderno

## 📋 Pasos de Instalación Detallados

### Windows

1. Descargar Python desde [python.org](https://www.python.org/downloads/)
2. Instalar Python (marcar "Add Python to PATH")
3. Descargar o clonar este repositorio
4. Abrir CMD/PowerShell en la carpeta del proyecto
5. Ejecutar `run.bat`

### Linux/Mac

1. Python generalmente viene preinstalado
2. Clonar repositorio: `git clone https://github.com/ajkarots/histograma-rgb.git`
3. Entrar a la carpeta: `cd histograma-rgb`
4. Ejecutar: `bash run.sh`

## 🐛 Solución de Problemas

### "Python no reconocido"
- Verifica que Python esté instalado: `python --version`
- Reinstala Python marcando "Add Python to PATH"

### "No se encuentran los módulos"
- Asegúrate de estar en el entorno virtual
- Ejecuta: `pip install -r requirements.txt`

### "Puerto 8501 en uso"
- Cierra otras instancias de Streamlit
- O usa: `streamlit run app.py --server.port 8502`

## 📄 Licencia

Este proyecto está disponible bajo licencia MIT. Ver [LICENSE](LICENSE) para más detalles.

## 👤 Autor

**Jonathan Ojeda (ajkarots)**

- GitHub: [@ajkarots](https://github.com/ajkarots)
- Proyecto académico para Inteligencia Artificial y Tratamiento de Imágenes

## 🔗 Enlaces Útiles

- [OpenCV Documentation](https://docs.opencv.org/)
- [Streamlit Documentation](https://docs.streamlit.io/)
- [NumPy Reference](https://numpy.org/doc/)
- [Matplotlib Guide](https://matplotlib.org/)

## 💡 Próximas Mejoras

- [ ] Histograma acumulativo
- [ ] Ecualización de histograma
- [ ] Más filtros (blur, sharpen, etc.)
- [ ] Exportación automática a PDF
- [ ] Procesamiento por lotes
- [ ] Interfaz de línea de comandos (CLI)
- [ ] Soporte para video

## 📞 Soporte

Para reportar bugs o sugerir mejoras, abre un [issue en GitHub](https://github.com/ajkarots/histograma-rgb/issues).

---

**Última actualización**: Abril 2026
