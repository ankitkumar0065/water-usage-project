
import streamlit as st
import pandas as pd

df = pd.read_csv("household_water_usage_jan_mar_2024.csv")
st.title("Water Consumption Monitoring Dashboard")
household = st.selectbox("Select Household", df['Household_ID'].unique())
filtered = df[df['Household_ID'] == household]
st.line_chart(filtered.set_index('Date')['Total_Usage_Liters'])
