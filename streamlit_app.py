#from collections import namedtuple
#import altair as alt
#import math
import pandas as pd
import streamlit as st
import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots


"""
# Welcome to Streamlit!

Edit `/streamlit_app.py` to customize this app to your heart's desire :heart:

If you have any questions, checkout our [documentation](https://docs.streamlit.io) and [community
forums](https://discuss.streamlit.io).

In the meantime, below is an example of what you can do with just a few lines of code:
"""

st.subheader("Selección del archivo CSV")
csv_file = st.file_uploader("Cargar archivo CSV", type=["csv"])




with st.echo(code_location='below'):
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
    # total_points = st.slider("Number of points in spiral", 1, 5000, 2000)
    # num_turns = st.slider("Number of turns in spiral", 1, 100, 9)

    # Point = namedtuple('Point', 'x y')
    # data = []

    # points_per_turn = total_points / num_turns

    # for curr_point_num in range(total_points):
    #     curr_turn, i = divmod(curr_point_num, points_per_turn)
    #     angle = (curr_turn + 1) * 2 * math.pi * i / points_per_turn
    #     radius = curr_point_num / total_points
    #     x = radius * math.cos(angle)
    #     y = radius * math.sin(angle)
    #     data.append(Point(x, y))

    # st.altair_chart(alt.Chart(pd.DataFrame(data), height=500, width=500)
    #     .mark_circle(color='#0068c9', opacity=0.5)
    #     .encode(x='x:Q', y='y:Q'))
