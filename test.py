"""Minimal check: load the data and show the dataframe."""

import streamlit as st

from lab_helpers import load_data

st.markdown(
    "<h1 style='text-align: center; color: red;'>Welcome to my Dashboard!</h1>",
    unsafe_allow_html=True,
)

st.markdown(
    "This is the "
    "[Breast Cancer Wisconsin (Diagnostic)]"
    "(https://archive.ics.uci.edu/dataset/17/breast-cancer-wisconsin-diagnostic) "
    "dataset from the UCI Machine Learning Repository."
)

data = load_data()

st.dataframe(data["exploration"])
