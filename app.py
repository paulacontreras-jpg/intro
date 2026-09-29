import streamlit as st
from PIL import Image

# --------------------------------------------------
# CONFIGURACIÓN
# --------------------------------------------------

st.set_page_config(
    page_title="Mi Mood de Hoy",
    page_icon="💗",
    layout="wide"
)


# --------------------------------------------------
# ESTILOS
# --------------------------------------------------

st.markdown("""
<style>

    /* FONDO GENERAL */
    .stApp {
        background: #FFF5F7;
    }

    /* BARRA LATERAL */
    [data-testid="stSidebar"] {
        background: linear-gradient(180deg, #8E244D 0%, #C94F76 100%);
    }

    [data-testid="stSidebar"] h1,
    [data-testid="stSidebar"] h2,
    [data-testid="stSidebar"] h3,
    [data-testid="stSidebar"] p {
        color: white;
    }


    /* ENCABEZADO */
    .titulo {
        background: linear-gradient(135deg, #A8325B, #E66A8D);
        color: white;
        padding: 35px;
        border-radius: 25px;
        text-align: center;
        margin-bottom: 25px;
        box-shadow: 0px 8px 20px rgba(168, 50, 91, 0.20);
    }

    .titulo h1 {
        font-size: 45px;
        margin-bottom: 8px;
    }

    .titulo p {
        font-size: 18px;
        margin: 0;
    }


    /* TARJETA DEL MOOD */
    .mood-card {
        background: white;
        padding: 25px;
        border-radius: 22px;
        border: 2px solid #F4C4D3;
        box-shadow: 0px 5px 18px rgba(160, 50, 90, 0.12);
        margin-bottom: 25px;
    }

    .mood-card h2 {
        color: #A8325B;
    }

    .mood-card p {
        color: #555555;
        font-size: 16px;
    }


    /* CAJAS DE COLUMNAS */
    .column-card {
        background: #FFE4EC;
        padding: 25px;
        border-radius: 20px;
        min-height: 200px;
        border: 2px solid #F5B5C7;
        box-shadow: 0px 4px 15px rgba(160, 50, 90, 0.10);
    }

    .column-card h3 {
        color: #8E244D;
    }

    .column-card p {
        color: #5B3944;
    }


    /* SEPARADORES */
    .decoracion {
        text-align: center;
        color: #D94F78;
        font-size: 25px;
        margin: 15px;
    }


    /* BOTÓN */
    .stButton > button {
        background: #A8325B;
        color: white;
        border: none;
        border-radius: 12px;
        padding: 10px 25px;
        font-weight: bold;
        font-size: 16px;
    }

    .stButton > button:hover {
        background: #E66A8D;
        color: white;
    }


    /* PIE DE PÁGINA */
    .footer {
        text-align: center;
        color: #A8325B;
        margin-top: 35px;
        padding: 20px;
        font-size: 14px;
    }

</style>
""", unsafe_allow_html=True)


# --------------------------------------------------
# BARRA LATERAL
# --------------------------------------------------

with st.sidebar:

    st.markdown("## 💗 Mi Mood")

    st.markdown("---")

    st.write(
        "Un pequeño espacio para escribir cómo me siento, "
        "compartir mi mood y hablar de las cosas que me ayudan."
    )

    st.markdown("---")

    st.markdown("### 🌸 Mood del día")

    st.write("💗 Escribe cómo te sientes")
    st.write("🐱 Habla de tus gatos")
    st.write("✨ Descubre si somos twins")


# --------------------------------------------------
# ENCABEZADO
# --------------------------------------------------

st.markdown("""
<div class="titulo">

<h1>💗 Mi Mood de Hoy 💗</h1>

<p>
Un pequeño espacio para compartir cómo me siento
</p>

</div>
""", unsafe_allow_html=True)


st.markdown(
    "<div class='decoracion'>♡ ✿ ♡ ✿ ♡</div>",
    unsafe_allow_html=True
)


# --------------------------------------------------
# MOOD
# --------------------------------------------------

st.markdown("""
<div class="mood-card">

<h2>🌷 ¿Cómo me siento hoy?</h2>

<p>
Este espacio es para escribir mi mood del día,
compartir cómo me siento y dejarlo por aquí.
</p>

</div>
""", unsafe_allow_html=True)


# --------------------------------------------------
# IMAGEN
# --------------------------------------------------

col_img1, col_img2, col_img3 = st.columns([1, 2, 1])

with col_img2:

    image = Image.open("healing.jfif")

    st.image(
        image,
        caption="🌸 Mi mood de hoy 🌸",
        width=400
    )


# --------------------------------------------------
# TEXTO DEL MOOD
# --------------------------------------------------

texto = st.text_input(
    "💭 Escribe tu mood",
    "Este es tu mood"
)

st.write("💗 Tu mood es:", texto)


st.markdown(
    "<div class='decoracion'>♡ ───── ♡ ───── ♡</div>",
    unsafe_allow_html=True
)


# --------------------------------------------------
# COLUMNAS
# --------------------------------------------------

st.subheader("🌸 Compartamos el mood")

col1, col2 = st.columns(2)


# --------------------------------------------------
# COLUMNA 1
# --------------------------------------------------

with col1:

    st.markdown("""
    <div class="column-card">

    <h3>💗 ¿Tenemos el mismo mood?</h3>

    <p>
    Todos los días me siento con el mismo mood.
    ¿A ti también te pasa?
    </p>

    </div>
    """, unsafe_allow_html=True)

    resp = st.checkbox("Me pasa igual 💕")

    if resp:
        st.success("TWINS 💗")


# --------------------------------------------------
# COLUMNA 2
# --------------------------------------------------

with col2:

    st.markdown("""
    <div class="column-card">

    <h3>🐱 ¿Los gatos ayudan?</h3>

    <p>
    ¿Crees que los gatos pueden ayudarte
    a manejar tu mood?
    </p>

    </div>
    """, unsafe_allow_html=True)

    modo = st.checkbox("Sí, los gatos ayudan 🐱")

    if modo:
        st.success("TWINS X2 🐱💗")

    else:
        st.write("🐾 Lastima...")


# --------------------------------------------------
# BOTÓN
# --------------------------------------------------

st.markdown(
    "<div class='decoracion'>♡ ✿ ♡ ✿ ♡</div>",
    unsafe_allow_html=True
)

st.subheader("💌 Un último mensaje")


if st.button("💗 Presiona el botón"):

    st.success("Gracias por presionarlo 💕")

else:

    st.write("Presiónalo pues 😭💗")


# --------------------------------------------------
# FOOTER
# --------------------------------------------------

st.markdown("""
<div class="footer">

<div class="decoracion">♡ 🐱 ♡ 🌸 ♡</div>

<b>Mi mood, mis sentimientos y mis gatos.</b>

<br>

Porque aparentemente los gatos son terapeutas sin licencia.

</div>
""", unsafe_allow_html=True)
