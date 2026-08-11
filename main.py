import streamlit as st

st.title("Interactive Streamlit App")

#Taking user input
name=st.text_input("Enter your name:")

#Displaying a message when a button is clicked
if st.button ("Submit"):
    st.write(f"Hello,{name}: Welcome to Streamlit.")
    
    st.text_input(f"Enter your command:")
#Displaying a message when a button is clicked
if st.button ("Submit"):   
    st.write(f" I'm Fine ")
    
