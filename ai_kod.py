import streamlit as st

# Geniş və çoxşaxəli IT Məlumat Bazası
it_bazasi = {
    "404": {
        "izah": "Səhifə tapılmadı (Not Found).",
        "meslehet": [
            "1. URL ünvanını diqqətlə yoxlayın, kiçik hərflərlə yazmağa çalışın.",
            "2. Səhifənin köhnə olub-olmadığını yoxlayın, brauzerin 'cache' yaddaşını təmizləyin.",
            "3. Saytın 'sitemap' hissəsindən səhifəni yenidən axtarın."
        ]
    },
    "500": {
        "izah": "Server daxili xətası (Internal Server Error).",
        "meslehet": [
            "1. Saytı bir neçə saniyədən sonra yeniləyin (F5).",
            "2. Əgər administrator sizsinizsə, serverin 'error.log' faylına baxın.",
            "3. Serverdə çalışan skriptlərin icazələrini (permissions) yoxlayın."
        ]
    },
    "DNS": {
        "izah": "DNS serveri tapılmadı (Domain Name System Error).",
        "meslehet": [
            "1. İnternet bağlantınızın olub-olmadığını yoxlayın.",
            "2. Kompüterin DNS parametrlərinə 8.8.8.8 və ya 1.1.1.1 daxil edin.",
            "3. 'ipconfig /flushdns' əmrini terminalda (CMD) icra edin."
        ]
    },
    "Port 80/443": {
        "izah": "Web trafik portları ilə əlaqəli problemlər.",
        "meslehet": [
            "1. Apache və ya Nginx servisinin işlədiyindən əmin olun.",
            "2. Firewall (Firewall) tənzimləmələrində bu portların açıq olduğunu yoxlayın.",
            "3. Başqa bir proqramın (məsələn: Skype) həmin portu tutub-tutmadığını yoxlayın."
        ]
    }
}

st.set_page_config(page_title="IT Məsləhətçi Pro", page_icon="⚙️")
st.title("⚙️ IT Məsləhətçi Pro")
st.write("Sistem və şəbəkə xətaları üçün çoxşaxəli dəstək platforması.")

# İstifadəçi girişi
kod = st.selectbox("Xəta kodunu və ya mövzunu seçin:", list(it_bazasi.keys()))

if st.button("Analiz et"):
    data = it_bazasi[kod]
    
    st.subheader(f"🔍 İzahı: {data['izah']}")
    
    st.subheader("💡 Məsləhətlər:")
    # Məsləhətləri siyahı şəklində göstər
    for m in data['meslehet']:
        st.success(m)

# IT problemlərinin həlli üçün ümumi sxem (Anlamaq üçün köməkçi)
st.write("---")
st.write("### Ümumi IT Problemlərinin Diaqnostika Sxemi:")
st.image("https://www.freeiconspng.com/uploads/technical-support-icon-2.png", caption="Texniki Dəstək Prosesi")
