import streamlit as st
st. title("My first app")
name = st.text_input("Как се казваш")
st.write(f"Здравей, {name}")
