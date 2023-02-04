import requests
import streamlit as st
from streamlit_lottie import st_lottie

st.set_page_config(page_title="My Webpage!", page_icon=":shark:", layout="wide")


def load_image(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

# Sidebar
st.sidebar.success("Select from any of the pages above.")


# --- Cloud Design for the Webpage---
lottie_file = load_image("https://assets6.lottiefiles.com/packages/lf20_lcuymkjx.json")

# ------header------
st.title("Home Page")
with st.container():
    st.header(":black[Rish Pednekar]")
    st.subheader("***IT & Data Science student @ Rutgers University (2021-2025)***")

# My Past Experiences
with st.container():
    st.write("----")
    left_c, right_c = st.columns(2)
    with left_c:
        st.header("About Me")
        st.subheader("**EXPERIENCES:**")
        st.write(
            """
            - Worked at Geek Squad ticketing 75+ items and fixing various client computer issues.
            - Volunteered at a CodeIE event to teach young kids the basics of programming in Scratch.
            - Worked as a Lifeguard for nearly 4 years to save lives.
            - Developed numerous computer programs with 5+ languages which can be viewed on my GitHub.
            - Microsoft Azure certified.
            """
        )
        st.subheader("**ASPIRATIONS:**")
        st.write(
            """
            - Work as a Cloud or DevOps Engineer!
            
            """
        )
    with right_c:
        st_lottie(lottie_file, height=400, key="coding")



