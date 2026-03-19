import streamlit as st
import pandas as pd

st.title("Global Economic Risk Monitor")

url = "https://raw.githubusercontent.com/alenachuklina/global-economic-risk-monitor/main/data/merged_data.csv"
df = pd.read_csv(url)

df = df.dropna()

countries = df["Country Name"].unique()
country = st.selectbox("Select country", countries)

df_country = df[df["Country Name"] == country]

df_country = df_country.sort_values("year")

st.subheader(f"GDP growth and Inflation — {country}")

st.line_chart(
    df_country.set_index("year")[["GDP_growth", "Inflation"]]
)
