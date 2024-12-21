import streamlit as st
st.title("Gross app calculator")
bsal=st.number_input("enter your salary")
if st.button("Calculate gross salary"):
    hra=0
    da=0
if bsal<10000:
    hra = 0.67 * bsal
    da = 0.73 * bsal
elif bsal<20000 :
    hra=0.69*bsal
    da = 0.76*bsal

else:
    hra = 0.73*bsal
    da = 0.89*bsal
gs = hra + da + bsal
st.success(f"gross salary is {gs}")

st.html("""
<h1>hi</h1>
<input></input>

""")