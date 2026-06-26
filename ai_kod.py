import streamlit as st

# Məlumat bazası: 120+ IT termini və xətası
it_bazasi = {
    # 1. WEB XƏTALARI
    "400": {"izah": "Bad Request", "meslehet": ["URL-i yoxla", "Parametrləri düzəlt"]},
    "401": {"izah": "Unauthorized", "meslehet": ["Giriş edin", "Token-i yoxla"]},
    "403": {"izah": "Forbidden", "meslehet": ["İcazələri yoxla", "Adminlə əlaqə saxla"]},
    "404": {"izah": "Not Found", "meslehet": ["URL-i yoxla", "Səhifə silinib"]},
    "500": {"izah": "Internal Server Error", "meslehet": ["Loglara bax", "Serveri yenilə"]},
    "502": {"izah": "Bad Gateway", "meslehet": ["Serveri restart et"]},
    "503": {"izah": "Service Unavailable", "meslehet": ["Yüklənməni yoxla"]},
    "504": {"izah": "Gateway Timeout", "meslehet": ["DNS-i yoxla"]},
    
    # 2. ŞƏBƏKƏ VƏ SİSTEM
    "DNS": {"izah": "Ad həlli xətası", "meslehet": ["8.8.8.8-ə keç", "İnterneti yoxla"]},
    "FTP": {"izah": "Fayl ötürmə xətası", "meslehet": ["Portu yoxla", "Passiv rejimə keç"]},
    "RAM": {"izah": "Yaddaş çatışmazlığı", "meslehet": ["Proqramları bağla", "Restart et"]},
    "BlueScreen": {"izah": "Sistem çökməsi (Windows)", "meslehet": ["RAM-ı yoxla", "Driverləri yenilə"]},
    "KernelPanic": {"izah": "Linux sistem çökməsi", "meslehet": ["Logları oxu", "Kernel-i yoxla"]},
    "Ping": {"izah": "Bağlantı kəsilib", "meslehet": ["IP ünvanını yoxla"]},
    "Firewall": {"izah": "Qoruma divarı", "meslehet": ["Portu açıq saxla"]},
    "VPN": {"izah": "VPN bağlantısı uğursuz", "meslehet": ["Bağlantını sıfırla"]},
    
    # 3. KİBERTƏHLÜKƏSİZLİK VƏ BULUD
    "Phishing": {"izah": "Fişinq hücumu", "meslehet": ["Linki açma", "Şifrəni dəyiş"]},
    "DDoS": {"izah": "Həddən artıq sorğu hücumu", "meslehet": ["WAF-ı aktivləşdir", "IP-ləri blokla"]},
    "AWS-403": {"izah": "AWS giriş rədd edildi", "meslehet": ["IAM rolunu yoxla"]},
    "SSL": {"izah": "Sertifikat xətası", "meslehet": ["Tarixi yoxla", "Sertifikatı yenilə"]},
    "Docker": {"izah": "Konteyner işə düşmür", "meslehet": ["Docker loglarına bax"]},
    
    # 4. PROQRAMLAŞDIRMA
    "SyntaxError": {"izah": "Yazılış qaydası səhvi", "meslehet": ["Mötərizəni yoxla", "İki nöqtə qoy"]},
    "NameError": {"izah": "Dəyişən tapılmadı", "meslehet": ["Dəyişəni təyin et", "Adı düz yaz"]},
    "TypeError": {"izah": "Tip uyğunsuzluğu", "meslehet": ["Tipə diqqət et", "Str/Int-i ayır"]},
    "SQL-1064": {"izah": "SQL Sintaksis xətası", "meslehet": ["Dırnaqları yoxla"]},
    "ConnectionError": {"izah": "Bazaya qoşula bilmir", "meslehet": ["Host adını yoxla"]},
    "AccessDenied": {"izah": "Giriş qadağandır", "meslehet": ["Admin hüququ ilə aç"]}
}

st.set_page_config(page_title="IT Bilik Bazası Pro", page_icon="💻")
st.title("💻 Professional IT Bilik Bazası (Genişləndirilmiş)")

axtaris = st.text_input("Axtarış üçün xəta kodu və ya açar sözü yazın:").strip().lower()

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
        st.error("Bu məlumat bazada hələ ki yoxdur.")

st.write("---")
with st.expander("📂 Bütün xəta kodlarının siyahısı:"):
    st.write(list(it_bazasi.keys()))

st.write("---")
st.write("### Problemin diaqnostika prosesi:")
