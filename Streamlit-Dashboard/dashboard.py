import streamlit as st
import pandas as pd
import numpy as np
# from src.loader import SlackDataLoader
# import src.loader as loader
#import src.utils as utils
import os, sys
import matplotlib.pyplot as plt
import plotly.express as px

@st.cache
def load_data():
    pp = os.path.abspath('../Streamlit-Dashboard/dataf.csv')
    df2 = pd.read_csv(pp)
    return df2

# p = os.path.abspath('../Streamlit-Dashboard/data2.csv')
# pp = os.path.abspath('../Streamlit-Dashboard/dataf.csv')

st.markdown('# Slack Message Analysis')
st.markdown('#### Project Description')
st.markdown("The purpose of this analysis is to understand data, answer usefull questioons")

dataa = load_data()
st.write(dataa)

st.markdown('#### Histogramme of essage sender name')
fig = px.histogram(dataa, y='sender_name', color=None)

st.plotly_chart(fig)

