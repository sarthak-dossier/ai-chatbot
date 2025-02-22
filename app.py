import streamlit as st
import google.generativeai as genai
API_KEY = "AIzaSyBXUa9RUn3eh1ffKs9WavVbs53vr8wYiDY"
genai.configure(api_key=API_KEY)
model = genai.GenerativeModel("gemini-pro")
st.title("🤖 AI Chatbot using Google Gemini API key")
user_input = st.text_input("You:", "")
if st.button("Send"):
    if user_input:
        response = model.generate_content(user_input)
        st.text_area("Chatbot:", response.text.strip(), height=100)
st.markdown("---")  
st.markdown("<p style='text-align: center; font-size: 25px; font-weight: bold;'>𝐜𝐫𝐞𝐚𝐭𝐞𝐝 𝐛𝐲 𝐒𝐚𝐫𝐭𝐡𝐚𝐤 𝐌𝐚𝐧𝐭𝐫𝐢</p>", unsafe_allow_html=True)
