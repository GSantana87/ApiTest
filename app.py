import streamlit as st
import google.generativeai as genai

# 1. Connect your Web App to your Gemini Brain
genai.configure(api_key="AIzaSyDZk0Xvu3Tc77aMxUFdgZa7nIf-uKjzDQA
")

model = genai.GenerativeModel(
    model_name="gemini-1.5-flash",
    # Paste the exact System Instructions you used in Google AI Studio here:
    system_instruction="You are an expert copywriter. Rephrase the user's text into 3 versions..."
)

# 2. Build the Minimal Interface
# This creates the single blank bar for you to type in
user_phrase = st.text_input("What do you want to rephrase?")

# 3. Show the Results
if user_phrase:
    with st.spinner("Rephrasing..."):
        response = model.generate_content(user_phrase)
        st.write(response.text)