# Contact Form
import streamlit as st
import requests
from streamlit_lottie import st_lottie

st.title("Contact")
link_icon = "https://www.keesingtechnologies.com/wp-content/uploads/2018/07/Linkedin-Icon.png"
linked_in = "https://www.linkedin.com/in/rish-pednekar/"
git_icon = "https://image.freepik.com/free-icon/github-logo-black-shape_318-52922.jpg"
git_hub = "https://github.com/rishp66"

with st.container():
    st.write("---")
    st.write("##")
    st.markdown(
        f"""<a href={linked_in}><img src={link_icon} alt="drawing" width="100"/></a>""",
        unsafe_allow_html=True,
    )
    st.markdown(
        f"""<a href={git_hub}><img src={git_icon} alt="drawing" width="100"/></a>""",
        unsafe_allow_html=True,
    )