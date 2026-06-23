import streamlit as st

# Xəta kodları bazası (Bura istədiyin qədər xəta əlavə edə bilərsən)
xeta_bazasi = {
    "404": "Səhifə tapılmadı. URL-i yoxlayın.",
    "500": "Server daxili xətası. Texniki heyətə müraciət edin.",
    "403": "Giriş qadağandır. İcazəniz yoxdur.",
    "Port 80": "HTTP xidməti (Web) üçün istifadə olunur.",
    "Port 443": "HTTPS xidməti (Təhlükəsiz Web) üçün istifadə olunur."
}

st.title("Şəbəkə Xəta Analizatoru")

kod = st.text_input("Xəta kodu və ya Port nömrəsini daxil edin (məs: 404):")

if st.button("Analiz et"):
    if kod in xeta_bazasi:
        st.success(f"Nəticə: {xeta_bazasi[kod]}")
    else:
        st.warning("Bu xəta kodu bazamızda yoxdur. Zəhmət olmasa başqa kod daxil edin.")
