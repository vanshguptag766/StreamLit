import streamlit as st 
st.title("Simple Calculator!")
num1 = st.number_input("Enter First Number: ")
num2 = st.number_input("Enter Second Number: ")
operation = st.selectbox("Select Operation: ",["Addition","Subtraction","Division","Multiplication"])
if st.button("Calculate"):
    if operation == "Addition":
        st.write("Answer: ",num1+num2)
    elif operation == "Subtraction":
        st.write("Answer: ",num1-num2)
    elif operation == "Division":
        if num2 == 0:
            st.write("Cannot Divide By Zero")
        else:
            st.write("Answer: ",num1/num2)
    elif operation == "Multiplication":
        st.write("Answer: ",num1*num2)
    