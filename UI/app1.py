import streamlit as st
from random import choice

st.title("Name generator")

fnames = ['Alex', 'Bob', 'Charlie', 'David']


lnames = [ 'Anderson', 'Baker', 'clark', 'Davis']

btn = st.button("Generate name")
if btn:
    fn = choice(fnames)
    ln = choice(lnames)
    fullname = f"{fn} {ln}"
    st.success(fullname)

# streamlit run UI/app1.py