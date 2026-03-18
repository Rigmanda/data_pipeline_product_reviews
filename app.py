import streamlit as st
import pandas as pd
import plotly.express as px

st.title("Product Reviews Dashboard")

# Load data
df = pd.read_csv("data/processed/reviews_products_with_sentiment.csv")

st.subheader("Raw Data")
st.dataframe(df)

# Example chart
if "sentiment" in df.columns:
    fig = px.histogram(df, x="sentiment", title="Sentiment Distribution")
    st.plotly_chart(fig)