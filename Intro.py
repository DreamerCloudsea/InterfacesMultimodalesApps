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

# CSS personalizado para el tema de fantasía morado más oscuro
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;500;600&display=swap');
    
    * {
        font-family: 'Poppins', sans-serif;
    }
    
    .main {
        background: linear-gradient(135deg, #6a0dad 0%, #8a2be2 50%, #9370db 100%);
    }
    
    .stApp {
        background: linear-gradient(135deg, #6a0dad 0%, #8a2be2 50%, #9370db 100%);
        background-attachment: fixed;
    }
    
    .css-1d391kg, .css-1lcbmhc {
        background-color: rgba(255, 255, 255, 0.95) !important;
        backdrop-filter: blur(10px);
        border-radius: 15px;
        border: 1px solid #b19cd9;
        padding: 20px;
        margin: 10px 0;
        box-shadow: 0 4px 20px rgba(106, 13, 173, 0.2);
    }
    
    .stTitle {
        color: #ffffff !important;
        text-align: center;
        font-weight: 600;
        text-shadow: 2px 2px 8px rgba(106, 13, 173, 0.5);
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
        background: linear-gradient(180deg, #6a0dad 0%, #4b0082 100%) !important;
        color: white;
    }
    
    .card {
        background: rgba(255, 255, 255, 0.98);
        border-radius: 15px;
        padding: 20px;
        margin: 10px 0;
        border: 1px solid #e6e6fa;
        box-shadow: 0 6px 20px rgba(106, 13, 173, 0.15);
        transition: all 0.3s ease;
        height: 320px;
        display: flex;
        flex-direction: column;
        justify-content: space-between;
    }
    
    .card:hover {
        transform: translateY(-8px);
        box-shadow: 0 12px 30px rgba(106, 13, 173, 0.25);
        border: 1px solid #9370db;
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
        color: #6a0dad;
        font-size: 16px;
        font-weight: 600;
        margin-bottom: 10px;
        min-height: 40px;
        display: flex;
        align-items: center;
        text-align: center;
        justify-content: center;
    }
    
    .card-description {
        color: #555;
        font-size: 13px;
        line-height: 1.4;
        flex-grow: 1;
        margin-bottom: 15px;
        text-align: center;
    }
    
    .link-button {
        background: linear-gradient(45deg, #8a2be2, #6a0dad);
        color: white !important;
        padding: 10px 20px;
        border-radius: 25px;
        text-decoration: none;
        display: inline-block;
        text-align: center;
        font-size: 14px;
        font-weight: 500;
        transition: all 0.3s ease;
        border: none;
        cursor: pointer;
        width: 100%;
        box-shadow: 0 4px 15px rgba(138, 43, 226, 0.3);
    }
    
    .link-button:hover {
        transform: scale(1.05);
        box-shadow: 0 6px 20px rgba(138, 43, 226, 0.4);
        background: linear-gradient(45deg, #6a0dad, #8a2be2);
        color: white;
        text-decoration: none;
    }
    
    .header-banner {
        background: linear-gradient(45deg, #6a0dad, #8a2be2);
        padding: 25px;
        border-radius: 15px;
        text-align: center;
        margin: 20px 0;
        box-shadow: 0 8px 25px rgba(106, 13, 173, 0.3);
        border: 1px solid #b19cd9;
    }
    
    .footer {
        text-align: center;
        color: #ffffff;
        padding: 20px;
        font-size: 14px;
        text-shadow: 1px 1px 3px rgba(0, 0, 0, 0.3);
    }
    
    .section-title {
        color: #ffffff;
        text-align: center;
        font-size: 28px;
        font-weight: 600;
        margin: 30px 0;
        text-shadow: 2px 2px 8px rgba(106, 13, 173, 0.5);
    }
</style>
""", unsafe_allow_html=True)

# Sidebar mejorado
with st.sidebar:
    st.markdown("""
    <div style='text-align: center; padding: 20px 0;'>
        <h2 style='color: white; margin-bottom: 20px; text-shadow: 1px 1px 3px rgba(0,0,0,0.3);'>🧠 Portal IA</h2>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("---")
    
    parrafo = (
        "La inteligencia artificial permite mejorar la toma de decisiones con el uso de datos, "
        "automatizar tareas rutinarias y proporcionar análisis avanzados en tiempo real, lo que "
        "resulta en una mayor eficiencia y precisión en diversos campos."
    )
    
    st.markdown(f"""
    <div style='background: rgba(255,255,255,0.15); padding: 15px; border-radius: 10px; margin: 10px 0; border: 1px solid rgba(255,255,255,0.2);'>
        <p style='color: white; font-size: 14px; line-height: 1.5; text-shadow: 1px 1px 2px rgba(0,0,0,0.3);'>{parrafo}</p>
    </div>
    """, unsafe_allow_html=True)

# Título principal
st.title("✨ Aplicaciones de Inteligencia Artificial")

# Lista de aplicaciones con 20 slots
apps = [
    {
        "title": "Intro modificada",
        "description": "Genera mensajitos de acuerdo al estado de ánimo",
        "url": "https://sldz8n54exqwjrjywlsjsb.streamlit.app/",
        "icon": "😊"
    },
    {
        "title": "Analizador de Sentimientos",
        "description": "Describe cómo te sientes y descubre qué tan malo es",
        "url": "https://7dc7lkisw7zk2vlx5mypgm.streamlit.app/",
        "icon": "💖"
    },
    {
        "title": "Reconocimiento de Caracteres",
        "description": "Toma una foto y mira si detecta el texto",
        "url": "https://characters-4aw4mgk6egebtktb8yrxbj.streamlit.app/",
        "icon": "🧠"
    },
    {
        "title": "Pdf Analyzer",
        "description": "Detecta la información que contiene un pdf",
        "url": "https://chatpdf-dulzyqnvxjn6f3j4xklfzg.streamlit.app/",
        "icon": "📄"
    },
    {
        "title": "Control con Voz",
        "description": "Controlar variables por medio de comandos de voz",
        "url": "https://ctrlvoice-6tk75bepfzqejsrcituana.streamlit.app/",
        "icon": "🎤"
    },
    {
        "title": "Detección de Bocetos",
        "description": "Dibuja algo y mira si la IA descifra qué es",
        "url": "https://drawrecog-3mbt5y5wwyextxtsnqsamh.streamlit.app/",
        "icon": "🌐"
    },
    {
        "title": "Reconococimiento de Números",
        "description": "Dibuja un número y mira si la IA lo detecta correctamente",
        "url": "https://6cj9yugoaccstbos6mr2kg.streamlit.app/",
        "icon": "📄"
    },
    {
        "title": "Dibujos Mitológicos",
        "description": "Dibuja algo y descubre cómo se asocia con la mitología",
        "url": "https://histinf-zcbmlerdrrtb8xcx2qspe5.streamlit.app/",
        "icon": "🔮"
    },
    {
        "title": "OCR Translator",
        "description": "Extrae texto de imágenes y conviértelo a audio en diferentes idioma",
        "url": "https://ocr-audio-enavkxpmvhn3bkq4yrqtzw.streamlit.app/",
        "icon": "🤖"
    },
    {
        "title": "Sensor Reader",
        "description": "Monitoreo de variables en tiempo real",
        "url": "https://recepmqtt-czec5ke5fnb8cku6qcei5j.streamlit.app/",
        "icon": "📡"
    },
    {
        "title": "Control MQTT",
        "description": "Envía valores a tus programas",
        "url": "https://sendcmqtt-tappjjpcr473nu6i9ck9eo.streamlit.app/",
        "icon": "🌡️"
    },
    {
        "title": "Analizador TF-IDF",
        "description": "Esta herramienta analiza la similitud semántica entre preguntas y documentosl",
        "url": "https://tdfesp-gw3knzfev6uuy2ypzmnfro.streamlit.app/",
        "icon": "🌍"
    },
    {
        "title": "Conversor Texto a Audio",
        "description": "Ingresa texto y conviértelo en un audio",
        "url": "https://textau-vq4d4rzu5cpx6fwxuheota.streamlit.app/",
        "icon": "🎤"
    },
    {
        "title": "TF-IDF Analysis",
        "description": "Analiza texto y te ayuda a responder preguntas respecto a este",
        "url": "https://8y5wp8m4zafle8ftocb67f.streamlit.app/",
        "icon": "⭐"
    },
    {
        "title": "Reconocimiento de Imágenes",
        "description": "Toma una foto para que el programa la analice",
        "url": "https://dxxx3fldp8od8ysl2ikxav.streamlit.app/",
        "icon": "🚨"
    },
    {
        "title": "Traductor Inteligente",
        "description": "Graba tu audio y traduce la información en varios idiomas",
        "url": "https://traductor-a2iwpgh9nuhuc9mkyldk8j.streamlit.app/",
        "icon": "📝"
    },
    {
        "title": "Mood Analyzer",
        "description": "Describe cómo te siente y mira las recomendaciones",
        "url": "https://q5qvtqddw5xqdwqnnfxizq.streamlit.app/",
        "icon": "💕"
    },
    {
        "title": "Image Analyzer",
        "description": "Sube una imagen y haz preguntas sobre esta",
        "url": "https://visionapp-npvocfvn4dgwsnqxtqqu3w.streamlit.app/",
        "icon": "👁️"
    },
    {
        "title": "Vision App",
        "description": "Detección de objetos en tiempo real",
        "url": "https://yolov5-jqm3epsmncbffdvqjnhz8s.streamlit.app/",
        "icon": "⚙️"
    },
]

# Mostrar aplicaciones en 4 columnas
st.markdown('<div class="section-title">Aplicaciones Disponibles</div>', unsafe_allow_html=True)

cols = st.columns(4)

for i, app in enumerate(apps):
    with cols[i % 4]:
        st.markdown(f"""
        <div class='card'>
            <div class='card-content'>
                <div class='card-icon'>
                    <div style='font-size: 48px; color: #6a0dad; text-shadow: 2px 2px 4px rgba(106, 13, 173, 0.2);'>{app['icon']}</div>
                </div>
                <div class='card-title'>{app['title']}</div>
                <div class='card-description'>{app['description']}</div>
                <a href='{app['url']}' class='link-button' target='_blank'>Acceder a la App</a>
            </div>
        </div>
        """, unsafe_allow_html=True)
