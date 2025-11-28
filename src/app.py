import sys
import os
sys.path.append(os.path.dirname(os.path.abspath(__file__)))
import joblib
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

model_path = os.path.join(BASE_DIR, "..", "models", "calorie_model.pkl")
data_path = os.path.join(BASE_DIR, "..", "Data", "cleaned_food.csv")

print("Model path :", model_path)
print("Data path :", data_path)

from analyzer import classify_benefit, nutriscore
from recommender import healthier_alternatives

model = joblib.load(model_path)
df_raw = pd.read_csv(data_path)
df = df_raw.groupby("food").mean(numeric_only=True).reset_index().round()

def predict_calories(nutrition):
    return model.predict([nutrition])[0]


def recommend_food(goal):
    if goal == "protein":
        return df.sort_values("protein", ascending=False).head(5)
    elif goal == "fiber":
        return df.sort_values("fiber", ascending=False).head(5)
    elif goal == "low_cal":
        return df.sort_values("calories").head(5)
    
st.set_page_config(page_title="Nutreezy", page_icon="🥗")

st.title(" Nutreezy - Smart Food Analyzer")


food_list = sorted(df['food'].unique().tolist())
selected_food = st.selectbox("Pilih makanan:", food_list)

food_data = df[df["food"] == selected_food].iloc[0].to_dict()

st.subheader(" Kandungan Nutrisi")
st.markdown(
    f"""
    <div style="
        padding: 20px;
        border-radius: 12px;
        background: #f8f9fa;
        border: 1px solid #e0e0e0;
        width: 50%;
    ">
        <h4 style="margin-top: 0;"> {food_data['food']}</h4>
        <ul style="line-height: 1.8;">
            <li><b>Calories:</b> {food_data['calories']}</li>
            <li><b>Protein:</b> {food_data['protein']}</li>
            <li><b>Fat:</b> {food_data['fat']}</li>
            <li><b>Carbs:</b> {food_data['carbs']}</li>
            <li><b>Fiber:</b> {food_data['fiber']}</li>
            <li><b>Sugar:</b> {food_data['sugar']}</li>
        </ul>
    </div>
    """,
    unsafe_allow_html=True
)

benefit = classify_benefit(food_data)
score = nutriscore(food_data)

st.subheader(" Hasil Analisis")
st.success(f"Manfaat utama: **{benefit}**")
st.info(f"NutriScore: **{score}**")

st.subheader(" Grafik Nutrisi")
labels = ["Protein", "Fat", "Carbs", "Fiber","Sugar"]
sample = [
    food_data["protein"],
    food_data["fat"],
    food_data["carbs"],
    food_data["fiber"],
    food_data["sugar"]
]

predicted_calories = predict_calories(sample)

fig, ax = plt.subplots()
ax.bar(labels, sample)
st.pyplot(fig)

st.subheader(" Alternatif Lebih Sehat")
alternatives = healthier_alternatives(selected_food, df, top_n=1)

if len(alternatives) == 0:
    st.warning("Tidak ada alternatif yang lebih sehat ditemukan")
else:
    for alt in alternatives:
        st.success(f" {alt['food']}")
        st.write(f"Alasan: {alt['reason']}")
        st.write(f"Kalori: {alt['calories']} | Protein: {alt['protein']} | Fiber: {alt['fiber']}")
        st.write("---")