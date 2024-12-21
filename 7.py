import streamlit as st
st.title("Gross Salary Calculator")
bs=st.number_input("Enter your Basic Salary:",min_value=0,step=1)

if st.button("Calculate Gross Salary"):
    hra=0
    da=0

    if bs < 10000:
        hra = bs * 0.67
        da = bs * 0.73
    elif bs <= 20000:
        hra = bs * 0.69
        da = bs * 0.76
    else:
        hra = bs * 0.73
        da = bs * 0.89

gs = bs + hra + da
st.success(gs)