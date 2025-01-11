# Core Streamlit Imports
import streamlit as st

# Data Manipulation
import pandas as pd
import numpy as np

# Visualization
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px

# Machine Learning (if needed)
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error

# Database Interaction (if needed)
from sqlalchemy import create_engine # type: ignore

# API Interaction (if needed)
import requests

st.title("Essential Python Libraries for Analysts, Scientists, and Engineers")
image_path_python = "/c/Users/Sloan/Documents/Github/Streamlit_Series/pythoncloud.jpg"
st.image(image_path_python, use_column_width=True)
st.write("Welcome to the Essential Python Libraries for Analysts, Scientists, and Engineers! This is a Streamlit app that showcases the most important Python libraries for data analysis, visualization, and machine learning. The libraries that will be covered in this app are: Pandas, NumPy, Matplotlib, Seaborn, Plotly, and Scikit-Learn. Each library will have its own section where we will explore the most important features and functions. Let's get started!")


st.title("Essential Libaries for Data Analysts")
image_path_analyst = "/c/Users/Sloan/Documents/Github/Streamlit_Series/data-analyst1.jpg"
st.image(image_path_analyst, use_column_width=True)

st.subheader("Pandas")

st.subheader("NumPy")

st.subheader("Matplotlib")

st.subheader("Seaborn")

st.subheader("openpyxl")


st.title("Essential Libaries for Data Scientists")
image_path_science = "/c/Users/Sloan/Documents/Github/Streamlit_Series/DS.png"
st.image(image_path_science, use_column_width=True)

st.subheader("Pandas")

st.subheader("NumPy")

st.subheader("scikit-learn & Statsmodels & keras")

st.subheader("TensorFlow & PyTorch ")

st.subheader("NLTK")


st.title("Essential Libaries for Analytics Engineers/ML Engineers")
image_path_analytics = "/c/Users/Sloan/Documents/Github/Streamlit_Series/Aeng.png"
st.image(image_path_analytics, use_column_width=True)

st.markdown("To avoid redundency, Pandas and Numpy are not listed here.")

st.subheader("scikit-learn & Statsmodels & keras")

st.subheader("TensorFlow & PyTorch ")

st.subheader("Airflow")

st.subheader("Dask")

st.subheader("MLflow")


st.title("Essential Libaries for Data Engineers")
image_path_engineer = "/c/Users/Sloan/Documents/Github/Streamlit_Series/Engineers.jpg"
st.image(image_path_engineer, use_column_width=True)

st.markdown("To avoid redundency, Pandas and Numpy are not listed here.")

st.subheader("SQLAlchemy")

st.subheader("Airflow")

st.subheader("PySpark")

st.subheader("Dask")

st.subheader("FastAPI")

st.subheader("Pyarrow")