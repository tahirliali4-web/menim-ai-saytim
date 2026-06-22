import os
import streamlit as st
import google.generativeai as genai

# Açarını əlavə et
api_key = st.secrets["GEMINI_API_KEY"]

# Əgər AQ. ilə başlayırsa, biz bunu 'genai' kitabxanası ilə yox, 
# birbaşa HTTP sorğusu ilə və ya 'google-auth' ilə etməliyik.
# Amma əvvəlcə bunu yoxla:
try:
    genai.configure(api_key=api_key)
    model = genai.GenerativeModel('gemini-1.5-flash')
    response = model.generate_content("Salam")
    st.write(response.text)
except Exception as e:
    st.error(f"Xəta baş verdi: {e}")
