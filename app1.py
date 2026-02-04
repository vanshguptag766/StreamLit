import streamlit as st 
st.title("Simple Iinput App")
name = st.text_input("Enter Your Name: ")
if st.button("submit"):
    st.write("helloooo ",name)