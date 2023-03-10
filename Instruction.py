import streamlit as st
import pandas as pd
from io import StringIO
# st.snow()
import streamlit as st
import time

progress_text = "Loading Instruction. Please wait."
my_bar = st.progress(0, text=progress_text)

for percent_complete in range(100):
    time.sleep(0.1)
    my_bar.progress(percent_complete + 1, text=progress_text)

st.title("Experense Tarcko")
st.subheader("Steps to follow , if you want this to work!")
st.write("1. Go to https://takeout.google.com/")
st.write("2. Deselect all the selected items except 'GPAY' data.")
st.write("3. Let the data be download")
st.write("4. Now extract the data and upload in the Data_Showing section ")
st.write("5. Make sure to upload the My Activity.html - path for the file will be downloads/takeout(filename)/Google Pay/My Activity/My Activity.html")
st.write("6. After uploading , download the changed file")
st.write("7. Wait for the Analysis to finish")
st.write("8. Horrayy!! CSV file is generated ")