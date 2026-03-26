import streamlit as st

st.set_page_config(
    page_title="Portafolio | Karen Hernández",
    page_icon="🎨",
    layout="wide"
)

st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=DM+Serif+Display:ital@0;1&family=DM+Sans:wght@300;400;500&display=swap');

    *, *::before, *::after { box-sizing: border-box; margin: 0; padding: 0; }

    html, body, .stApp {
        background-color: #0e0e0e !important;
        color: #f0ede6;
        font-family: 'DM Sans', sans-serif;
    }

    /* Hide streamlit chrome */
    #MainMenu, footer, header { visibility: hidden; }
    .block-container { padding: 0 !important; max-width: 100% !important; }
    section[data-testid="stSidebar"] { display: none; }

    /* ─── HERO ─── */
    .hero {
        min-height: 100vh;
        display: flex;
        flex-direction: column;
        justify-content: center;
        align-items: flex-start;
        padding: 80px 10vw;
        position: relative;
        overflow: hidden;
        background: #0e0e0e;
    }
    .hero::before {
        content: '';
        position: absolute;
        top: -200px; right: -200px;
        width: 700px; height: 700px;
        background: radial-gradient(circle, rgba(232,196,104,0.12) 0%, transparent 70%);
        pointer-events: none;
    }
    .hero::after {
        content: '';
        position: absolute;
        bottom: -100px; left: -100px;
        width: 500px; height: 500px;
        background: radial-gradient(circle, rgba(232,196,104,0.06) 0%, transparent 70%);
        pointer-events: none;
    }
    .hero-tag {
        font-family: 'DM Sans', sans-serif;
        font-size: 12px;
        font-weight: 500;
        letter-spacing: 4px;
        text-transform: uppercase;
        color: #e8c468;
        margin-bottom: 24px;
        opacity: 0;
        animation: fadeUp 0.6s ease forwards;
    }
    .hero-name {
        font-family: 'DM Serif Display', serif;
        font-size: clamp(52px, 8vw, 110px);
        line-height: 1.0;
        color: #f0ede6;
        margin-bottom: 16px;
        opacity: 0;
        animation: fadeUp 0.6s ease 0.15s forwards;
    }
    .hero-name em {
        font-style: italic;
        color: #e8c468;
    }
    .hero-sub {
        font-size: clamp(16px, 2vw, 22px);
        color: rgba(240,237,230,0.55);
        font-weight: 300;
        max-width: 520px;
        line-height: 1.6;
        margin-bottom: 48px;
        opacity: 0;
        animation: fadeUp 0.6s ease 0.3s forwards;
    }
    .hero-divider {
        width: 60px; height: 2px;
        background: #e8c468;
        margin-bottom: 48px;
        opacity: 0;
        animation: fadeUp 0.6s ease 0.45s forwards;
    }
    .hero-meta {
        display: flex;
        gap: 40px;
        flex-wrap: wrap;
        opacity: 0;
        animation: fadeUp 0.6s ease 0.6s forwards;
    }
    .hero-meta-item {
        display: flex;
        flex-direction: column;
        gap: 4px;
    }
    .hero-meta-label {
        font-size: 11px;
        letter-spacing: 3px;
        text-transform: uppercase;
        color: rgba(240,237,230,0.35);
    }
    .hero-meta-value {
        font-size: 15px;
        color: #f0ede6;
        font-weight: 400;
    }
    @keyframes fadeUp {
        from { opacity: 0; transform: translateY(20px); }
        to   { opacity: 1; transform: translateY(0); }
    }

    /* ─── SECTION WRAPPER ─── */
    .section {
        padding: 100px 10vw;
        position: relative;
    }
    .section-label {
        font-size: 11px;
        letter-spacing: 4px;
        text-transform: uppercase;
        color: #e8c468;
        margin-bottom: 16px;
        display: flex;
        align-items: center;
        gap: 12px;
    }
    .section-label::after {
        content: '';
        flex: 1;
        height: 1px;
        background: rgba(232,196,104,0.2);
        max-width: 80px;
    }
    .section-title {
        font-family: 'DM Serif Display', serif;
        font-size: clamp(32px, 4vw, 52px);
        color: #f0ede6;
        margin-bottom: 60px;
        line-height: 1.1;
    }
    .section-title em {
        font-style: italic;
        color: #e8c468;
    }

    /* ─── PROJECT GRID ─── */
    .projects-grid {
        display: grid;
        grid-template-columns: repeat(auto-fill, minmax(300px, 1fr));
        gap: 2px;
    }
    .proj-card {
        background: #161616;
        padding: 36px 32px;
        border: 1px solid rgba(240,237,230,0.06);
        transition: all 0.35s cubic-bezier(0.25, 0.46, 0.45, 0.94);
        position: relative;
        overflow: visible;
        display: flex;
        flex-direction: column;
        gap: 16px;
    }
    .proj-card::before {
        content: '';
        position: absolute;
        inset: 0;
        background: linear-gradient(135deg, rgba(232,196,104,0.04) 0%, transparent 60%);
        opacity: 0;
        transition: opacity 0.35s ease;
    }
    .proj-card:hover {
        background: #1a1a1a;
        border-color: rgba(232,196,104,0.25);
        transform: translateY(-4px);
    }
    .proj-card:hover::before { opacity: 1; }
    .proj-platform {
        font-size: 10px;
        letter-spacing: 3px;
        text-transform: uppercase;
        color: #e8c468;
        font-weight: 500;
    }
    .proj-num {
        position: absolute;
        top: 28px; right: 32px;
        font-family: 'DM Serif Display', serif;
        font-size: 42px;
        color: rgba(240,237,230,0.04);
        line-height: 1;
        pointer-events: none;
    }
    .proj-icon {
        font-size: 32px;
        line-height: 1;
    }
    .proj-title {
        font-family: 'DM Serif Display', serif;
        font-size: 22px;
        color: #f0ede6;
        line-height: 1.2;
    }
    .proj-desc {
        font-size: 14px;
        color: rgba(240,237,230,0.5);
        line-height: 1.6;
        font-weight: 300;
        flex-grow: 1;
    }
    .proj-links {
        display: flex;
        flex-wrap: wrap;
        gap: 8px;
        margin-top: 8px;
    }
    .proj-link {
        font-size: 12px;
        letter-spacing: 1px;
        color: #e8c468 !important;
        text-decoration: none !important;
        border: 1px solid rgba(232,196,104,0.3);
        padding: 7px 16px;
        border-radius: 2px;
        transition: all 0.2s ease;
        font-weight: 500;
        text-transform: uppercase;
        cursor: pointer;
        pointer-events: auto !important;
        position: relative;
        z-index: 10;
    }
    .proj-link:hover {
        background: #e8c468 !important;
        color: #0e0e0e !important;
        border-color: #e8c468;
        text-decoration: none !important;
    }
    .proj-link.secondary {
        color: rgba(240,237,230,0.4) !important;
        border-color: rgba(240,237,230,0.12);
    }
    .proj-link.secondary:hover {
        background: rgba(240,237,230,0.08) !important;
        color: #f0ede6 !important;
        border-color: rgba(240,237,230,0.3);
    }

    /* ─── PLATFORM LEGEND ─── */
    .legend {
        display: flex;
        gap: 24px;
        flex-wrap: wrap;
        margin-bottom: 48px;
    }
    .legend-item {
        display: flex;
        align-items: center;
        gap: 8px;
        font-size: 12px;
        color: rgba(240,237,230,0.45);
        letter-spacing: 1px;
        text-transform: uppercase;
    }
    .legend-dot {
        width: 6px; height: 6px;
        border-radius: 50%;
        background: #e8c468;
        opacity: 0.6;
    }

    /* ─── FOOTER ─── */
    .footer {
        padding: 60px 10vw;
        border-top: 1px solid rgba(240,237,230,0.06);
        display: flex;
        justify-content: space-between;
        align-items: center;
        flex-wrap: wrap;
        gap: 16px;
    }
    .footer-name {
        font-family: 'DM Serif Display', serif;
        font-size: 24px;
        color: rgba(240,237,230,0.3);
    }
    .footer-copy {
        font-size: 12px;
        color: rgba(240,237,230,0.2);
        letter-spacing: 2px;
    }
