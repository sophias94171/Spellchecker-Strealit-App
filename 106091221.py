import streamlit as st

st.title("Spellchecker")
with st.sidebar:
    st.checkbox("Show original word")
st.selectbox("Choose a word or ...", ['apple','lamon','speling','hapy','language','greay','sussuss'])
st.text_input("Type your own!!")
