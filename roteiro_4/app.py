import streamlit as st
import requests

st.title("Roteiro 4: Integração com APIs")

pais = st.text_input("Digite o nome de um país em inglês:")
infos = st.button("Clique para mais informações sobre esse país")

if infos:
    r = requests.get(f'https://restcountries.com/v3.1/name/{pais}')

    # st.write(r.json())
    st.write('***Nome comum:***')
    st.write(r.json()[0]['name']['common'])

    st.write('***Nome oficial:***')
    st.write(r.json()[0]['name']['official'])

    st.write('***Capital:***')
    st.write(r.json()[0]['capital'][0])

