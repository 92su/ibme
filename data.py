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

st.set_page_config(layout='wide',initial_sidebar_state='expanded')

with open ('style.css') as f:
    st.markdown(f'<style>{f.read()}</style>',unsafe_allow_html=True)


st.title('Research published in international journals')


st.sidebar.subheader('Upload Excel File')
uploaded_file = st.sidebar.file_uploader("Choose a XLSX file", type="xlsx")
if uploaded_file:
    df = pd.read_excel(uploaded_file,sheet_name=1)
    st.dataframe(df)
    #st.table(df)
    #print(df)


    st.header('Number of Publication')
    st.bar_chart(df, x="academicyear", y=["Quartile1","Quartile2","Quartile3","Quartile4"])

# sidebar - year selection
    st.sidebar.subheader('Pie Chart Filter Data ')
    sorted_year = sorted(df.academicyear.unique())
    selected_year = st.sidebar.multiselect('Academic Year',sorted_year,sorted_year)

    sorted_paper = sorted(df.TotalPaper.unique())
    selected_paper = st.sidebar.multiselect('Total Paper',sorted_paper,sorted_paper)

    df_selected_year = df[(df.academicyear.isin(selected_year)) & (df.TotalPaper.isin(selected_paper))]

    st.header('Display Year')
    st.write('Data:'+str(df_selected_year.shape[0])+'rows and'+ str(df_selected_year.shape[1])+ ' columns.')
    st.dataframe(df_selected_year)

    #chart_data = pd.DataFrame(columns=['Academic Year','TotalPaper'])
    #st.bar_chart(chart_data)

    df_grouped = (df.groupby(by=["academicyear"]).count()[["Quartile1"]].sort_values(by="Quartile1"))


    pie_chart = px.pie(df_selected_year,title="Number of Publication",values='TotalPaper',names='academicyear')

    st.plotly_chart(pie_chart)
