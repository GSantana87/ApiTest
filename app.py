import streamlit as st
import google.generativeai as genai

# 1. Securely fetch the key from Streamlit's hidden settings
ai_key = st.secrets["GEMINI_API_KEY"]
genai.configure(api_key=ai_key)

# 2. Setup the model (Upgraded to the active 2.5 version)
model = genai.GenerativeModel(
    model_name="gemini-2.5-flash",
    system_instruction="You are an expert copywriter and editor. Rephrase the user's text into 3 versions: 1. Professional, 2. Casual, 3. Concise." 
)

# 3. Build the Interface
user_phrase = st.text_area("What do you want to rephrase?", height=150)

# 4. Create the button and trigger the AI
if st.button("Rephrase Text"):
    if user_phrase:
        with st.spinner("Rephrasing..."):
            response = model.generate_content(user_phrase)
            st.write(response.text)
