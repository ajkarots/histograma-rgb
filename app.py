"""Main Streamlit application for RGB Histogram Processing."""

import streamlit as st
import cv2
import numpy as np
from PIL import Image
import io
from utils.image_processor import ImageProcessor
from utils.histogram import HistogramPlotter

# Configure page
st.set_page_config(
    page_title="Histograma RGB",
    page_icon="🎨",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS
st.markdown("""
    <style>
    .main-title {
        font-size: 2.5em;
        color: #1f77b4;
        text-align: center;
        margin-bottom: 10px;
    }
    .subtitle {
        font-size: 1.2em;
        color: #666;
        text-align: center;
        margin-bottom: 30px;
    }
    .info-box {
        background-color: #e8f4f8;
        padding: 15px;
        border-radius: 8px;
        border-left: 4px solid #1f77b4;
    }
    </style>
""", unsafe_allow_html=True)

# Title
st.markdown('<h1 class="main-title">🎨 Procesador de Histograma RGB</h1>', unsafe_allow_html=True)
st.markdown('<p class="subtitle">Control interactivo de saturación de canales de color</p>', unsafe_allow_html=True)

# Initialize session state
if 'processor' not in st.session_state:
    st.session_state.processor = ImageProcessor()
if 'plotter' not in st.session_state:
    st.session_state.plotter = HistogramPlotter()
if 'original_image' not in st.session_state:
    st.session_state.original_image = None
if 'red_factor' not in st.session_state:
    st.session_state.red_factor = 1.0
if 'green_factor' not in st.session_state:
    st.session_state.green_factor = 1.0
if 'blue_factor' not in st.session_state:
    st.session_state.blue_factor = 1.0

# Sidebar - Image upload
st.sidebar.header("📂 Carga de Imagen")
uploaded_file = st.sidebar.file_uploader(
    "Selecciona una imagen",
    type=["jpg", "jpeg", "png", "bmp", "gif"],
    help="Formatos soportados: JPG, PNG, BMP, GIF"
)

if uploaded_file is not None:
    # Load image
    file_bytes = np.asarray(bytearray(uploaded_file.read()), dtype=np.uint8)
    image_bgr = cv2.imdecode(file_bytes, cv2.IMREAD_COLOR)
    st.session_state.original_image = st.session_state.processor.resize_image(image_bgr)

# Sidebar - Saturation controls
st.sidebar.header("🎚️ Control de Saturación")

col1, col2 = st.sidebar.columns([3, 1])
with col1:
    st.session_state.red_factor = st.slider(
        "🔴 Rojo",
        0.0, 2.0, 1.0,
        step=0.05,
        help="Intensidad del canal rojo (0.0 elimina, 1.0 original, 2.0 duplica)"
    )
with col2:
    st.metric("x", f"{st.session_state.red_factor:.2f}")

col1, col2 = st.sidebar.columns([3, 1])
with col1:
    st.session_state.green_factor = st.slider(
        "🟢 Verde",
        0.0, 2.0, 1.0,
        step=0.05,
        help="Intensidad del canal verde (0.0 elimina, 1.0 original, 2.0 duplica)"
    )
with col2:
    st.metric("x", f"{st.session_state.green_factor:.2f}")

col1, col2 = st.sidebar.columns([3, 1])
with col1:
    st.session_state.blue_factor = st.slider(
        "🔵 Azul",
        0.0, 2.0, 1.0,
        step=0.05,
        help="Intensidad del canal azul (0.0 elimina, 1.0 original, 2.0 duplica)"
    )
with col2:
    st.metric("x", f"{st.session_state.blue_factor:.2f}")

# Reset button
if st.sidebar.button("🔄 Resetear a Original", use_container_width=True, key="reset"):
    st.session_state.red_factor = 1.0
    st.session_state.green_factor = 1.0
    st.session_state.blue_factor = 1.0
    st.rerun()

# Main content
if st.session_state.original_image is not None:
    # Process image
    processed_image = st.session_state.processor.apply_saturation(
        st.session_state.original_image,
        st.session_state.red_factor,
        st.session_state.green_factor,
        st.session_state.blue_factor
    )
    
    # Convert to grayscale
    original_gray = st.session_state.processor.to_grayscale(st.session_state.original_image)
    processed_gray = st.session_state.processor.to_grayscale(processed_image)
    
    # Convert BGR to RGB for display
    original_rgb = cv2.cvtColor(st.session_state.original_image, cv2.COLOR_BGR2RGB)
    processed_rgb = cv2.cvtColor(processed_image, cv2.COLOR_BGR2RGB)
    
    # Section 1: Image Comparison
    st.header("📷 Comparación de Imágenes")
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("Imagen Original")
        st.image(original_rgb, use_column_width=True)
    
    with col2:
        st.subheader("Imagen Procesada")
        st.image(processed_rgb, use_column_width=True)
    
    # Section 2: Histograms
    st.header("📊 Histogramas RGB")
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.subheader("Canal Rojo")
        fig_r_orig, fig_r_proc = st.session_state.plotter.plot_histograms(
            st.session_state.original_image,
            processed_image,
            channel=2,  # Red in BGR
            channel_name="Rojo"
        )
        st.write("**Original**")
        st.pyplot(fig_r_orig)
        st.write("**Procesado**")
        st.pyplot(fig_r_proc)
    
    with col2:
        st.subheader("Canal Verde")
        fig_g_orig, fig_g_proc = st.session_state.plotter.plot_histograms(
            st.session_state.original_image,
            processed_image,
            channel=1,  # Green in BGR
            channel_name="Verde"
        )
        st.write("**Original**")
        st.pyplot(fig_g_orig)
        st.write("**Procesado**")
        st.pyplot(fig_g_proc)
    
    with col3:
        st.subheader("Canal Azul")
        fig_b_orig, fig_b_proc = st.session_state.plotter.plot_histograms(
            st.session_state.original_image,
            processed_image,
            channel=0,  # Blue in BGR
            channel_name="Azul"
        )
        st.write("**Original**")
        st.pyplot(fig_b_orig)
        st.write("**Procesado**")
        st.pyplot(fig_b_proc)
    
    # Section 3: RGB Decomposition
    st.header("🎨 Descomposición de Canales RGB")
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.subheader("Canal Rojo")
        col_a, col_b = st.columns(2)
        with col_a:
            st.write("**Original**")
            red_orig = np.zeros_like(original_rgb)
            red_orig[:,:,0] = original_rgb[:,:,0]
            st.image(red_orig, use_column_width=True)
        with col_b:
            st.write("**Procesada**")
            red_proc = np.zeros_like(processed_rgb)
            red_proc[:,:,0] = processed_rgb[:,:,0]
            st.image(red_proc, use_column_width=True)
    
    with col2:
        st.subheader("Canal Verde")
        col_a, col_b = st.columns(2)
        with col_a:
            st.write("**Original**")
            green_orig = np.zeros_like(original_rgb)
            green_orig[:,:,1] = original_rgb[:,:,1]
            st.image(green_orig, use_column_width=True)
        with col_b:
            st.write("**Procesada**")
            green_proc = np.zeros_like(processed_rgb)
            green_proc[:,:,1] = processed_rgb[:,:,1]
            st.image(green_proc, use_column_width=True)
    
    with col3:
        st.subheader("Canal Azul")
        col_a, col_b = st.columns(2)
        with col_a:
            st.write("**Original**")
            blue_orig = np.zeros_like(original_rgb)
            blue_orig[:,:,2] = original_rgb[:,:,2]
            st.image(blue_orig, use_column_width=True)
        with col_b:
            st.write("**Procesada**")
            blue_proc = np.zeros_like(processed_rgb)
            blue_proc[:,:,2] = processed_rgb[:,:,2]
            st.image(blue_proc, use_column_width=True)
    
    # Section 4: Grayscale
    st.header("⚫ Escala de Grises")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("Original en B&N")
        st.image(original_gray, use_column_width=True, channels="GRAY")
    
    with col2:
        st.subheader("Procesada en B&N")
        st.image(processed_gray, use_column_width=True, channels="GRAY")
    
    # Section 5: Statistics
    st.header("📈 Estadísticas de Canales")
    
    stats_orig = st.session_state.processor.get_image_stats(st.session_state.original_image)
    stats_proc = st.session_state.processor.get_image_stats(processed_image)
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.write("**Rojo**")
        c1, c2 = st.columns(2)
        with c1:
            st.metric("Original (μ)", f"{stats_orig['red']['mean']:.1f}")
            st.metric("Original (σ)", f"{stats_orig['red']['std']:.1f}")
        with c2:
            st.metric("Procesado (μ)", f"{stats_proc['red']['mean']:.1f}")
            st.metric("Procesado (σ)", f"{stats_proc['red']['std']:.1f}")
    
    with col2:
        st.write("**Verde**")
        c1, c2 = st.columns(2)
        with c1:
            st.metric("Original (μ)", f"{stats_orig['green']['mean']:.1f}")
            st.metric("Original (σ)", f"{stats_orig['green']['std']:.1f}")
        with c2:
            st.metric("Procesado (μ)", f"{stats_proc['green']['mean']:.1f}")
            st.metric("Procesado (σ)", f"{stats_proc['green']['std']:.1f}")
    
    with col3:
        st.write("**Azul**")
        c1, c2 = st.columns(2)
        with c1:
            st.metric("Original (μ)", f"{stats_orig['blue']['mean']:.1f}")
            st.metric("Original (σ)", f"{stats_orig['blue']['std']:.1f}")
        with c2:
            st.metric("Procesado (μ)", f"{stats_proc['blue']['mean']:.1f}")
            st.metric("Procesado (σ)", f"{stats_proc['blue']['std']:.1f}")
    
    # Section 6: Downloads
    st.header("💾 Descargas")
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        # Processed image
        processed_pil = Image.fromarray(processed_rgb)
        buf_color = io.BytesIO()
        processed_pil.save(buf_color, format="PNG")
        buf_color.seek(0)
        
        st.download_button(
            label="📥 Imagen Procesada (PNG)",
            data=buf_color,
            file_name="imagen_procesada.png",
            mime="image/png",
            use_container_width=True
        )
    
    with col2:
        # Grayscale image
        processed_gray_pil = Image.fromarray(processed_gray)
        buf_gray = io.BytesIO()
        processed_gray_pil.save(buf_gray, format="PNG")
        buf_gray.seek(0)
        
        st.download_button(
            label="📥 B&N (PNG)",
            data=buf_gray,
            file_name="imagen_byn.png",
            mime="image/png",
            use_container_width=True
        )
    
    with col3:
        # Info
        info_text = f"""
        **Parámetros Aplicados:**
        - Rojo: {st.session_state.red_factor:.2f}x
        - Verde: {st.session_state.green_factor:.2f}x
        - Azul: {st.session_state.blue_factor:.2f}x
        
        **Dimensiones:**
        - {processed_image.shape[1]} × {processed_image.shape[0]} px
        - {processed_image.shape[0] * processed_image.shape[1]:,} píxeles
        """
        st.info(info_text)

else:
    # No image loaded
    st.markdown("""
    <div class="info-box">
    <h3>👈 Por favor, carga una imagen</h3>
    <p>1. Selecciona una imagen en la barra lateral</p>
    <p>2. Ajusta los sliders RGB según lo desees</p>
    <p>3. Observa los cambios en tiempo real</p>
    <p>4. Descarga los resultados cuando termines</p>
    </div>
    """, unsafe_allow_html=True)
