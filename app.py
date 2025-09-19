import streamlit as st
from agent import agent

st.title("🏏 AI Sports Analyst Assistant")

query = st.text_input("Ask about players, matches, or training:")
if st.button("Analyze"):
    response = agent.run(query)
    st.write(response)
