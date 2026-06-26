import streamlit as st

# Məlumat bazası (Daha geniş)
it_bazasi = {
    "404": {"izah": "Not Found (Səhifə tapılmadı).", "meslehet": ["URL-i yoxla", "Səhifə silinib"]},
    "500": {"izah": "Internal Server Error (Server xətası).", "meslehet": ["Loglara bax", "Serveri yenilə"]},
    "DNS": {"izah": "DNS xətası (Ad həlli mümkün olmadı).", "meslehet": ["DNS 8.8.8.8-ə keç", "İnterneti yoxla"]},
    "SyntaxError": {"izah": "Sintaksis səhvi.", "meslehet": ["Mötərizələri yoxla", "Dırnaqları bağla"]}
}

st.set_page_config(page_title="IT Ağıllı Axtarış", page_icon="🔍")
st.title("🔍 IT Ağıllı Axtarış Mərkəzi")

axtaris = st.text_input("Xəta kodu və ya açar söz yazın:").strip().lower()

if axtaris:
    tapildi = False
    for kod, melumat in it_bazasi.items():
        # Həm açar sözə, həm də izahın içindəki sözlərə görə axtarır
        if axtaris in kod.lower() or axtaris in melumat['izah'].lower():
            st.subheader(f"✅ Tapıldı: {kod}")
            st.info(f"İzahı: {melumat['izah']}")
            st.subheader("💡 Məsləhətlər:")
            for m in melumat['meslehet']:
                st.success(m)
            tapildi = True
            break # Tapdısa dayandır
    
    if not tapildi:
        st.error("Təəssüf ki, axtardığınız mövzuda nəticə tapılmadı.")
