import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Load data
df = pd.read_csv('hasilanl_vid2.csv')

st.title("╱╲ Sentiment Analysis Dashboard ╲╱")

# Sidebar filters
status = st.sidebar.selectbox("Select Sentiment", ['All', 'Positive', 'Neutral', 'Negative'])

if status == 'All':
    filtered_df = df
else:
    filtered_df = df[df['sentiment'] == status.lower()]

# Metrics
col1, col2, col3 = st.columns(3)
col1.metric("Total Comments", len(df))
col2.metric("Filtered Count", len(filtered_df))
col3.metric("Negative Ratio", f"{len(df[df['sentiment']=='negative'])/len(df)*100:.1f}%")

# Visualization
st.subheader("Sentiment Distribution")
fig, ax = plt.subplots()
df['sentiment'].value_counts().plot(kind='bar', ax=ax, color=['red', 'gray', 'green'])
st.pyplot(fig)

# Data Table
st.subheader("Filtered Comments")
st.dataframe(filtered_df[['clean_comment', 'sentiment']].head(100))
