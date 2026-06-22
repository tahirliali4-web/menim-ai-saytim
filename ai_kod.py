import streamlit as st
import google.generativeai as genai

# 1. Konfiqurasiya
st.title("🤖 Hər şeyi Bilən İT Köməkçisi")

try:
    # API açarını Secrets-dən alırıq
    api_key = st.secrets["GEMINI_API_KEY"]
    genai.configure(api_key=api_key)
    model = genai.GenerativeModel('gemini-1.5-flash')
except Exception as e:
    st.error(f"Xəta: {e}. Zəhmət olmasa Secrets-i yoxlayın.")
    st.stop()

# 2. Söhbət məntiqi
if "messages" not in st.session_state:
    st.session_state.messages = []

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

if prompt := st.chat_input("İT sualını bura yaz..."):
    st.chat_message("user").markdown(prompt)
    st.session_state.messages.append({"role": "user", "content": prompt})

    try:
        response = model.generate_content(prompt)
        cavab = response.text
    except Exception as e:
        cavab = f"Səhv baş verdi: {e}"
    
    with st.chat_message("assistant"):
        st.markdown(cavab)
    st.session_state.messages.append({"role": "assistant", "content": cavab})
