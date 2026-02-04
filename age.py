import streamlit as st 
st.title("Age & City")
age = st.slider("Enter Your Age: ",1,100)
city = st.selectbox("Select Your City: ",["Mumbai","Delhi","Chennai","Goa"])
if st.button("submit"):
    st.write("Your Age: ",age)
    st.write("Your City: ",city)
    