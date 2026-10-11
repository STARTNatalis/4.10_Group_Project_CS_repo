import streamlit as st

st.title('Budget Basket 🛒')

st.write('Compare supermarket prices and find the best deals in Switzerland!')

product = st.text_input("What product are you looking for?")

if product:
    st.write("You are searching for:", product)