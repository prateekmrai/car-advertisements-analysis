import streamlit as st
import pandas as pd
import plotly.express as px

# Title of the app
st.title('Car Advertisements Analysis')

# Load the dataset
df = pd.read_csv('vehicles_us.csv')

# Handle missing values for 'cylinders' column using groupby and median
if 'model' in df.columns and 'year' in df.columns:
    df['cylinders'] = df.groupby(['model', 'year'])['cylinders'].transform(lambda x: x.fillna(x.median()))
else:
    st.error("The dataset does not contain the required 'model' or 'year' columns.")

# Filter options
price_filter = st.slider('Select price range', 0, int(df['price'].max()), (0, int(df['price'].max() / 2)))
odometer_filter = st.slider('Select odometer range', 0, int(df['odometer'].max()), (0, int(df['odometer'].max() / 2)))
filtered_df = df[df['price'].between(price_filter[0], price_filter[1]) & df['odometer'].between(odometer_filter[0], odometer_filter[1])]

# Display the dataframe
st.header('Dataset Overview')
st.write(filtered_df.head())

# Plot 1: Price Distribution
st.header('Price Distribution')
fig_hist = px.histogram(filtered_df, x='price', title='Price Distribution of Car Advertisements')
fig_hist.update_layout(xaxis_title='Price', yaxis_title='Count')
st.plotly_chart(fig_hist)

# Plot 2: Odometer vs Price
st.header('Odometer vs Price')
fig_scatter = px.scatter(filtered_df, x='odometer', y='price', title='Odometer vs Price')
fig_scatter.update_layout(xaxis_title='Odometer', yaxis_title='Price')
st.plotly_chart(fig_scatter)

# Checkbox to show only cars with price less than $20,000
if st.checkbox('Show only cars with price less than $20,000'):
    filtered_df = filtered_df[filtered_df['price'] < 20000]
    st.write(filtered_df)

# Conclusion
st.header('Conclusion')
st.write('The EDA reveals insights into the distribution of car prices and their relationship with mileage. '
         'Further analysis and modeling can be performed to understand other factors influencing car prices.')
