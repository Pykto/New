import streamlit as st

st.write("""
# My first app
Hello world!*""")


if st.button('Say hello'):
    st.write('Why hello there')
else:
    st.write('Goodbye')
    
st.write("El pablo")
