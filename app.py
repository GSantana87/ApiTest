import streamlit as st
import google.generativeai as genai

# --- CONFIGURACIÓN DE PÁGINA ---
st.set_page_config(page_title="Reprase it!", page_icon="✍️", layout="centered")

# --- CONFIGURACIÓN DE IA ---
ai_key = st.secrets["GEMINI_API_KEY"]
genai.configure(api_key=ai_key)

# --- INTERFAZ MINIMALISTA ---
st.title("✍️ Reprase it!")

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
