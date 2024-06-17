import pandas as pd
import plotly.express as px
import streamlit as st

st.header('Histogrmas de Vehículos')
car_data = pd.read_csv("../vehicles_us.csv")  # leer los datos
hist_button = st.button('Construir histograma')  # crear un botón
# Crear un botón para el gráfico de dispersión
scatter_button = st.button('Construir gráfico de dispersión')

if hist_button:  # al hacer clic en el botón
    # escribir un mensaje
    st.write(
        'Creación de un histograma para el conjunto de datos de anuncios de venta de coches')

    # crear un histograma
    fig = px.histogram(car_data, x="odometer")

    # mostrar un gráfico Plotly interactivo
    st.plotly_chart(fig, use_container_width=True)

if scatter_button:  # Al hacer clic en el botón del gráfico de dispersión
    st.write('Creación de un gráfico de dispersión para el conjunto de datos de anuncios de venta de coches')
    # Crear un gráfico de dispersión
    fig = px.scatter(car_data, x="odometer", y="price",
                     title="Gráfico de dispersión: Odómetro vs. Precio")
    # Mostrar un gráfico Plotly interactivo
    st.plotly_chart(fig, use_container_width=True)
