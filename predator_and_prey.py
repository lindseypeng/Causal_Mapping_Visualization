import streamlit as st
import numpy as np
import pandas as pd
import altair as alt
from scipy.integrate import odeint
## run streamlit run predator_and_prey.py to see dashboard
# Function for Lotka-Volterra equations
def deriv(y, t, a, b, c, d):
    R, F = y
    dRdt = a * R - b * R * F
    dFdt = c * R * F - d * F
    return [dRdt, dFdt]

# Introduction section
st.title('Lotka-Volterra Equations')
st.markdown("""
The **Lotka-Volterra equations**, also known as the predator-prey equations, are a pair of first-order, non-linear, differential equations frequently used to describe the dynamics of biological systems in which two species interact, one as a predator and the other as prey.

The equations are given by: """)
            
st.latex(r'''
\begin{align*}
\frac{dR}{dt} &= aR - bRF \\
\frac{dF}{dt} &= cRF - dF
\end{align*}''')

st.markdown("""
Where:
- \( R \) is the number of prey (e.g., rabbits)
- \( F \) is the number of predators (e.g., foxes)
- \( a \) is the natural growth rate of prey in the absence of predators
- \( b \) is the death rate of prey due to predation
- \( c \) is the growth rate of predators per prey eaten
- \( d \) is the natural death rate of predators in the absence of prey
""")

# Streamlit sidebar for user input
st.sidebar.header('Model Parameters')
a = st.sidebar.slider('Natural growth rate of rabbits (a)', 0.0, 2.0, 1.0)
b = st.sidebar.slider('Death rate of rabbits due to predation (b)', 0.0, 1.0, 0.1)
c = st.sidebar.slider('Growth rate of foxes due to predation (c)', 0.0, 1.0, 0.1)
d = st.sidebar.slider('Natural death rate of foxes (d)', 0.0, 2.0, 1.0)

# Initial conditions
R0 = st.sidebar.slider('Initial rabbit population (R0)', 1, 100, 10)
F0 = st.sidebar.slider('Initial fox population (F0)', 1, 100, 5)
y0 = [R0, F0]

# Time points
t = np.linspace(0, 50, 500)

# Integrate the equations over the time grid
solution = odeint(deriv, y0, t, args=(a, b, c, d))
R, F = solution.T

# Create a DataFrame for Altair
data = pd.DataFrame({
    'Time': t,
    'Rabbits': R,
    'Foxes': F
}).melt('Time', var_name='Population Type', value_name='Population')

# Altair plot
chart = alt.Chart(data).mark_line().encode(
    x='Time',
    y='Population',
    color='Population Type'
).properties(
    title='Rabbits and Foxes Population Dynamics',
    width=700,
    height=400
).interactive()

# Display the plot in Streamlit
st.altair_chart(chart)
