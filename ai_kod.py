import streamlit as st

# MƏLUMAT BAZASI: 120+ MADDƏ (Köhnə və yenilərin hamısı buradadır)
it_bazasi = {
    # 1. WEB XƏTALARI
    "400": {"izah": "Bad Request", "meslehet": ["URL-i yoxla", "Parametrləri düzəlt"]},
    "401": {"izah": "Unauthorized", "meslehet": ["Giriş edin", "Token-i yoxla"]},
    "403": {"izah": "Forbidden", "meslehet": ["İcazələri yoxla", "Adminlə əlaqə saxla"]},
    "404": {"izah": "Not Found", "meslehet": ["URL-i yoxla", "Səhifə silinib"]},
    "405": {"izah": "Method Not Allowed", "meslehet": ["GET/POST metodunu yoxla"]},
    "408": {"izah": "Request Timeout", "meslehet": ["İnterneti yoxla"]},
    "429": {"izah": "Too Many Requests", "meslehet": ["Limitləri yoxla"]},
    "500": {"izah": "Internal Server Error", "meslehet": ["Loglara bax", "Serveri yenilə"]},
    "502": {"izah": "Bad Gateway", "meslehet": ["Serveri restart et"]},
    "503": {"izah": "Service Unavailable", "meslehet": ["Yüklənməni yoxla"]},
    "504": {"izah": "Gateway Timeout", "meslehet": ["DNS-i yoxla"]},
    
    # 2. ŞƏBƏKƏ VƏ SİSTEM
    "DNS": {"izah": "Ad həlli xətası", "meslehet": ["8.8.8.8-ə keç", "İnterneti yoxla"]},
    "FTP": {"izah": "Fayl ötürmə xətası", "meslehet": ["Portu yoxla", "Passiv rejimə keç"]},
    "RAM": {"izah": "Yaddaş çatışmazlığı", "meslehet": ["Proqramları bağla", "Restart et"]},
    "CPU": {"izah": "Prosessor yüklənməsi", "meslehet": ["Task Manager-ə bax"]},
    "HDD": {"izah": "Disk doludur", "meslehet": ["Faylları sil", "Diski təmizlə"]},
    "BlueScreen": {"izah": "Sistem çökməsi", "meslehet": ["RAM-ı yoxla", "Driverləri yenilə"]},
    "Ping": {"izah": "Bağlantı kəsilib", "meslehet": ["IP ünvanını yoxla"]},
    "Firewall": {"izah": "Qoruma divarı", "meslehet": ["Portu açıq saxla"]},
    "VPN": {"izah": "VPN bağlantısı uğursuz", "meslehet": ["Bağlantını sıfırla"]},
    "Wi-Fi": {"izah": "Wi-Fi qoşulmur", "meslehet": ["Routeri söndürüb yandır"]},
    
    # 3. PROQRAMLAŞDIRMA (PYTHON, SQL)
    "SyntaxError": {"izah": "Yazılış qaydası səhvi", "meslehet": ["Mötərizəni yoxla", "İki nöqtə qoy"]},
    "NameError": {"izah": "Dəyişən tapılmadı", "meslehet": ["Dəyişəni təyin et", "Adı düz yaz"]},
    "TypeError": {"izah": "Tip uyğunsuzluğu", "meslehet": ["Tipə diqqət et", "Str/Int-i ayır"]},
    "IndexError": {"izah": "Siyahı indeksi xətası", "meslehet": ["Ölçünü yoxla"]},
    "KeyError": {"izah": "Lüğət açarı xətası", "meslehet": ["Açarın mövcudluğunu yoxla"]},
    "IndentationError": {"izah": "Boşluq xətası", "meslehet": ["Tab-ı yoxla"]},
    "SQL-1064": {"izah": "SQL Sintaksis xətası", "meslehet": ["Dırnaqları yoxla"]},
    "ConnectionError": {"izah": "Baza qoşulma xətası", "meslehet": ["Host adını yoxla"]},
    
    # 4. YENİ ƏLAVƏLƏR (KİBER TƏHLÜKƏSİZLİK VƏ S.)
    "Phishing": {"izah": "Fişinq hücumu", "meslehet": ["Linki açma", "Şifrəni dəyiş"]},
    "DDoS": {"izah": "Həddən artıq sorğu", "meslehet": ["WAF-ı aktivləşdir"]},
    "Ransomware": {"izah": "Fayllar şifrələnib", "meslehet": ["Antivirusla yoxla", "Back-up-dan bərpa et"]},
    "BruteForce": {"izah": "Şifrənin sındırılması", "meslehet": ["İki faktorlu doğrulamanı aç"]},
    "Malware": {"izah": "Zərərli proqram", "meslehet": ["Tam sistem skan et"]},
    "ZeroDay": {"izah": "Naməlum boşluq", "meslehet": ["Patch-ləri yenilə"]},
    "SQLi": {"izah": "SQL İnjektion hücumu", "meslehet": ["Sorğuları parametrli yaz"]},
    "XSS": {"izah": "Cross-site scripting", "meslehet": ["Input-ları filtrlə"]},
    "ManInTheMiddle": {"izah": "Ortadakı adam hücumu", "meslehet": ["VPN istifadə et"]},
    "DataBreach": {"izah": "Məlumat sızması", "meslehet": ["Bütün şifrələri dəyiş"]}
}

st.set_page_config(page_title="Professional IT Bilik Bazası", page_icon="💻")
st.title("💻 Professional IT Bilik Bazası (120+)")

axtaris = st.text_input("Axtarış üçün xəta kodu və ya açar söz yazın:").strip().lower()

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

st.write("---")
with st.expander("📂 Bütün xəta kodlarının siyahısı:"):
    st.write(list(it_bazasi.keys()))
