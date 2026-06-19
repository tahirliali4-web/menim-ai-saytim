from sklearn.tree import DecisionTreeClassifier

# Süni intellekt üçün məlumatlar [Xəta Kodu, Port]
X_data = [[10, 80], [12, 443], [5, 21], [500, 0], [550, 0], [600, 12]]
y_cavablar = [0, 0, 0, 1, 1, 1]  # 0 = Şəbəkə, 1 = Sistem

model = DecisionTreeClassifier()
model.fit(X_data, y_cavablar)

print("Suni intellekt oyrendi!\n")

# Yeni problemi yoxlayırıq
yeni_problem = [[8, 80]] 
texmin = model.predict(yeni_problem)

if texmin[0] == 0:
    print(f"Giris {yeni_problem} ucun AI Texmini: Bu bir SEBEKE xetasidir!")
else:
    print(f"Giris {yeni_problem} ucun AI Texmini: Bu bir SISTEM xetasidir!")