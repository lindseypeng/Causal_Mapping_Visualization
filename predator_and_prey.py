
import time  # to simulate a real time data, time loop

import numpy as np  # np mean, np random
import pandas as pd  # read csv, df manipulation
import streamlit as st  # 🎈 data web app development
from scipy.integrate import odeint
import altair as alt

# Lotka-Volterra equations
def deriv(y, t, a, b, c, d):
    R, F = y
    dRdt = a * R - b * R * F
    dFdt = c * R * F - d * F
    return [dRdt, dFdt]

st.set_page_config(
    page_title="Predator and prey",
    page_icon="✅",
    layout="wide",
)

# dashboard title
st.title("Lotka-Volterra Dashboard")
# Parameters
a = st.slider('Prey Growth Rate', min_value=1, max_value=10, value=5, step=0.1)
b = st.slider('Prey Death Rate', min_value=1, max_value=10, value=5, step=0.1)
c = st.slider('Predator Growth Rate', min_value=1, max_value=10, value=5, step=0.1)
d = st.slider('Predator Death Rate', min_value=1, max_value=10, value=5, step=0.1)

R0 = st.number_input('Initial Prey Number', min_value=1, max_value=10, value=5, step=0.1)
F0 = st.number_input('Initial Predator Number', min_value=1, max_value=10, value=5, step=0.1)

y0 = [R0, F0]
# Time points where we want the solution
t = np.linspace(0, 50, 500)

# Integrate the equations over the time grid, t.
solution = odeint(deriv, y0, t, args=(a, b, c, d))
R, F = solution.T

#
predator = pd.DataFrame({
  'x': t,
  'f(x)': R
})

prey = pd.DataFrame({
  'x': t,
  'f(x)': R
})


alt.Chart(pd.).mark_line().encode(
    x='x',
    y='f(x)'
)