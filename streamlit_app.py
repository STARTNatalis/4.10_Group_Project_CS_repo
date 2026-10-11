import streamlit as st

# Budget Basket - First Version

st.title('Budget Basket 🛒')

st.write('Compare supermarket prices and find the best deals!')

# 1. Our product data

product = st.text_input("What product are you looking for?")

if product:
    st.write("You are searching for:", product)


 # 2. Let the user choose a product

 # 3. Display prices for the selected product

 # 4. Find the cheapest supermarket

 # 5. Calculate potential savings