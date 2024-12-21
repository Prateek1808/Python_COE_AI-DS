import streamlit as st
st.title("this is simple app")
num1=st.number_input("enter number",min_value=1,step=1)
if st.button("even/odd"):
    if num1%2==0:
        st.success("even no")
    else:
        st.error("odd no")
st.color_picker("pick a color")