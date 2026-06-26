import streamlit as st

# Tam və geniş IT Ensklopediyası
it_bazasi = {
    # 4xx Xətaları (Müştəri səhvi)
    "400": {"izah": "Bad Request (Yanlış sorğu).", "meslehet": ["URL-i yoxla", "Parametrləri düzəlt"]},
    "401": {"izah": "Unauthorized (Giriş icazəsi yoxdur).", "meslehet": ["Düzgün login/şifrə daxil et"]},
    "403": {"izah": "Forbidden (Giriş qadağandır).", "meslehet": ["İcazələri yoxla", "Adminlə əlaqə saxla"]},
    "404": {"izah": "Not Found (Səhifə tapılmadı).", "meslehet": ["URL-i diqqətlə yoxla", "Saytın ana səhifəsinə qayıt"]},
    "408": {"izah": "Request Timeout (Sorğu vaxtı bitdi).", "meslehet": ["İnterneti yoxla", "Səhifəni yenilə"]},
    
    # 5xx Xətaları (Server səhvi)
    "500": {"izah": "Internal Server Error (Server xətası).", "meslehet": ["Serveri yenilə", "Log fayllarına bax"]},
    "502": {"izah": "Bad Gateway (Keçid xətası).", "meslehet": ["Serverin cavab verməsini gözlə", "Gateway-i yoxla"]},
    "503": {"izah": "Service Unavailable (Xidmət hazır deyil).", "meslehet": ["Serverin həddən artıq yüklənməsini yoxla", "Bir az sonra yoxla"]},
    "504": {"izah": "Gateway Timeout (Keçid vaxtı bitdi).", "meslehet": ["Serverin cavab verməsini gözlə", "DNS parametrlərini yoxla"]},
    
    # Digər Texniki Xətalar
    "DNS": {"izah": "Ad həlli xətası.", "meslehet": ["DNS parametrlərini 8.8.8.8 et", "İnternet bağlantısını yoxla"]},
    "SyntaxError": {"izah": "Proqramlaşdırma sintaksis xətası.", "meslehet": ["Mötərizələri yoxla", "Yazılışı düzəlt"]},
    "BlueScreen": {"izah": "Windows sistem çökməsi.", "meslehet": ["RAM-ı yoxla", "Sürücüləri (driver) yenilə"]}
}

st.set_page_config(page_title="IT Ensklopediyası", page_icon="🌐")
st.title("🌐 IT Bütün Xətalar Mərkəzi")

# Axtarış hissəsi
axtaris = st.text_input("Xəta kodunu və ya xəta adını yazın (məs: 404, 500, DNS, SyntaxError):").strip()

if axtaris:
    if axtaris in it_bazasi:
        data = it_bazasi[axtaris]
        st.subheader(f"🔍 İzahı: {data['izah']}")
        st.subheader("💡 Məsləhətlər:")
        for m in data['meslehet']:
            st.success(m)
    else:
        st.error(f"'{axtaris}' bazada tapılmadı. Zəhmət olmasa düzgün kod yazdığınızdan əmin olun.")

# Baza siyahısı (İstifadəçi baxa bilsin)
with st.expander("Bazada olan bütün xəta kodları:"):
    st.write(list(it_bazasi.keys()))

st.write("---")
st.write("### Problemin diaqnostika prosesi:")
