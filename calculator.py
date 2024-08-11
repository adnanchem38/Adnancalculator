import streamlit as st

# Set the title of the app
st.title("Simple Calculator")

# Input fields for the two numbers
num1 = st.number_input("Enter the first number", value=0.0)
num2 = st.number_input("Enter the second number", value=0.0)

# Operation selection
operation = st.selectbox("Select Operation", ("Addition", "Subtraction", "Multiplication", "Division"))

# Perform the calculation based on the operation selected
if operation == "Addition":
    result = num1 + num2
elif operation == "Subtraction":
    result = num1 - num2
elif operation == "Multiplication":
    result = num1 * num2
elif operation == "Division":
    if num2 != 0:
        result = num1 / num2
    else:
        st.error("Cannot divide by zero")
        result = None

# Display the result
if result is not None:
    st.write(f"The result of {operation} is: {result}")



