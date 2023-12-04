# pip install openpyxl
import pandas as pd
import streamlit as st
import zipfile
import base64
import os
import datetime as dt
import plotly.express as px  # pip install plotly-express
from dateutil.relativedelta import relativedelta # to add days or years
from datetime import datetime, date ,time
from PIL import Image
import matplotlib.pyplot as plt


st.title('Research published in international journals')


st.sidebar.subheader('Dashbaord for IBME')
st.sidebar.subheader('Upload Excel File')
uploaded_file = st.sidebar.file_uploader("Choose a XLSX file", type="xlsx")
if uploaded_file:
    df = pd.read_excel(uploaded_file,sheet_name=1)
    st.dataframe(df)

    #df.pivot(index='academicyear',columns='Quartile1',values='TotalPaper').plot(kind='bar')
    st.title('Number of Publication')
    st.bar_chart(df, x="academicyear", y=["Quartile1","Quartile2","Quartile3","Quartile4"])
