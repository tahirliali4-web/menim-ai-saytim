import streamlit as st

# Genişləndirilmiş IT və Python Məlumat Bazası
it_bazasi = {
    # Web Xətaları
    "404": {"izah": "Səhifə tapılmadı.", "meslehet": ["URL-i yoxla", "Səhifə silinib ola bilər"]},
    "500": {"izah": "Server daxili xətası.", "meslehet": ["Server loglarını yoxla", "Kodu nəzərdən keçir"]},
    
    # Python Proqramlaşdırma Xətaları
    "SyntaxError": {"izah": "Sintaksis xətası (yazılış qaydası).", "meslehet": ["Mötərizələri yoxla", "Dırnaq işarələrini bağla", "İki nöqtə (:) qoyulubmu?"]},
    "NameError": {"izah": "Dəyişən adı tapılmadı.", "meslehet": ["Dəyişənin adını düz yazmısan?", "Dəyişəni öncədən təyin etmisən?"]},
    "TypeError": {"izah": "Tip uyğunsuzluğu.", "meslehet": ["Rəqəmlə mətni toplayırsan?", "Funksiyaya düzgün tip göndər"]},
    "IndexError": {"izah": "Siyahı indeksi xətası.", "meslehet": ["Siyahının ölçüsündən böyük indeks istifadə etmə"]},
    
    # Sistem və Şəbəkə
    "DNS": {"izah": "DNS xətası.", "meslehet": ["İnterneti yoxla", "DNS ünvanlarını yenilə (8.8.8.8)"]},
    "RAM": {"izah": "Yaddaş tükəndi.", "meslehet": ["Proqramları bağla", "Restart et"]},
    "Port 80": {"izah": "HTTP portu məşğuldur.", "meslehet": ["Başqa web serveri söndür"]}
}

st.set_page_config(page_title="IT & Python Məsləhətçi", page_icon="💻")
st.title("💻 IT & Python Məsləhətçi")

axtaris = st.text_input("Xəta kodunu və ya xəta adını yazın (məs: 404, SyntaxError, DNS):").strip()

if axtaris:
    if axtaris in it_bazasi:
        data = it_bazasi[axtaris]
        st.subheader(f"🔍 İzahı: {data['izah']}")
        st.subheader("💡 Məsləhətlər:")
        for m in data['meslehet']:
            st.success(m)
    else:
        st.warning(f"'{axtaris}' haqqında hələ ki, məlumat yoxdur. Bazanı genişləndirmək üçün mənə bildir!")

# Vizual dəstək
st.write("---")
st.write("### Problemin diaqnozu üçün sistem sxemi:")
#