</style>
""", unsafe_allow_html=True)

# ─── HERO ───
st.markdown("""
<div class="hero">
    <div class="hero-tag">Bitácora de curso</div>
    <div class="hero-name">Karen<br><em>Hernández</em></div>
    <div class="hero-sub">
        Diseño Interactivo · Universidad EAFIT<br>
        Interfaces Multimodales
    </div>
    <div class="hero-divider"></div>
    <div class="hero-meta">
        <div class="hero-meta-item">
            <span class="hero-meta-label">Programa</span>
            <span class="hero-meta-value">Diseño Interactivo</span>
        </div>
        <div class="hero-meta-item">
            <span class="hero-meta-label">Universidad</span>
            <span class="hero-meta-value">EAFIT</span>
        </div>
        <div class="hero-meta-item">
            <span class="hero-meta-label">Curso</span>
            <span class="hero-meta-value">Interfaces Multimodales</span>
        </div>
        <div class="hero-meta-item">
            <span class="hero-meta-label">Proyectos</span>
            <span class="hero-meta-value">15</span>
        </div>
    </div>
</div>
""", unsafe_allow_html=True)

# ─── PROJECTS ───
projects = [
    {
        "platform": "TinkerCad",
        "icon": "🔴",
        "title": "Semáforo Arduino",
        "desc": "Introducción a microcontroladores. Simulación de un semáforo funcional con Arduino.",
        "links": [("Ver proyecto", "https://www.tinkercad.com/things/7xz9SUpM7HK-brave-amur-hillar", "primary")]
    },
    {
        "platform": "Streamlit",
        "icon": "✨",
        "title": "Introducción",
        "desc": "Introducción a aplicaciones en línea y creación de interfaces multimodales.",
        "links": [("Abrir app", "https://introduccion-mnosckb64kzz9xkujt5k2j.streamlit.app/", "primary")]
    },
    {
        "platform": "Wokwi + Processing",
        "icon": "🌡️",
        "title": "Sistema de Clima",
        "desc": "Interfaz gráfica con ESP32, sensor de temperatura y humedad. Visualización en Processing.",
        "links": [
            ("Wokwi ESP32", "https://wokwi.com/projects/458889210606244865", "primary"),
            ("Código Processing", "https://drive.google.com/file/d/1HVQ5nSc9Mu2CY4MHf1dqi6spUkX27QOf/view?usp=drive_link", "secondary"),
            ("Ver video", "https://drive.google.com/file/d/1G15lzwiVktrhzx3gj1_5XHoCw_hYODje/view?usp=drive_link", "secondary"),
        ]
    },
    {
        "platform": "Streamlit",
        "icon": "🎤",
        "title": "Texto a Audio",
        "desc": "Ingresa un texto para convertirlo a audio y escucharlo en el navegador.",
        "links": [("Abrir app", "https://ejemplovozatexto-5bub8n89en8ueyr573ug9u.streamlit.app/", "primary")]
    },
    {
        "platform": "Streamlit",
        "icon": "🌍",
        "title": "Traductor",
        "desc": "Ingresa un texto y selecciona un lenguaje de salida para traducirlo al instante.",
        "links": [("Abrir app", "https://traductor-esuz2vm4xss2y3jwyatxmd.streamlit.app/", "primary")]
    },
    {
        "platform": "Streamlit",
        "icon": "🔍",
        "title": "OCR — Reconocimiento de Caracteres",
        "desc": "Digitaliza y reconoce automáticamente caracteres impresos o escritos a mano.",
        "links": [("Abrir app", "https://dchzzx86aqvhtv5qmqyl28.streamlit.app/", "primary")]
    },
    {
        "platform": "Streamlit",
        "icon": "🤖",
        "title": "OCR + Traductor + Audio",
        "desc": "Combinación de reconocimiento óptico, traducción y síntesis de voz en una sola app.",
        "links": [("Abrir app", "https://ocr-audio-npul52t44wtcgfbznej3xe.streamlit.app/", "primary")]
    },
    {
        "platform": "Streamlit",
        "icon": "☁️",
        "title": "Wordcloud",
        "desc": "Genera nubes de palabras a partir de cualquier texto ingresado.",
        "links": [("Abrir app", "https://wordcloud-hqvubvcvvc2jnqum9egjnm.streamlit.app/", "primary")]
    },
    {
        "platform": "Streamlit",
        "icon": "💖",
        "title": "Análisis de Sentimientos",
        "desc": "Analiza el tono emocional de un texto e identifica sentimientos positivos, negativos o neutros.",
        "links": [("Abrir app", "https://sentimenta-3we8zkzs8bksrvsmvywxzk.streamlit.app/", "primary")]
    },
    {
        "platform": "Streamlit",
        "icon": "📝",
        "title": "TextBlob — Análisis de Texto",
        "desc": "Herramienta de análisis de texto con la biblioteca TextBlob para NLP.",
        "links": [("Abrir app", "https://textotextblob24511asfdgaliudsbvliu3w4y78efr.streamlit.app/", "primary")]
    },
    {
        "platform": "Streamlit",
        "icon": "📊",
        "title": "TF-IDF en Inglés",
        "desc": "Preguntas y respuestas sobre documentos usando análisis TF-IDF en inglés.",
        "links": [("Abrir app", "https://wmqqht2uiqskeuwyama88g.streamlit.app/", "primary")]
    },
    {
        "platform": "Streamlit",
        "icon": "📊",
        "title": "TF-IDF en Español",
        "desc": "Preguntas y respuestas sobre documentos usando análisis TF-IDF en español.",
        "links": [("Abrir app", "https://tdfespanol-3x9cmmpeuafzn9unzksxfd.streamlit.app/", "primary")]
    },
    {
        "platform": "Streamlit",
        "icon": "👁️",
        "title": "Detección de Objetos YOLOv5",
        "desc": "Detección de objetos en tiempo real usando el modelo de visión por computadora YOLOv5.",
        "links": [("Abrir app", "https://deteccionobjetosyolo-mzheyr5dcpubxhgvjh3mmi.streamlit.app/", "primary")]
    },
    {
        "platform": "Streamlit",
        "icon": "🖐️",
        "title": "Detección de Gestos",
        "desc": "Reconocimiento de gestos con las manos en tiempo real mediante visión artificial.",
        "links": [("Abrir app", "https://detecciongestos-4y9rmt8daniuvt3c9wqp84.streamlit.app/", "primary")]
    },
]

st.markdown("""
<div class="section">
    <div class="section-label">Trabajos</div>
    <div class="section-title">Proyectos <em>desarrollados</em></div>
    <div class="legend">
        <div class="legend-item"><div class="legend-dot"></div>TinkerCad</div>
        <div class="legend-item"><div class="legend-dot"></div>Streamlit</div>
        <div class="legend-item"><div class="legend-dot"></div>Wokwi</div>
        <div class="legend-item"><div class="legend-dot"></div>Processing</div>
    </div>
