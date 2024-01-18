import streamlit as st
st.title ("webpage interface using streamlit")

name = st.text_input("Enter your Name:")
Fname = st.text_input("Enter your Father Name:")
Address = st.text_area("Enter you Text: ")
classdata = st.selectbox("Enter your class :" ,(1,2,3,4,5,6,7,8))


button = st.button("Done")

if button:
    st.markdown(f""" 
                Name: {name}
                Father Name: {Fname}
                Address: {Address}
                class: {classdata}
                """)