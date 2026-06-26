import streamlit as st

# Çox genişləndirilmiş IT Məlumat Bazası
it_bazasi = {
    # Python
    "SyntaxError": {"izah": "Yazılış qaydası səhvi.", "meslehet": ["Mötərizəni yoxla", "İki nöqtəni qoy", "Dırnaqları bağla"]},
    "NameError": {"izah": "Dəyişən adı tanınmır.", "meslehet": ["Dəyişəni əvvəl təyin et", "Adı düz yaz"]},
    "TypeError": {"izah": "Tip uyğunsuzluğu.", "meslehet": ["Str və Int-i birləşdirmə", "Düzgün tip istifadə et"]},
    
    # Şəbəkə
    "DNS": {"izah": "Ad həlli xətası.", "meslehet": ["İnterneti yoxla", "DNS 8.8.8.8 et", "Modemi restart et"]},
    "404": {"izah": "Səhifə tapılmadı.", "meslehet": ["URL-i yoxla", "Səhifə silinib ola bilər"]},
    "500": {"izah": "Server daxili xətası.", "meslehet": ["Server loglarına bax", "Kodu debug et"]},
    
    # SQL (Verilənlər Bazası)
    "SQL-1064": {"izah": "SQL sintaksis xətası.", "meslehet": ["Sorğunu yoxla", "Dırnaqlara diqqət et"]},
    "ConnectionError": {"izah": "Bazaya qoşula bilmir.", "meslehet": ["Host adını yoxla", "Şifrəni yoxla"]},
    
    # Windows/Sistem
    "BlueScreen": {"izah": "Sistem çökməsi.", "meslehet": ["RAM-ı yoxla", "Driverləri yenilə"]},
    "AccessDenied": {"izah": "İcazə yoxdur.", "meslehet": ["Administrator kimi aç", "Fayl icazələrini yoxla"]}
}

st.set_page_config(page_title="IT Ensklopediyası", page_icon="📚")
st.title("📚 IT Mütəxəssis Aləti")

# Axtarış
axtaris = st.text_input("Axtarış (məs: SyntaxError, DNS, BlueScreen):").strip()

if axtaris:
    if axtaris in it_bazasi:
        data = it_bazasi[axtaris]
        st.subheader(f"İzahı: {data['izah']}")
        st.subheader("💡 Məsləhətlər:")
        for m in data['meslehet']:
            st.success(m)
    else:
        st.error(f"'{axtaris}' bazada yoxdur. Zəhmət olmasa siyahını yoxlayın.")

# Vizual köməkçi (Axtarış prosesini anlamaq üçün)
st.write("---")
st.write("### IT Problemlərinin Həlli Addımları:")

st.write("1. Xətanı müəyyən et. 2. Bazadan axtar. 3. Məsləhəti tətbiq et.")
