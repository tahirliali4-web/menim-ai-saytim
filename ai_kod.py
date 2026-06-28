import streamlit as st
import json

# JSON faylını oxuyur
def bazani_yukle():
    with open('it_bazasi.json', 'r', encoding='utf-8') as f:
        return json.load(f)

it_bazasi = bazani_yukle()

st.set_page_config(page_title="Professional IT Bilik Bazası", page_icon="💻")
st.title("💻 Professional IT Bilik Bazası (Limitsiz)")

axtaris = st.text_input("Axtarış üçün xəta kodu yazın:").strip().lower()

if axtaris:
    tapildi = False
    for kod, melumat in it_bazasi.items():
        if axtaris in kod.lower() or axtaris in melumat['izah'].lower():
            st.subheader(f"✅ Tapıldı: {kod}")
            st.info(f"İzahı: {melumat['izah']}")
            st.subheader("💡 Məsləhətlər:")
            for m in melumat['meslehet']:
                st.success(m)
            tapildi = True
    if not tapildi:
        st.error("Bu məlumat hələlik bazada yoxdur.")

with st.expander("📂 Bütün xəta kodları:"):
    st.write(list(it_bazasi.keys()))
