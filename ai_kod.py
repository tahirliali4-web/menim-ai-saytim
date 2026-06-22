import streamlit as st
import google.generativeai as genai

st.title("🤖 Hər şeyi Bilən İT Köməkçisi")

# Secrets-dən açarı təhlükəsiz şəkildə oxuyuruq
# Əgər API açarı Secrets-də düzgün qeyd olunubsa, proqram işləyəcək
try:
    genai.configure(api_key=st.secrets["GEMINI_API_KEY"])
    model = genai.GenerativeModel('gemini-pro')
except Exception as e:
    st.error("API açarı tapılmadı! Zəhmət olmasa Streamlit 'Secrets' bölməsinə GEMINI_API_KEY = 'açarın' formatında əlavə edin.")
    st.stop()

# Söhbət tarixçəsini saxlayaq
if "messages" not in st.session_state:
    st.session_state.messages = []

# Əvvəlki mesajları göstərək
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# İstifadəçidən sual alaq
if prompt := st.chat_input("İT sualını yaz..."):
    st.chat_message("user").markdown(prompt)
    st.session_state.messages.append({"role": "user", "content": prompt})

    # AI-yə sualı göndərək
    try:
        response = model.generate_content(f"Sən bir İT mütəxəssisisən. Bu suala ətraflı cavab ver: {prompt}")
        cavab = response.text
    except Exception as e:
        cavab = "Üzr istəyirəm, texniki xəta baş verdi."
    
    with st.chat_message("assistant"):
        st.markdown(cavab)
    st.session_state.messages.append({"role": "assistant", "content": cavab})
