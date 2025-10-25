import streamlit as st
from PIL import Image
import requests
import json

# Configuración de la página
st.set_page_config(
    page_title="Aplicaciones de IA",
    page_icon="✨",
    layout="wide"
)

# CSS personalizado para el tema de fantasía morado pastel con animaciones
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
    
    .card {
        background: rgba(255, 255, 255, 0.95);
        border-radius: 15px;
        padding: 20px;
        margin: 10px 0;
        border: 1px solid #e6e6fa;
        box-shadow: 0 4px 12px rgba(147, 112, 219, 0.1);
        transition: all 0.3s ease;
        height: 320px;
        display: flex;
        flex-direction: column;
        justify-content: space-between;
    }
    
    .card:hover {
        transform: translateY(-5px);
        box-shadow: 0 8px 25px rgba(147, 112, 219, 0.2);
    }
    
    .card-content {
        flex-grow: 1;
        display: flex;
        flex-direction: column;
    }
    
    .card-icon {
        height: 80px;
        margin-bottom: 15px;
        display: flex;
        align-items: center;
        justify-content: center;
    }
    
    .card-title {
        color: #9370db;
        font-size: 16px;
        font-weight: 600;
        margin-bottom: 10px;
        min-height: 40px;
        display: flex;
        align-items: center;
    }
    
    .card-description {
        color: #666;
        font-size: 13px;
        line-height: 1.4;
        flex-grow: 1;
        margin-bottom: 15px;
    }
    
    .link-button {
        background: linear-gradient(45deg, #ba55d3, #9370db);
        color: white !important;
        padding: 8px 16px;
        border-radius: 20px;
        text-decoration: none;
        display: inline-block;
        text-align: center;
        font-size: 14px;
        transition: all 0.3s ease;
        border: none;
        cursor: pointer;
        width: 100%;
    }
    
    .link-button:hover {
        transform: scale(1.05);
        box-shadow: 0 4px 12px rgba(147, 112, 219, 0.3);
        color: white;
        text-decoration: none;
    }
    
    .lottie-container {
        display: flex;
        justify-content: center;
        align-items: center;
    }
</style>
""", unsafe_allow_html=True)

# Lottie animations JSON para cada card (simplificadas)
lottie_animations = [
    # Animaciones tiernas para cada una de las 20 cards
    {"url": "https://assets1.lottiefiles.com/packages/lf20_gns0rlrk.json"},  # Robot
    {"url": "https://assets1.lottiefiles.com/packages/lf20_kxsd2ytq.json"},  # Voice
    {"url": "https://assets1.lottiefiles.com/packages/lf20_5mkr3lua.json"},  # Brain
    {"url": "https://assets1.lottiefiles.com/packages/lf20_vybwn7df.json"},  # Microphone
    {"url": "https://assets1.lottiefiles.com/packages/lf20_u8jppxsl.json"},  # Data
    {"url": "https://assets1.lottiefiles.com/packages/lf20_5mkm9egb.json"},  # Audio Wave
    {"url": "https://assets1.lottiefiles.com/packages/lf20_ibkg3j.json"},   # Document
    {"url": "https://assets1.lottiefiles.com/packages/lf20_issg1qzi.json"}, # Camera
    {"url": "https://assets1.lottiefiles.com/packages/lf20_5nk02qkz.json"}, # IoT
    {"url": "https://assets1.lottiefiles.com/packages/lf20_vybwn7df.json"}, # Chat
    {"url": "https://assets1.lottiefiles.com/packages/lf20_gns0rlrk.json"}, # Face ID
    {"url": "https://assets1.lottiefiles.com/packages/lf20_5mkm9egb.json"}, # Magic Wand
    {"url": "https://assets1.lottiefiles.com/packages/lf20_u8jppxsl.json"}, # Heart
    {"url": "https://assets1.lottiefiles.com/packages/lf20_ibkg3j.json"},   # Translate
    {"url": "https://assets1.lottiefiles.com/packages/lf20_issg1qzi.json"}, # Recommendation
    {"url": "https://assets1.lottiefiles.com/packages/lf20_5nk02qkz.json"}, # Alert
    {"url": "https://assets1.lottiefiles.com/packages/lf20_vybwn7df.json"}, # NLP
    {"url": "https://assets1.lottiefiles.com/packages/lf20_gns0rlrk.json"}, # Vision
    {"url": "https://assets1.lottiefiles.com/packages/lf20_5mkm9egb.json"}, # Automation
    {"url": "https://assets1.lottiefiles.com/packages/lf20_u8jppxsl.json"}  # Prediction
]

# Función para mostrar Lottie animation
def load_lottieanimation(url):
    try:
        r = requests.get(url)
        if r.status_code == 200:
            return r.json()
    except:
        return None

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

# Título principal
st.title("✨ Aplicaciones de Inteligencia Artificial")

# Enlace principal
url_ia = "https://sites.google.com/view/aplicacionesdeia/inicio"
st.markdown(f"""
<div style='background: linear-gradient(45deg, #9370db, #8a2be2); padding: 20px; border-radius: 15px; text-align: center; margin: 20px 0;'>
    <h3 style='color: white; margin: 0;'>📚 Recursos y Ejercicios Prácticos</h3>
    <p style='color: #f0f0f0; margin: 10px 0;'>Encuentra páginas y ejercicios prácticos en el siguiente enlace</p>
    <a href='{url_ia}' class='link-button' target='_blank' style='width: 200px; margin: 0 auto;'>Explorar Recursos</a>
</div>
""", unsafe_allow_html=True)

# Lista de aplicaciones con 20 slots
apps = [
    {
        "title": "Conversión de texto a voz",
        "description": "Usaremos una de las aplicaciones de Inteligencia Artificial para convertir texto en audio natural",
        "url": "https://imultimod.streamlit.app/",
        "icon": "🔊"
    },
    {
        "title": "Reconocimiento de Objetos",
        "description": "Veremos como se detectan objetos en Imágenes usando modelos de visión artificial",
        "url": "https://xn3pg24ztuv6fdiqon8qn3.streamlit.app/",
        "icon": "📷"
    },
    {
        "title": "Entrenando Modelos",
        "description": "Veremos como puedes usar tu modelo entrenado y desplegarlo en aplicaciones",
        "url": "https://xn3pg24ztuv6fdiqon8qn3.streamlit.app/",
        "icon": "🧠"
    },
    {
        "title": "Conversión de voz a texto",
        "description": "Aplicación que usa la conversión de voz a texto con alta precisión",
        "url": "https://traductor-ab0sp9f6fi.streamlit.app/",
        "icon": "🎤"
    },
    {
        "title": "Análisis de Datos",
        "description": "Veremos como se pueden analizar datos usando agentes inteligentes",
        "url": "https://asistpy-csv.streamlit.app/",
        "icon": "📊"
    },
    {
        "title": "Transcriptor Audio y Video",
        "description": "Realizamos transcripciones precisas de audio y video automáticamente",
        "url": "https://transcript-whisper.streamlit.app/",
        "icon": "🎵"
    },
    {
        "title": "Generación en Contexto",
        "description": "Aplicación que usa RAG a partir de documentos PDF para respuestas contextuales",
        "url": "https://chatpdf-cc.streamlit.app/",
        "icon": "📄"
    },
    {
        "title": "Análisis de Imagen",
        "description": "Capacidad de análisis avanzado en Imágenes con modelos de última generación",
        "url": "https://vision2-gpt4o.streamlit.app/",
        "icon": "🖼️"
    },
    {
        "title": "Sistema Ciberfísico",
        "description": "Capacidad de interacción con el mundo físico mediante sensores y actuadores",
        "url": "https://vision2-gpt4o.streamlit.app/",
        "icon": "🌐"
    },
    {
        "title": "Chatbot Inteligente",
        "description": "Asistente virtual con capacidades avanzadas de conversación natural",
        "url": "#",
        "icon": "🤖"
    },
    {
        "title": "Reconocimiento Facial",
        "description": "Sistema de identificación biométrica mediante análisis facial",
        "url": "#",
        "icon": "😊"
    },
    {
        "title": "Generación de Imágenes",
        "description": "Creación de imágenes artísticas y realistas con inteligencia artificial",
        "url": "#",
        "icon": "🎨"
    },
    {
        "title": "Análisis de Sentimientos",
        "description": "Análisis emocional en texto para entender opiniones y emociones",
        "url": "#",
        "icon": "💖"
    },
    {
        "title": "Traducción Automática",
        "description": "Traducción en tiempo real entre múltiples idiomas con alta precisión",
        "url": "#",
        "icon": "🌍"
    },
    {
        "title": "Sistema de Recomendaciones",
        "description": "Recomendación personalizada basada en preferencias y comportamiento",
        "url": "#",
        "icon": "⭐"
    },
    {
        "title": "Detección de Anomalías",
        "description": "Identificación de patrones inusuales y comportamientos sospechosos",
        "url": "#",
        "icon": "🚨"
    },
    {
        "title": "Procesamiento de Lenguaje",
        "description": "Comprensión del lenguaje natural para análisis textual avanzado",
        "url": "#",
        "icon": "📝"
    },
    {
        "title": "Visión por Computadora",
        "description": "Análisis avanzado de imágenes y video para múltiples aplicaciones",
        "url": "#",
        "icon": "👁️"
    },
    {
        "title": "Automación de Procesos",
        "description": "Automatización inteligente de tareas repetitivas y procesos",
        "url": "#",
        "icon": "⚙️"
    },
    {
        "title": "Predicción de Series",
        "description": "Análisis predictivo avanzado para forecasting y tendencias",
        "url": "#",
        "icon": "📈"
    }
]

# Mostrar aplicaciones en 4 columnas para mejor distribución
st.markdown("## 🎯 Aplicaciones Disponibles")
st.markdown("---")

cols = st.columns(4)

for i, app in enumerate(apps):
    with cols[i % 4]:
        # Usar el icono como fallback si Lottie no carga
        lottie_url = lottie_animations[i]["url"]
        
        st.markdown(f"""
        <div class='card'>
            <div class='card-content'>
                <div class='card-icon'>
                    <div style='font-size: 48px; color: #9370db;'>{app['icon']}</div>
                </div>
                <div class='card-title'>{app['title']}</div>
                <div class='card-description'>{app['description']}</div>
                <a href='{app['url']}' class='link-button' target='_blank'>Acceder a la App</a>
            </div>
        </div>
        """, unsafe_allow_html=True)

# Footer
st.markdown("---")
st.markdown("""
<div style='text-align: center; color: #9370db; padding: 20px;'>
    <p style='margin: 0; font-size: 14px;'>✨ Desarrollado con Streamlit y IA | Todas las cards tienen el mismo tamaño ✨</p>
</div>
""", unsafe_allow_html=True)

# JavaScript para cargar Lottie animations (comentado ya que Streamlit tiene limitaciones)
st.markdown("""
<script src="https://unpkg.com/@lottiefiles/lottie-player@latest/dist/lottie-player.js"></script>
<script>
// Las animaciones Lottie se cargarían aquí en un entorno web tradicional
console.log('Lottie animations ready to load');
</script>
""", unsafe_allow_html=True)
