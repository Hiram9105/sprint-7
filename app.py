import streamlit as st
import pandas as pd
import plotly.express as px

# Título de la aplicación
st.header('Aplicación de Análisis de Datos de Vehículos')

# Leer los datos del archivo CSV
try:
    df = pd.read_csv('vehicles_us.csv')
except FileNotFoundError:
    st.error("El archivo 'vehicles_us.csv' no se encontró. Asegúrate de que esté en el mismo directorio que app.py.")
    st.stop()

# Crear un botón para generar el histograma
hist_button = st.button('Construir histograma de odómetro')

if hist_button:
    st.write('Creación de un histograma para la columna odómetro del conjunto de datos.')
    # Crear un histograma con Plotly Express
    fig = px.histogram(df, x="odometer", title="Distribución del Odómetro")
    # Mostrar el gráfico Plotly en Streamlit
    st.plotly_chart(fig, use_container_width=True)

# Crear un botón para generar el gráfico de dispersión
scatter_button = st.button('Construir gráfico de dispersión')

if scatter_button:
    st.write('Creación de un gráfico de dispersión para visualizar la relación entre odómetro y precio.')
    # Crear un gráfico de dispersión con Plotly Express
    fig_scatter = px.scatter(df, x="odometer", y="price", title="Odómetro vs. Precio")
    # Mostrar el gráfico Plotly en Streamlit
    st.plotly_chart(fig_scatter, use_container_width=True)
