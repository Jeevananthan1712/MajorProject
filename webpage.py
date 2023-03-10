import streamlit as st
import pandas as pd

@st.cache
def convert_df(df):
    # IMPORTANT: Cache the conversion to prevent computation on every rerun
    return df.to_csv().encode('utf-8')

st.write("Money Send/paid and Received Data ")
df = pd.read_csv("Data.csv")
dff = pd.read_csv("MoneyData.csv")
# st.line_chart(df)
st.write(df)
csvdata = convert_df(dff)
st.download_button(
    label="Download data as CSV",
    data=csvdata,
    file_name='Data.csv.csv',
    mime='text/csv',
)
st.write("Category Wise Distribution ")
st.write(dff)

csv = convert_df(dff)
st.download_button(
    label="Download data as CSV",
    data=csv,
    file_name='MoneyData.csv.csv',
    mime='text/csv',
)
# st.bar_chart(dff)
