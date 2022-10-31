from gc import callbacks
import streamlit as st
import Spellchecker as sp

def callback1():
    st.session_state.text = st.session_state.selectbox
def callback2():
    st.session_state.text = st.session_state.text

st.title("Spellchecker")
with st.sidebar:
    checkbox = st.checkbox("Show original word", key = 'checkbox')

selectbox = st.selectbox("Choose a word or ...", ['apple','lamon','speling','hapy','language','greay','sussuss'] ,on_change = callback1 ,key = 'selectbox')

text = st.text_input('Type your own!!',value='', on_change = callback2, key = 'text')


if text:
    st.write(sp.correction(text))

if checkbox:
    st.write('Original word: ', text)

st.write(st.session_state)
