
import streamlit as st

st.set_page_config(
    page_title="DecoKids",
    page_icon="🎨",
    layout="centered"
)

st.title("🎨 DecoKids")
st.subheader("Decoración para escuelas infantiles")
st.write(
    "¡Diseña espacios coloridos, creativos y acogedores "
    "para los más pequeños!"
)

# Selección del ambiente
ambiente = st.selectbox(
    "¿Qué espacio deseas decorar?",
    [
        "Aula infantil",
        "Biblioteca",
        "Patio de juegos",
        "Comedor",
        "Sala de lectura"
    ]
)

# Selección del estilo
estilo = st.selectbox(
    "Elige un estilo decorativo",
    [
        "Colores pastel",
        "Naturaleza",
        "Animales",
        "Arcoíris",
        "Espacio y planetas"
    ]
)

# Presupuesto
presupuesto = st.slider(
    "Presupuesto aproximado (S/)",
    min_value=100,
    max_value=2000,
    value=500,
    step=100
)

# Botón para generar la propuesta
if st.button("✨ Crear propuesta decorativa"):
    st.success("¡Tu propuesta está lista!")

    st.markdown(f"### 🏫 {ambiente}")
    st.write(f"**Estilo elegido:** {estilo}")
    st.write(f"**Presupuesto:** S/ {presupuesto}")

    ideas = {
        "Colores pastel": [
            "Pintar las paredes en tonos suaves",
            "Agregar cojines y alfombras",
            "Decorar con figuras de nubes y estrellas"
        ],
        "Naturaleza": [
            "Usar plantas seguras para niños",
            "Crear murales de árboles y flores",
            "Incorporar materiales de madera"
        ],
        "Animales": [
            "Colocar murales de animales",
            "Crear figuras de cartulina",
            "Usar cojines con formas de animales"
        ],
        "Arcoíris": [
            "Decorar una pared con un arcoíris",
            "Utilizar cajas organizadoras de colores",
            "Agregar dibujos infantiles"
        ],
        "Espacio y planetas": [
            "Crear planetas colgantes",
            "Decorar con estrellas y cohetes",
            "Pintar un mural del sistema solar"
        ]
    }

    st.markdown("### 💡 Ideas de decoración")

    for idea in ideas[estilo]:
        st.write(f"✅ {idea}")

    st.info(
        "Consejo: utiliza materiales no tóxicos, "
        "fáciles de limpiar y seguros para los niños."
    )

st.divider()
st.caption("DecoKids | Creamos espacios para imaginar y aprender 💛")
 
