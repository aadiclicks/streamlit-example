from collections import namedtuple
import altair as alt
import math
import pandas as pd
import streamlit as st

my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
st.dataframe(my_fruit_list)
