import streamlit as st
import requests
import json
import base64
import os
from streamlit_lottie import st_lottie

# ⚙️ Configuración básica
st.set_page_config(page_title="Curriculum Laura", layout="wide")

# Obtener imagen en base64 desde ruta absoluta
def get_base64_image(relative_path):
    full_path = os.path.join(os.path.dirname(__file__), relative_path)
    with open(full_path, "rb") as img_file:
        return base64.b64encode(img_file.read()).decode()

# Fondo como imagen base64
img_base64 = get_base64_image("assets/animaciones/img_Fazul.png")

# Inyectar CSS
st.markdown(
    f"""
    <style>
    html, body, .stApp {{
        height: 100%;
        margin: 0;
        padding: 0;
        background-image: url("data:image/png;base64,{img_base64}");
        background-size: cover;
        background-position: center;
        background-repeat: no-repeat;
        background-attachment: fixed;
    }}
    .stApp {{
        background-color: rgba(0, 0, 0, 0.85);
        color: white;
    }}
    .block-container {{
        background-color: rgba(0, 0, 0, 0.6);
        padding: 2rem;
        border-radius: 10px;
    }}
    </style>
    """,
    unsafe_allow_html=True
)

# --- CONTENIDO ---
st.title("📄 Curriculum Vitae")
st.markdown("---")

# Función para cargar animaciones desde URL o archivo
def load_lottieurl(url):
    r = requests.get(url)
    return r.json() if r.status_code == 200 else None

# Cargar animación de presentación
with open("assets/animaciones/Ordenador.json", "r") as f:
    lottie_about = json.load(f)

# 👤 Foto y nombre
col1, col2 = st.columns([1, 3])
with col1:
    st.image("assets/my.jpg", width=150)
with col2:
    st.subheader("👩‍💻 Laura Ordoñez")
    st.write("Estudiante de Desarrollo de Aplicaciones Multiplataforma (DAM). Amante de la tecnología, en constante aprendizaje.")

st.markdown("---")

# Menú de navegación
if "pagina" not in st.session_state:
    st.session_state.pagina = "inicio"

menu1, menu2, menu3, menu4 = st.columns(4)
with menu1:
    if st.button("🏠 Inicio"):
        st.session_state.pagina = "inicio"
with menu2:
    if st.button("💼 Experiencia"):
        st.session_state.pagina = "experiencia"
with menu3:
    if st.button("🧠 Sobre mí"):
        st.session_state.pagina = "sobremi"
with menu4:
    if st.button("⚙️ Habilidades Técnicas"):
        st.session_state.pagina = "habilidades"

# --- Páginas ---
if st.session_state.pagina == "inicio":
    st.subheader("📬 Contacto")
    st.markdown("""
    - 📧 **Email:** laura93o@hotmail.com  
    - 💼 **LinkedIn:** [linkedin.com/in/laura](https://www.linkedin.com/in/laura-ordo%C3%B1ez-737532300/)  
    - 🐙 **GitHub:** [github.com/lauraordo93](https://github.com/lauraordo93)
    """)

elif st.session_state.pagina == "experiencia":
    st.subheader("💼 Experiencia")
    st.markdown("""
    🗓️ **2024/2025 - Actualidad**  
    **Estudiante DAM**  
    - Desarrollo de aplicaciones con **Java**  
    - Bases de datos con **SQL**  
    - Programación orientada a objetos  
    - Interfaces gráficas con **Python**

    🗓️ **2025 - Proyecto personal**  
    **Portal web en desarrollo**  
    - Creación de un portal vertical como proyecto intermodular  
    - Tecnologías: HTML, CSS, JavaScript, PHP, SQL  
    - Tema: Saxofonista (estructura dinámica con base de datos incluida)
    """)

elif st.session_state.pagina == "sobremi":
    st.subheader("🧠 Sobre mí")
    col1, col2 = st.columns([2, 3])
    with col1:
        st_lottie(lottie_about, height=200, key="about")
    with col2:
        st.write("""
        Soy Laura Ordoñez, estudiante del Grado Superior en Desarrollo de Aplicaciones Multiplataforma (DAM).  
        Me apasiona el mundo de la tecnología y siempre estoy buscando aprender cosas nuevas.  
        Tengo una actitud proactiva, me gusta trabajar en equipo y enfrentar nuevos retos que me permitan seguir creciendo profesionalmente.  
        Actualmente tengo conocimientos en Java, SQL, Python, HTML y estoy desarrollando proyectos personales para reforzar lo aprendido.
        """)

elif st.session_state.pagina == "habilidades":
    st.subheader("⚙️ Habilidades Técnicas")

    with open("assets/animaciones/python.json", "r") as f:
        lottie_python = json.load(f)
    with open("assets/animaciones/java.json", "r") as f:
        lottie_java = json.load(f)
    with open("assets/animaciones/html.json", "r") as f:
        lottie_html = json.load(f)
    with open("assets/animaciones/sql.json", "r") as f:
        lottie_sql = json.load(f)

    col1, col2 = st.columns(2)
    with col1:
        st_lottie(lottie_python, height=100, key="python")
        st.write("**Python**")
        st.progress(50)

        st_lottie(lottie_html, height=100, key="html")
        st.write("**HTML / CSS**")
        st.progress(55)

    with col2:
        st_lottie(lottie_java, height=100, key="java")
        st.write("**Java**")
        st.progress(75)

        st_lottie(lottie_sql, height=100, key="sql")
        st.write("**SQL**")
        st.progress(70)
