import streamlit as st

st.title("Roteiro 1: Primeiros Passos com Streamlit")
label= 'Digite algo aqui:'
frase = st.text_input(label, value="", max_chars=None, key=None, type="default")

if st.button("Clique-me"):
    st.write(frase)
