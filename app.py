import streamlit as st
import google.generativeai as genai

# 1. Securely fetch the key from Streamlit's hidden settings
ai_key = st.secrets["GEMINI_API_KEY"]
genai.configure(api_key=ai_key)

# 2. Selector de Idioma (¡Lo nuevo!)
target_language = st.selectbox(
    "Choose your language / Elige tu idioma:", 
    ["Español", "English", "Deutsch", "Italiano", "Português"]
)

# 3. Setup the model (¡Ahora dinámico!)
# Nota la letra 'f' antes de las comillas. Esto nos permite inyectar la variable target_language dentro de las instrucciones.
model = genai.GenerativeModel(
    model_name="gemini-2.5-flash",
    system_instruction=f"You are an expert copywriter and editor. Rephrase the user's text into 3 versions: 1. Professional, 2. Casual, 3. Concise. You MUST write the results entirely in {target_language}." 
)

# 4. Build the Interface
user_phrase = st.text_area("What do you want to rephrase?", height=150)

# 5. Create the button and trigger the AI
if st.button("Rephrase Text"):
    if user_phrase:
        with st.spinner("Rephrasing..."):
            response = model.generate_content(user_phrase)
            st.write(response.text)
