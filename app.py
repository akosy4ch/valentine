import streamlit as st
import plotly.graph_objects as go
import plotly.express as px
import numpy as np
import pandas as pd

def get_zvalue(a, b, x, y):
    constant = x ** 2 + ((1 + b) * y) ** 2 - 1
    c0 = constant ** 3
    c1, c5 = 0.0, 0.0
    c2, c4 = 3 * (constant ** 2), 3 * constant
    c3 = -(a * (y ** 2) + x ** 2)
    c6 = 1.0

    coefficients = [c6, c5, c4, c3, c2, c1, c0]
    rts = np.roots(coefficients)
    z = rts[~np.iscomplex(rts)]
    return z.real if len(z) > 0 else []

def draw_heart(a=9/200, b=0.01, grid=0.10, palette='reds'):
    x = np.arange(-2, 2, grid)
    y = x
    all_triplets = []

    for i in x:
        for j in y:
            zaxis = get_zvalue(a, b, i, j)
            for k in zaxis:
                all_triplets.append([i, j, k])

    results = np.array(all_triplets).T
    df = pd.DataFrame({'x': results[0], 'y': results[1], 'z': results[2]})

    fig = px.scatter_3d(df, x='x', y='y', z='z', color='z', color_continuous_scale=palette)
    
    fig.update_layout(title="💖 Спишь? Это я, Алибек, узнала? 💖", template="plotly_white")
    return fig

# Streamlit App
st.title("💖 Будь моей валентинкой Амика 💖")

# Dropdown menu to choose the color
palette_choice = st.selectbox("Выбери цвет сердца:", ["reds", "pinkyl", "magma"])

# Display the heart with the selected color
st.plotly_chart(draw_heart(palette=palette_choice))
