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
        "title": "Pdf Analizer",
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
