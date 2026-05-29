import streamlit as st
import google.generativeai as genai

# --- CONFIGURACIÓN DE PÁGINA ---
st.set_page_config(page_title="Copywriter AI", page_icon="✍️", layout="centered")

# --- CONFIGURACIÓN DE IA ---
# Asegúrate de tener la clave configurada en los Secrets de Streamlit
ai_key = st.secrets["GEMINI_API_KEY"]
genai.configure(api_key=ai_key)

# --- INTERFAZ SIDEBAR ---
st.sidebar.title("Settings")
target_language = st.sidebar.selectbox(
    "Select Language:", 
    ["Español", "English", "Deutsch", "Italiano", "Português"]
)
st.sidebar.info("Tool designed for professional editing.")

# --- INTERFAZ PRINCIPAL ---
st.title("✍️ Professional AI Copywriter")
st.markdown("Enter your text below to get **Professional**, **Casual**, and **Concise** versions.")
st.divider()

user_phrase = st.text_area("Your text:", height=200)

if st.button("Generate Rephrased Versions"):
    if user_phrase:
        with st.spinner("Refining your text..."):
            model = genai.GenerativeModel(
                model_name="gemini-2.5-flash",
                system_instruction=f"You are an expert copywriter. Rephrase the user's text into 3 versions: 1. Professional, 2. Casual, 3. Concise. Write results in {target_language}." 
            )
            response = model.generate_content(user_phrase)
            st.write(response.text)
    else:
        st.error("Please write something first!")
