import pandas as pd
import plotly.express as px
import streamlit as st
        
car_data = pd.read_csv('vehicles_us.csv') # leer los datos

st.header('Encabezado del Proyecto del Sprint05')
st.write(car_data.head(5))
f1=(car_data['condition']== "good").sum()
st.write(f'La cantidad de autos en buenas condiciones son: {f1} de los 51,525 en la base de datos')

modelo = car_data.groupby('model').size().reset_index(name='count')
st.write(modelo)

top_10_modelos = modelo.sort_values(by='count', ascending=False).head(10)

fig = px.bar(top_10_modelos, x='model', y='count', color='model', labels={'model': 'Modelo', 'count': 'Cantidad'},title='Top 10 Modelos Más Frecuentes')

# Mostrar la figura
st.plotly_chart(fig, use_container_width=True)

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