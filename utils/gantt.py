import pandas as pd
import plotly.express as px
import streamlit as st

def render_gantt(tasks):
    df = pd.DataFrame(tasks)
    fig = px.timeline(df, x_start="Start", x_end="End", y="Task", color="Task")
    fig.update_yaxes(categoryorder="total ascending")
    st.plotly_chart(fig, use_container_width=True)
