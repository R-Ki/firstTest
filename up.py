import streamlit as st

def add_numbers(a, b):
    return a + b

st.title("Simple Calculator")

# ユーザー入力
num1 = st.number_input("Enter first number", value=0)
num2 = st.number_input("Enter second number", value=0)

if st.button("Add"):
    result = add_numbers(num1, num2)
    st.write(f"The result is {result}")