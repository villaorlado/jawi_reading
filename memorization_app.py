import streamlit as st
import pandas as pd
import random

# Load the CSV file
@st.cache_data
def load_data():
    return pd.read_excel('rumi-jawi.xlsx')

data = load_data()

# Select a random word from column "A"
if 'current_index' not in st.session_state or st.button('Next'):
    st.session_state.current_index = random.randint(0, len(data) - 1)

current_word = data.iloc[st.session_state.current_index]['jawi']

# Display the word
st.markdown(f"<h1 style='color: black;'>{current_word}</h1>", unsafe_allow_html=True)

# Button to reveal the corresponding word in column "B"
if st.button('Rumi'):
    answer = data.iloc[st.session_state.current_index]['rumi']
    st.markdown(f"<h1 style='color: black;'>{answer}</h1>",unsafe_allow_html=True)

