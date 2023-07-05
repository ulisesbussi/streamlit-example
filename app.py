import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots
# Selección del archivo CSV
st.subheader("Selección del archivo CSV")
csv_file = st.file_uploader("Cargar archivo CSV", type=["csv"])


# Comprobar si se seleccionó un archivo CSV
if csv_file is not None:
    # Leer el archivo CSV
    df = pd.read_csv(csv_file)

    st.subheader("Gráfico Miniatura")

    #fig_miniatura = go.Figure()
    #make subplots 2 rows by 1 column
    fig = make_subplots(rows=2, cols=1, shared_xaxes=True,)
    #change figure size
    fig.update_layout(height=600, width=800, title_text="Gráfico Miniatura")
    

    fig.add_trace(go.Scatter(
        x=df['t'],
        y=df['x'],
        mode='lines',
        name='x'
    ),row=1, col=1)
    fig.add_trace(go.Scatter(
        x=df['t'],
        y=df['y'],
        mode='lines',
        name='y'
    ),row=1, col=1)

    dx = df['x'].diff()
    dy = df['y'].diff()
    dt = df['t'].iloc[0:-1]


    fig.update_xaxes(
        rangeslider_visible=True,
        range=[df['t'].iloc[0], df['t'].iloc[-1]],
        type='linear',
        row=1, col=1
    )


    fig.add_trace(go.Scatter(
        x=dt,
        y=dx,
        mode='lines',
        name='dx'
    ),row=2, col=1)

    fig.add_trace(go.Scatter(
        x=dt,
        y=dy,
        mode='lines',
        name='dy'
    ),row=2, col=1)

    
    st.plotly_chart(fig)


else:
    st.info("Cargue un archivo CSV para visualizar los datos y generar el gráfico.")