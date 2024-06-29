import pandas as pd
import plotly.express as px
import streamlit as st
        
car_data = pd.read_csv('C:\\Users\\osval\\intento_4\\vehicles_us.csv') # leer los datos

st.header('Encabezado del Proyecto del Sprint05')

hist_button = st.button('Construir histograma') # crear un botón
        
if hist_button: # al hacer clic en el botón
            # escribir un mensaje
    st.write('Creación de un histograma para el conjunto de datos de anuncios de venta de coches')
            
            # crear un histograma
    fig = px.histogram(car_data, x="odometer")
        
            # mostrar un gráfico Plotly interactivo
    st.plotly_chart(fig, use_container_width=True)


disp_boton = st.button('Gráfica de Dispersión')

if disp_boton:
    st.write('Se crea el grafico de dispersión')

    fig = px.scatter(car_data, x="odometer", y="price")

    st.plotly_chart(fig, use_container_width=True)

construye_histo = st.checkbox('Histograma')

if construye_histo:
    st.write('Histograma de odómetro')
            # crear un histograma
    fig = px.histogram(car_data, x="odometer")
            # mostrar un gráfico Plotly interactivo
    st.plotly_chart(fig, use_container_width=True)

disp_construye = st.checkbox('Dispersion')

if disp_construye:
    st.write('Dispersion de odómetro')
            # crear un histograma
    fig = px.scatter(car_data, x="odometer")
            # mostrar un gráfico Plotly interactivo
    st.plotly_chart(fig, use_container_width=True)