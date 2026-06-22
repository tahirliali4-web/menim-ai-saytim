import streamlit as st
from sklearn.tree import DecisionTreeClassifier

st.title("Süni İntellektlə Xəta Diaqnozu")

# 1. Məlumatlar (Modeli öyrədirik)
# Siyahıdakı hər bir [xəta_kodu, port] cütlüyü bir nümunədir
X_data = [[10, 80], [12, 443], [5, 21], [500, 0], [550, 0], [600, 12]]
# 0 = Şəbəkə xətası, 1 = Sistem xətası
y_cavablar = [0, 0, 0, 1, 1, 1] 

model = DecisionTreeClassifier()
model.fit(X_data, y_cavablar)

# 2. İstifadəçidən məlumat alırıq
xata_kodu = st.number_input("Xəta Kodu daxil et:", value=10)
port = st.number_input("Port nömrəsi daxil et:", value=80)

# 3. Analiz düyməsi
if st.button("Analiz et"):
    yeni_problem = [[xata_kodu, port]]
    texmin = model.predict(yeni_problem)
    
    if texmin[0] == 0:
        st.error(f"Nəticə: Bu bir ŞƏBƏKƏ xətasıdır!")
    else:
        st.success(f"Nəticə: Bu bir SİSTEM xətasıdır!")
