# Histograma RGB - Documentación Técnica

## Resumen Ejecutivo

**Histograma RGB** es una aplicación interactiva de procesamiento de imágenes desarrollada en Python con Streamlit. Permite ajustar la saturación de canales RGB en tiempo real y visualizar los cambios mediante histogramas, descomposiciones de canales y conversiones a escala de grises.

## 📋 Tabla de Contenidos

1. [Objetivos](#objetivos)
2. [Tecnologías](#tecnologías)
3. [Arquitectura](#arquitectura)
4. [Funcionalidades](#funcionalidades)
5. [Instalación](#instalación)
6. [Uso](#uso)
7. [Fundamentos Matemáticos](#fundamentos-matemáticos)
8. [Limitaciones](#limitaciones)

---

## Objetivos

1. ✅ Descomponer imágenes en canales RGB individuales
2. ✅ Calcular y visualizar histogramas de cada canal
3. ✅ Aplicar control de saturación mediante sliders interactivos
4. ✅ Procesar en tiempo real sin lag
5. ✅ Exportar resultados para análisis posterior
6. ✅ Proporcionar interfaz intuitiva y educativa

---

## Tecnologías

| Librería | Versión | Propósito |
|----------|---------|----------|
| **Python** | 3.8+ | Lenguaje base |
| **Streamlit** | 1.28.0 | Framework web interactivo |
| **OpenCV** | 4.8.0 | Procesamiento profesional de imágenes |
| **NumPy** | 1.24.3 | Operaciones numéricas y arrays |
| **Matplotlib** | 3.7.2 | Visualización de histogramas |
| **Pillow** | 10.0.0 | Manejo de formatos de imagen |

### Por qué estas tecnologías

- **Streamlit**: Desarrollo rápido de interfaces interactivas sin JavaScript
- **OpenCV**: Estándar industrial para procesamiento de imágenes
- **NumPy**: Operaciones vectorizadas rápidas en GPU
- **Matplotlib**: Gráficos de calidad académica

---

## Arquitectura

```
┌─────────────────────────────────────────────────────┐
│     Interface Streamlit (app.py)                    │
│  - Widgets de UI                                     │
│  - Gestión de estado                                │
│  - Visualización de resultados                      │
└───────────────────┬─────────────────────────────────┘
                    │
    ┌───────────────┴──────────────────┐
    │                                  │
┌───▼──────────────────┐    ┌─────────▼──────────────┐
│ image_processor.py   │    │ histogram.py           │
│                      │    │                        │
│ - decompose_rgb()    │    │ - plot_histograms()    │
│ - apply_saturation() │    │ - calculate_histogram()│
│ - to_grayscale()     │    │ - get_stats()          │
│ - resize_image()     │    │ - plot_decomposition() │
│ - get_image_stats()  │    │                        │
└───┬──────────────────┘    └─────────┬──────────────┘
    │                                  │
    └───────────────┬──────────────────┘
                    │
    ┌───────────────▼──────────────────┐
    │  OpenCV + NumPy (Core)           │
    │  - cv2.split()                   │
    │  - cv2.merge()                   │
    │  - cv2.calcHist()                │
    │  - np.clip()                     │
    │  - np.mean(), np.std()           │
    └──────────────────────────────────┘
```

---

## Funcionalidades

### 1. Carga de Imagen

**Soporta:**
- Formatos: JPG, PNG, BMP, GIF
- Redimensionamiento automático (máximo 600px de ancho para rendimiento)
- Conversión automática BGR (OpenCV) ↔ RGB (visualización)

**Código:**
```python
image_bgr = cv2.imdecode(file_bytes, cv2.IMREAD_COLOR)
image_resized = processor.resize_image(image_bgr)
```

### 2. Control de Saturación RGB

**Características:**
- 3 sliders independientes (rango 0.0 a 2.0)
- Actualización en tiempo real (sin delay)
- Botón de reseteo para restaurar original
- Botón de escala de grises rápida

**Rango de valores:**
| Valor | Efecto |
|-------|--------|
| 0.0 | Elimina completamente el canal |
| 0.5 | Reduce 50% la intensidad |
| 1.0 | Imagen original sin cambios |
| 1.5 | Aumenta 50% la intensidad |
| 2.0 | Duplica la intensidad |

### 3. Visualización

- **Comparación lado a lado:** Original vs Procesada
- **6 Histogramas:** 3 canales × 2 versiones (original + procesado)
- **Descomposición de canales:** Visualización individual R, G, B
- **Escala de grises:** Versión B&N original y procesada
- **Estadísticas:** Media, desviación estándar por canal

### 4. Exportación

- Imagen procesada en PNG
- Versión en escala de grises
- Imagen original
- Parámetros aplicados registrados

---

## Instalación

### Opción 1: Instalación Manual

**Windows:**
```batch
git clone https://github.com/ajkarots/histograma-rgb.git
cd histograma-rgb
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
streamlit run app.py
```

**Linux/Mac:**
```bash
git clone https://github.com/ajkarots/histograma-rgb.git
cd histograma-rgb
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
streamlit run app.py
```

### Opción 2: Usar Script de Ejecución

**Windows:**
```batch
run.bat
```

**Linux/Mac:**
```bash
bash run.sh
```

Los scripts crean automáticamente el entorno virtual e instalan dependencias.

---

## Uso

### Flujo Básico

1. **Inicia la aplicación:**
   ```bash
   streamlit run app.py
   ```

2. **Se abre en el navegador** (generalmente http://localhost:8501)

3. **Carga una imagen:**
   - Usa el widget "Selecciona una imagen" en la barra lateral
   - Formatos soportados: JPG, PNG, BMP, GIF

4. **Ajusta los sliders:**
   - Mueve los sliders de R, G, B independientemente
   - Observa cambios en tiempo real

5. **Explora las visualizaciones:**
   - Imágenes lado a lado
   - Histogramas comparativos
   - Descomposiciones de canales
   - Escala de grises

6. **Exporta resultados:**
   - Descarga imagen procesada, B&N u original

### Ejemplos de Uso

**Ejemplo 1: Potenciar Colores Rojos**
```
Rojo:  1.8x
Verde: 1.0x
Azul:  1.0x
→ Imagen con tonos rojos más intensos
```

**Ejemplo 2: Efecto Azul Frío**
```
Rojo:  0.7x
Verde: 0.8x
Azul:  1.5x
→ Imagen con predominancia azul, tonos fríos
```

**Ejemplo 3: Oscurecer Imagen**
```
Rojo:  0.5x
Verde: 0.5x
Azul:  0.5x
→ Imagen más oscura (mitad de intensidad)
```

**Ejemplo 4: Eliminar Verde (efecto magenta)**
```
Rojo:  1.2x
Verde: 0.0x
Azul:  1.2x
→ Imagen sin canal verde
```

---

## Fundamentos Matemáticos

### Descomposición RGB

Una imagen RGB se representa como tres matrices 2D:

```
Imagen = [Canal_Rojo, Canal_Verde, Canal_Azul]

Donde cada pixel = (R, G, B) ∈ [0, 255]³
```

**En OpenCV (formato BGR):**
```python
B, G, R = cv2.split(image)
```

### Aplicación de Saturación

Para cada canal:

```
Canal_procesado[i, j] = min(255, max(0, Canal_original[i, j] × factor))
```

**Descripción:**
- Multiplica cada píxel por el factor
- `max(0, ...)`: Asegura no ir por debajo de 0
- `min(255, ...)`: Asegura no superar 255 (clipping)
- Resultado: píxeles en rango válido [0, 255]

**Implementación:**
```python
canal_float = canal.astype(np.float32) * factor
canal_clipped = np.clip(canal_float, 0, 255).astype(np.uint8)
```

### Histograma

Un histograma cuenta la frecuencia de cada nivel de intensidad:

```
H[i] = número de píxeles con intensidad i
Donde: i ∈ [0, 255]
```

**Propiedades:**
- Rango X: 0 a 255 (niveles de intensidad)
- Rango Y: 0 a altura×ancho (cantidad de píxeles)
- Área total bajo la curva = total de píxeles

**Cálculo con OpenCV:**
```python
hist = cv2.calcHist([image], [channel], None, [256], [0, 256])
```

### Conversión a Escala de Grises

Usando método de promedio ponderado (estándar internacional):

```
Gris[i, j] = 0.299 × R[i, j] + 0.587 × G[i, j] + 0.114 × B[i, j]
```

**Pesos:**
- Rojo: 30% (menos sensibilidad visual)
- Verde: 59% (mayor sensibilidad visual)
- Azul: 11% (menor sensibilidad visual)

**Implementación OpenCV:**
```python
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
```

### Estadísticas por Canal

**Media (promedio de intensidades):**
```
μ = (1/N) × Σ(intensidad_i)
```

**Desviación Estándar (variabilidad):**
```
σ = √[(1/N) × Σ(intensidad_i - μ)²]
```

---

## Limitaciones Técnicas

### Hardware
- **Tamaño máximo de imagen:** 600px de ancho (escalado automático)
- **Memoria:** Depende de disponibilidad del sistema
- **Velocidad:** Mejor en SSD, puede ser lenta en HDD

### Software
- **Precisión:** 8 bits por canal (0-255)
- **Precisión de sliders:** 0.05 incrementos
- **Velocidad de actualización:** Limitada por refresh de Streamlit (~0.5s)

### Funcionalidad
- No soporta:
  - Imágenes CMYK
  - Video (solo imágenes estáticas)
  - Lotes (batch processing)
  - Filtros avanzados (blur, sharpen, etc.)

---

## Próximas Mejoras

- [ ] Agregar histograma acumulativo
- [ ] Ecualización de histograma
- [ ] Más filtros (blur, sharpen, dilate, erode)
- [ ] Exportación a PDF automática
- [ ] Procesamiento por lotes (batch)
- [ ] Interfaz de línea de comandos (CLI)
- [ ] Soporte para video
- [ ] Análisis de contraste

---

## Referencias

- [OpenCV Docs](https://docs.opencv.org/)
- [Streamlit Docs](https://docs.streamlit.io/)
- [NumPy Reference](https://numpy.org/doc/)
- [Matplotlib Guide](https://matplotlib.org/)
- [Digital Image Processing by Gonzalez & Woods](https://www.amazon.com/Digital-Image-Processing-Rafael-Gonzalez/dp/0133356728/)

---

## Autor

**Proyecto:** Histograma RGB  
**Asignatura:** Inteligencia Artificial y Tratamiento de Imágenes  
**Autor:** ajkarots  
**Fecha:** Abril 2026  
**Versión:** 1.0

---

## Notas de Desarrollo

### Estructura de Carpetas

```
histograma-rgb/
├── app.py                      # Aplicación principal (600+ líneas)
├── requirements.txt            # Dependencias
├── README.md                   # Guía de usuario
├── DOCUMENTACION_TECNICA.md   # Este archivo
├── run.sh                      # Script Linux/Mac
├── run.bat                     # Script Windows
├── .gitignore                  # Configuración git
└── utils/                      # Módulos reutilizables
    ├── __init__.py
    ├── image_processor.py      # Clase ImageProcessor (80+ líneas)
    └── histogram.py            # Clase HistogramPlotter (60+ líneas)
```

### Decisiones de Diseño

1. **Streamlit sobre Flask:** Desarrollo rápido, no requiere HTML/CSS/JS
2. **OpenCV sobre PIL:** Más rápido, mejor para procesamiento
3. **Session state:** Evita recalcular toda la imagen en cada cambio
4. **Redimensionamiento automático:** Balance entre precisión y velocidad
5. **Módulos separados:** Código limpio y reutilizable

---

*Documento actualizado: Abril 2026*
