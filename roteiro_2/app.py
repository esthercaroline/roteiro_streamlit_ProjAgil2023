import streamlit as st
st.set_page_config(page_title="Roteiro 2: Widgets Interativos")


with st.container():
    st.subheader("Streamlit da teté")
    st.title("Roteiro 2: Widgets Interativos")

    value = st.slider("Escolha um valor", 0, 100)

    checkbox =  st.checkbox('Cliquei!')
    opcoes =  st.radio('Escolha uma opção', ['Teté é linda', 'Teté é legal', 'Teté é inteligente', 'All the above'])
    choice = st.selectbox('Escolha uma opção', ['Quero dormir', 'Quero aprender cálculo', 'Quero aprender sql', 'All the above'])
    selected = st.toggle('Teté é genial?')
    if st.button("Mostrar valor do slider"):
        st.write(f"Valor escolhido: {value}")
        if checkbox:
            st.write('Checkbox marcado!')

        if selected:
            st.write('Sim! Você sabe que eu sou genial!')
        if not selected:
            st.write('VOU TE CAÇAR!')
        if choice == 'All the above':
            st.write('Todas as opções marcadas!')
        else:
            st.write(f'Opção escolhida: {choice}, afff!')
        if opcoes == 'All the above':
            st.write('Todas as opções marcadas!')
        else:
            st.write(f'Opção escolhida: {opcoes}, mas eu já sabia!')

    

    st.write('---')

   

 