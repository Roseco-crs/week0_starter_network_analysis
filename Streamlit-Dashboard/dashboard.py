import streamlit as st
import pandas as pd
import numpy as np
from src.loader import SlackDataLoader
import src.loader as loader
import src.utils as utils
import os, sys


p = os.path.abspath('../Streamlit-Dashboard/data2.csv')
pp = os.path.abspath('../Streamlit-Dashboard/dataf.csv')


st.markdown('# Slack Message Analysis')
st.markdown('#### Project Description')
st.markdown("The purpose of this analysis is to understand data, answer usefull questioons")

st.markdown("#### Load Data-1")
df1 = pd.read_csv(p)
st.write(df1)

st.markdown("#### Load Data-2")

df2 = pd.read_csv(pp)
st.write(df2)








