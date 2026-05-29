import streamlit as st
import google.generativeai as genai

# --- CONFIGURACIÓN DE PÁGINA Y ESTILO ---
st.set_page_config(page_title="Rephrase it!", page_icon="✍️", layout="centered")

# Ocultar el ícono de link (anchor) de los títulos
st.markdown("""
    <style>
    .stApp .header-anchor {display: none;}
    </style>
    """, unsafe_allow_html=True)

# --- CONFIGURACIÓN DE IA ---
ai_key = st.secrets["GEMINI_API_KEY"]
genai.configure(api_key=ai_key)

# --- INTERFAZ MINIMALISTA ---
st.title("✍️ Rephrase it!")

target_language = st.selectbox(
    "Choose your language:", 
    ["Español", "English", "Deutsch", "Italiano", "Português"]
)

user_phrase = st.text_area("Enter your text below:", height=200)

if st.button("Generate"):
    if user_phrase:
        with st.spinner("Refining..."):
            model = genai.GenerativeModel(
                model_name="gemini-2.5-flash",
                system_instruction=f"You are an expert copywriter. Rephrase the user's text into 3 versions: 1. Professional, 2. Casual, 3. Concise. Write results in {target_language}." 
            )
            response = model.generate_content(user_phrase)
            st.write(response.text)
    else:
        st.warning("Please enter some text first.")
