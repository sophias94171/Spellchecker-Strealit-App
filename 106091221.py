from gc import callbacks
import streamlit as st
from annotated_text import annotated_text
import Spellchecker as sp



def callback1():
    st.session_state.text = st.session_state.selectbox
def callback2():
    st.session_state.text = st.session_state.text

st.title("Spellchecker")
st.subheader('by Sophia Yang')

with st.sidebar:
    checkbox = st.checkbox("Show original word", key = 'checkbox')

selectbox = st.selectbox("Choose a word or ...", ['apple','lamon','speling','hapy','language','greay','sussuss'] ,on_change = callback1 ,key = 'selectbox')

text = st.text_input('Type your own!!',value='', on_change = callback2, key = 'text')

if checkbox:
    st.write('Original word: ', text)

if text:
    if sp.correction(text) == text:
        annotated_text(
            (sp.correction(text) + ' is the correct spelling!', '', '#afa')
        )
    else:
         annotated_text(
            ( 'Correction: ' + sp.correction(text), '', '#faa')
        )


# st.session_state