</div>
""", unsafe_allow_html=True)

# Style native st.link_button to match dark design
st.markdown("""
<style>
    [data-testid="stLinkButton"] > a {
        background: transparent !important;
        color: #e8c468 !important;
        border: 1px solid rgba(232,196,104,0.35) !important;
        border-radius: 2px !important;
        font-size: 11px !important;
        letter-spacing: 1.5px !important;
        text-transform: uppercase !important;
        font-family: 'DM Sans', sans-serif !important;
        font-weight: 500 !important;
        transition: all 0.2s ease !important;
    }
    [data-testid="stLinkButton"] > a:hover {
        background: #e8c468 !important;
        color: #0e0e0e !important;
        border-color: #e8c468 !important;
    }
    [data-testid="stLinkButton"] > a p {
        color: inherit !important;
    }
</style>
""", unsafe_allow_html=True)

cols_per_row = 3
rows = [projects[i:i+cols_per_row] for i in range(0, len(projects), cols_per_row)]

for row_idx, row in enumerate(rows):
    cols = st.columns(len(row))
    for col, p in zip(cols, row):
        i = projects.index(p)
        with col:
            st.markdown(f"""
            <div class="proj-card">
                <span class="proj-num">{str(i+1).zfill(2)}</span>
                <div class="proj-platform">{p['platform']}</div>
                <div class="proj-icon">{p['icon']}</div>
                <div class="proj-title">{p['title']}</div>
                <div class="proj-desc">{p['desc']}</div>
            </div>
            """, unsafe_allow_html=True)
            for label, url, _ in p["links"]:
                st.link_button(label, url, use_container_width=True)

# ─── FOOTER ───
st.markdown("""
<div class="footer">
    <div class="footer-name">Karen Hernández</div>
    <div class="footer-copy">Diseño Interactivo · EAFIT · Interfaces Multimodales</div>
</div>
""", unsafe_allow_html=True)
