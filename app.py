import streamlit as st
import google.generativeai as genai

# Securely fetch the key from Streamlit's hidden settings
ai_key = st.secrets["GEMINI_API_KEY"]
genai.configure(api_key=ai_key)

model = genai.GenerativeModel(
   model_name="models/gemini-1.5-flash",
    system_instruction="You are an expert copywriter. Rephrase the user's text into 3 versions..." 
)

user_phrase = st.text_input("What do you want to rephrase?")

# Esto evita que se envíe texto vacío a Google al cargar la página
if user_phrase:
    with st.spinner("Rephrasing..."):
        response = model.generate_content(user_phrase)
        st.write(response.text)
