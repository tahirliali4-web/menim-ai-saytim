import streamlit as st
import pandas as pd

st.title("🌐 Universal IT Xəta Diaqnoz Sistemi")

# Bütün IT xətalarını burada saxlayırıq (Lüğət formatında)
# İstədiyin qədər xəta əlavə edə bilərsən
xeta_bazasi = {
    404: {"ad": "Not Found (Sayt tapılmadı)", "təsir": "Şəbəkə", "həll": "URL ünvanını yoxlayın."},
    500: {"ad": "Internal Server Error", "təsir": "Sistem", "həll": "Server tərəfində problem var, adminə yazın."},
    403: {"ad": "Forbidden (İcazə yoxdur)", "təsir": "Təhlükəsizlik", "həll": "İstifadəçi hüquqlarınızı yoxlayın."},
    503: {"ad": "Service Unavailable", "təsir": "Sistem", "həll": "Server yüklənib, bir az sonra cəhd edin."},
    200: {"ad": "OK (Xəta yoxdur)", "təsir": "Normal", "həll": "Hər şey qaydasındadır."}
}

# Yan panel
st.sidebar.header("Xəta Kodu Daxil Et")
kod = st.sidebar.number_input("Xəta kodu (Məs: 404, 500, 403):", value=404)

if st.sidebar.button("Diaqnoz qoy"):
    if kod in xeta_bazasi:
        xeta = xeta_bazasi[kod]
        st.success(f"Xəta: {xeta['ad']}")
        st.write(f"**Təsir dairəsi:** {xeta['təsir']}")
        st.write(f"**Həll yolu:** {xeta['həll']}")
    else:
        st.error("Bu xəta bazamızda yoxdur, amma ümumi olaraq: Log fayllarını yoxlayın!")

# Bütün bazanı görmək üçün
st.write("---")
st.write("### 📚 Bazadakı Mövcud Xətalar")
df = pd.DataFrame.from_dict(xeta_bazasi, orient='index')
st.table(df)
