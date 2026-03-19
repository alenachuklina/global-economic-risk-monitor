import streamlit as st
import pandas as pd

st.title("Global Economic Risk Monitor")

url = "https://raw.githubusercontent.com/alenachuklina/global-economic-risk-monitor/main/data/merged_data.csv"
df = pd.read_csv(url)

df = df.dropna()

countries = df["Country Name"].unique()

selected_countries = st.multiselect(
    "Select countries",
    countries,
    default=["Spain", "Germany", "France"]
)

df_filtered = df[df["Country Name"].isin(selected_countries)]

df_country = df_country.sort_values("year")

st.subheader("GDP growth and Inflation comparison")

for country in selected_countries:
    df_country = df_filtered[df_filtered["Country Name"] == country]
    df_country = df_country.sort_values("year")

    st.line_chart(
        df_country.set_index("year")[["GDP_growth", "Inflation"]],
        use_container_width=True
    )
