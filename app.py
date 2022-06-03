import streamlit as st

import numpy as np
import pandas as pd
import seaborn as sns

st.set_page_config(
    page_title="Streamlit",  # => Quick reference - Streamlit
    page_icon="🐍",
    layout="centered",  # wide
    initial_sidebar_state="auto")  # collapsed

st.markdown("""# This is a header
## This is a sub header
This is text""")

df = pd.DataFrame({
    'first column': list(range(1, 11)),
    'second column': np.arange(10, 101, 10)
})

# this slider allows the user to select a number of lines
# to display in the dataframe
# the selected value is returned by st.slider
line_count = st.slider('Select a line count', 1, 10, 3)

# and used in order to select the displayed lines
head_df = df.head(line_count)

head_df

col1, col2, col3 = st.columns(3)
col1.metric("SPDR S&P 500", "$437.8", "-$1.25")
col2.metric("FTEC", "$121.10", "0.46%")
col3.metric("BTC", "$46,583.91", "+4.87%")

st.latex(r'''
a + ar + a r^2 + a r^3 + \cdots + a r^{n-1} =
\sum_{k=0}^{n-1} ar^k =
a \left(\frac{1-r^{n}}{1-r}\right)
''')

direction = st.radio('Select a direction', ('top', 'right', 'bottom', 'left'))

st.write(direction)

if direction == 'top':
    st.write('🔼')
elif direction == 'right':
    st.write('▶️')
elif direction == 'bottom':
    st.write('🔽')
else:
    st.write('◀️')


@st.cache
def get_dataframe_data():

    return pd.DataFrame(np.random.randn(10, 5),
                        columns=('col %d' % i for i in range(5)))


df = get_dataframe_data()

cm = sns.color_palette("coolwarm_r", as_cmap=True)
df = df.head().style.background_gradient(cmap=cm)

st.write(df)


@st.cache
def get_line_chart_data():

    return pd.DataFrame(np.random.randn(20, 3), columns=['a', 'b', 'c'])


df = get_line_chart_data()

st.line_chart(df)

CSS = """
h1 {
    color: red;
}
.stApp {
    background-image: url(https://avatars1.githubusercontent.com/u/9978111?v=4);
    background-size: cover;
}
"""

if st.checkbox('Inject CSS'):
    st.write(f'<style>{CSS}</style>', unsafe_allow_html=True)
