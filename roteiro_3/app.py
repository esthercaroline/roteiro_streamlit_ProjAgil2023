import streamlit as st

st.title("Roteiro 3: Chilling - Página 1")


st.sidebar.title("Menu")
st.sidebar.write('[Spotify](https://open.spotify.com/collection/tracks) - Lets listen to some tunes')
st.sidebar.write('[Netflix](https://www.netflix.com/browse) - Lets watch some movies')
st.sidebar.write('[Youtube](https://www.youtube.com/) - Lets watch some videos')
st.sidebar.write('[Página 2](http://localhost:8502/)')


tab1, tab2, tab3, tab4 = st.tabs(["Tasks", "Groceries", "Reminders", 'Journal'])

with tab1:
    st.write("This is the Tasks tab")
    with st.expander("Task 1"):
        st.write("Call a repairing service for your computer")

with tab2:
    st.write("This is the Groceries tab")
    container_groceries = st.container()
    container_groceries.write(" ***Buy some Sensação***")
    container_groceries.write("Buy some Oatmeal")

    
