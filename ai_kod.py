import streamlit as st

# Genişləndirilmiş IT xəta və məsləhət bazası
xeta_bazasi = {
    "404": {"izah": "Səhifə tapılmadı.", "meslehet": "URL-i yoxlayın və ya səhifənin silindiyini yoxlayın."},
    "500": {"izah": "Server daxili xətası.", "meslehet": "Server loglarını yoxlayın, konfiqurasiya xətası ola bilər."},
    "503": {"izah": "Xidmət əlçatan deyil.", "meslehet": "Serverin həddindən artıq yükləndiyini və ya texniki baxışda olduğunu yoxlayın."},
    "Port 21": {"izah": "FTP (Fayl Transferi) portu.", "meslehet": "İcazələri yoxlayın, passiv/aktiv rejimini dəyişməyi sınayın."},
    "Port 22": {"izah": "SSH (Uzaqdan idarəetmə) portu.", "meslehet": "Serverin cavab verdiyini və firewall-un girişi bağlamadığını yoxlayın."},
    "Port 80/443": {"izah": "HTTP/HTTPS (Web) portları.", "meslehet": "Web server (Nginx/Apache) xidmətinin işlək olduğunu yoxlayın."},
    "DNS": {"izah": "Ad həlli xətası (DNS Error).", "meslehet": "İnternet bağlantınızı və DNS server ünvanlarını (8.8.8.8) yoxlayın."}
}

st.set_page_config(page_title="IT Dəstək Məsləhətçisi", page_icon="💻")
st.title("💻 IT Dəstək Məsləhətçisi")
st.write("Şəbəkə və sistem xətaları üçün köməkçi.")

kod = st.text_input("Xəta kodunu və ya Portu daxil edin (məs: 503, Port 22, DNS):")

if st.button("Analiz et"):
    # İstifadəçinin daxil etdiyi məlumatı bazadakı açarlarla uyğunlaşdırmaq
    kod = kod.strip()
    if kod in xeta_bazasi:
        st.subheader("🔍 İzahı:")
        st.info(xeta_bazasi[kod]["izah"])
        st.subheader("💡 Məsləhətim:")
        st.success(xeta_bazasi[kod]["meslehet"])
    else:
        st.warning("Bu xəta bazamda yoxdur. Zəhmət olmasa siyahıdakı kodlardan birini yoxlayın.")

# Siyahını görmək üçün
with st.expander("Bazada olan kodlar"):
    st.write(list(xeta_bazasi.keys()))
