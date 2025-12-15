import streamlit as st
import pandas as pd
import plotly_express as px
from pathlib import Path

st.header('Análisis de Datos de Vehículos')

# Construir la ruta absoluta al archivo CSV
csv_path = Path(__file__).parent / 'vehicles_us.csv'

df_vehicles = pd.read_csv(csv_path) # leer los datos
st.dataframe(df_vehicles) # mostrar el dataframe


if st.button('Construir histograma'):
    st.write('Creando un histograma para la columna odómetro')
    # Crear un histograma con Plotly Express
    fig = px.histogram(df_vehicles, x="odometer")
    # Mostrar el gráfico en Streamlit
    st.plotly_chart(fig, use_container_width=True)

if st.button('Construir gráfico de dispersión'):
    st.write('Creando un gráfico de dispersión para precio vs. año del modelo')
    # Crear un gráfico de dispersión
    fig = px.scatter(df_vehicles, x="model_year", y="price")
    # Mostrar el gráfico
    st.plotly_chart(fig, use_container_width=True)