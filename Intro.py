import streamlit as st
from PIL import Image

# Configuración de la página
st.set_page_config(
    page_title="Aplicaciones de IA",
    page_icon="✨",
    layout="wide"
)

# CSS personalizado para el tema de fantasía morado pastel
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;500;600&display=swap');
    
    * {
        font-family: 'Poppins', sans-serif;
    }
    
    .main {
        background: linear-gradient(135deg, #f5f0ff 0%, #e6e6fa 50%, #d8bfd8 100%);
    }
    
    .stApp {
        background: linear-gradient(135deg, #f5f0ff 0%, #e6e6fa 50%, #d8bfd8 100%);
    }
    
    .css-1d391kg, .css-1lcbmhc {
        background-color: rgba(255, 255, 255, 0.9) !important;
        backdrop-filter: blur(10px);
        border-radius: 15px;
        border: 1px solid #d8bfd8;
        padding: 20px;
        margin: 10px 0;
        box-shadow: 0 4px 15px rgba(128, 0, 128, 0.1);
    }
    
    .stTitle {
        color: #9370db !important;
        text-align: center;
        font-weight: 600;
        text-shadow: 2px 2px 4px rgba(147, 112, 219, 0.3);
        margin-bottom: 30px;
    }
    
    .stSubheader {
        color: #8a2be2 !important;
        font-weight: 500;
        border-bottom: 2px solid #d8bfd8;
        padding-bottom: 8px;
        margin-bottom: 15px;
    }
    
    .sidebar .sidebar-content {
        background: linear-gradient(180deg, #9370db 0%, #8a2be2 100%) !important;
        color: white;
    }
    
    .stButton>button {
        background: linear-gradient(45deg, #9370db, #8a2be2);
        color: white;
        border: none;
        border-radius: 25px;
        padding: 10px 20px;
        font-weight: 500;
        transition: all 0.3s ease;
    }
    
    .stButton>button:hover {
        transform: translateY(-2px);
        box-shadow: 0 5px 15px rgba(147, 112, 219, 0.4);
    }
    
    .card {
        background: rgba(255, 255, 255, 0.95);
        border-radius: 15px;
        padding: 20px;
        margin: 10px 0;
        border: 1px solid #e6e6fa;
        box-shadow: 0 4px 12px rgba(147, 112, 219, 0.1);
        transition: transform 0.3s ease;
    }
    
    .card:hover {
        transform: translateY(-5px);
        box-shadow: 0 8px 20px rgba(147, 112, 219, 0.2);
    }
    
    .link-button {
        background: linear-gradient(45deg, #ba55d3, #9370db);
        color: white !important;
        padding: 8px 16px;
        border-radius: 20px;
        text-decoration: none;
        display: inline-block;
        margin-top: 10px;
        font-size: 14px;
        transition: all 0.3s ease;
    }
    
    .link-button:hover {
        transform: scale(1.05);
        box-shadow: 0 4px 12px rgba(147, 112, 219, 0.3);
    }
</style>
""", unsafe_allow_html=True)

# Título principal
st.title("✨ Aplicaciones de Inteligencia Artificial")

# Sidebar mejorado
with st.sidebar:
    st.markdown("""
    <div style='text-align: center; padding: 20px 0;'>
        <h2 style='color: white; margin-bottom: 20px;'>🧠 Portal IA</h2>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("---")
    
    parrafo = (
        "La inteligencia artificial permite mejorar la toma de decisiones con el uso de datos, "
        "automatizar tareas rutinarias y proporcionar análisis avanzados en tiempo real, lo que "
        "resulta en una mayor eficiencia y precisión en diversos campos."
    )
    
    st.markdown(f"""
    <div style='background: rgba(255,255,255,0.1); padding: 15px; border-radius: 10px; margin: 10px 0;'>
        <p style='color: white; font-size: 14px; line-height: 1.5;'>{parrafo}</p>
    </div>
    """, unsafe_allow_html=True)

# Enlace principal
url_ia = "https://sites.google.com/view/aplicacionesdeia/inicio"
st.markdown(f"""
<div style='background: linear-gradient(45deg, #9370db, #8a2be2); padding: 20px; border-radius: 15px; text-align: center; margin: 20px 0;'>
    <h3 style='color: white; margin: 0;'>📚 Recursos y Ejercicios Prácticos</h3>
    <p style='color: #f0f0f0; margin: 10px 0;'>Encuentra páginas y ejercicios prácticos en el siguiente enlace</p>
    <a href='{url_ia}' class='link-button' target='_blank'>Explorar Recursos</a>
</div>
""", unsafe_allow_html=True)

# Lista de aplicaciones con 20 slots
apps = [
    {
        "title": "Conversión de texto a voz",
        "image": "txt_to_audio2.png",
        "description": "Usaremos una de las aplicaciones de Inteligencia Artificial",
        "url": "https://imultimod.streamlit.app/"
    },
    {
        "title": "Reconocimiento de Objetos",
        "image": "txt_to_audio.png",
        "description": "Veremos como se detectan objetos en Imágenes",
        "url": "https://xn3pg24ztuv6fdiqon8qn3.streamlit.app/"
    },
    {
        "title": "Entrenando Modelos",
        "image": "OIG5.jpg",
        "description": "Veremos como puedes usar tu modelo entrenado",
        "url": "https://xn3pg24ztuv6fdiqon8qn3.streamlit.app/"
    },
    {
        "title": "Conversión de voz a texto",
        "image": "OIG8.jpg",
        "description": "Aplicación que usa la conversión de voz a texto",
        "url": "https://traductor-ab0sp9f6fi.streamlit.app/"
    },
    {
        "title": "Análisis de Datos",
        "image": "data_analisis.png",
        "description": "Veremos como se pueden analizar datos usando agentes",
        "url": "https://asistpy-csv.streamlit.app/"
    },
    {
        "title": "Transcriptor Audio y Video",
        "image": "OIG3.jpg",
        "description": "Realizamos transcripciones de audio/video",
        "url": "https://transcript-whisper.streamlit.app/"
    },
    {
        "title": "Generación en Contexto",
        "image": "Chat_pdf.png",
        "description": "Aplicación que usa RAG a partir de un documento (PDF)",
        "url": "https://chatpdf-cc.streamlit.app/"
    },
    {
        "title": "Análisis de Imagen",
        "image": "OIG4.jpg",
        "description": "Capacidad de análisis en Imágenes",
        "url": "https://vision2-gpt4o.streamlit.app/"
    },
    {
        "title": "Sistema Ciberfísico",
        "image": "OIG6.jpg",
        "description": "Capacidad de interacción con el mundo físico",
        "url": "https://vision2-gpt4o.streamlit.app/"
    },
    # Slots adicionales para completar 20
    {
        "title": "Chatbot Inteligente",
        "image": "OIG5.jpg",
        "description": "Asistente virtual con capacidades avanzadas",
        "url": "#"
    },
    {
        "title": "Reconocimiento Facial",
        "image": "OIG8.jpg",
        "description": "Sistema de identificación biométrica",
        "url": "#"
    },
    {
        "title": "Generación de Imágenes",
        "image": "OIG3.jpg",
        "description": "Creación de imágenes con IA",
        "url": "#"
    },
    {
        "title": "Análisis de Sentimientos",
        "image": "data_analisis.png",
        "description": "Análisis emocional en texto",
        "url": "#"
    },
    {
        "title": "Traducción Automática",
        "image": "txt_to_audio2.png",
        "description": "Traducción en tiempo real",
        "url": "#"
    },
    {
        "title": "Recomendaciones",
        "image": "Chat_pdf.png",
        "description": "Sistema de recomendación personalizado",
        "url": "#"
    },
    {
        "title": "Detección de Anomalías",
        "image": "OIG4.jpg",
        "description": "Identificación de patrones inusuales",
        "url": "#"
    },
    {
        "title": "Procesamiento de Lenguaje",
        "image": "OIG6.jpg",
        "description": "Comprensión del lenguaje natural",
        "url": "#"
    },
    {
        "title": "Visión por Computadora",
        "image": "txt_to_audio.png",
        "description": "Análisis avanzado de imágenes",
        "url": "#"
    },
    {
        "title": "Automación de Procesos",
        "image": "OIG5.jpg",
        "description": "Automatización inteligente de tareas",
        "url": "#"
    },
    {
        "title": "Predicción de Series Temporales",
        "image": "data_analisis.png",
        "description": "Análisis predictivo avanzado",
        "url": "#"
    }
]

# Mostrar aplicaciones en 3 columnas
st.markdown("## 🎯 Aplicaciones Disponibles")
st.markdown("---")

cols = st.columns(3)

for i, app in enumerate(apps):
    with cols[i % 3]:
        st.markdown(f"""
        <div class='card'>
            <h4 style='color: #9370db; margin-bottom: 10px;'>{app['title']}</h4>
            <div style='text-align: center; margin: 15px 0;'>
                <div style='background: linear-gradient(45deg, #e6e6fa, #f5f0ff); 
                            padding: 20px; border-radius: 10px; display: inline-block;'>
                    <span style='font-size: 2em;'>🖼️</span>
                </div>
            </div>
            <p style='color: #666; font-size: 14px; line-height: 1.4;'>{app['description']}</p>
            <a href='{app['url']}' class='link-button' target='_blank'>Acceder</a>
        </div>
        """, unsafe_allow_html=True)

# Footer
st.markdown("---")
st.markdown("""
<div style='text-align: center; color: #9370db; padding: 20px;'>
    <p style='margin: 0;'>✨ Desarrollado con Streamlit y IA ✨</p>
</div>
""", unsafe_allow_html=True)
