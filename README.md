Nutreezy-Smart Food Recommendation & Nutrition Analyzer

Nutreezy adalah aplikasi berbasis Machine Learning yang membantu pengguna untuk:
- Menganalisis kandungan nutrisi makanan
- Memprediksi jumlah kalori menggunakan model regresi
- Memberikan rekomendasi alternatif makanan yang lebih sehat

Aplikasi ini dibangun menggunakan 
Python, Pandas, Streamlit, dan Scikit-Learn(Regresi Linear)

Fitur

- pilih makanan dari dataset  
- Prediksi kalori menggunakan Machine Learning (Linear Regression)  
- Klasifikasi manfaat makanan (Otot / Energi / Diet / Imunitas)  
- NutriScore (A - E)  
- Rekomendasi makanan alternatif yang lebih sehat  
- Visualisasi grafik nutrisi 

Machine Learning Model
Model yang digunakan:
Algoritma: Linear Regression
kenapa? 
karna data tidak terlalu kompleks,matematis dan linear. tidak ada hubungan aneh ataupun pola non linear
Ini alasan terkuat kenapa Linear Regression jadi sangat unggul di dataset nutrisi.

Fitur input: 
  - Protein  
  - Fiber  
  - Fat  
  - Sugar  
Output (Target): Calories

Cara Menjalankan
streamlit run src/app.py

untuk install library
pip install -r requirements.txt
