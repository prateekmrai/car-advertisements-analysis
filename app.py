import streamlit as st
import pandas as pd
import plotly.express as px

# Title of the app
st.title('Car Advertisements Analysis')

# Load the dataset
df = pd.read_csv('vehicles_us.csv')

# Display the dataframe
st.header('Dataset Overview')
st.write(df.head())

# Plot a histogram
st.header('Price Distribution')
fig_hist = px.histogram(df, x='price')
st.plotly_chart(fig_hist)

# Plot a scatter plot
st.header('Odometer vs Price')
fig_scatter = px.scatter(df, x='odometer', y='price')
st.plotly_chart(fig_scatter)

# Checkbox to filter data
if st.checkbox('Show only cars with price less than $20,000'):
    df = df[df['price'] < 20000]
    st.write(df)
