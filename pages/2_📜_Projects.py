import streamlit as st
from streamlit_lottie import st_lottie
import requests

st.set_page_config(page_title="My Projects!", page_icon=":shark:", layout="wide")

def load_image(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()



st.title("Projects")
lottie_file_2 = load_image("https://assets3.lottiefiles.com/datafiles/NI3H6lEUzvyyknU/data.json")
lottie_file_3 = load_image("https://assets2.lottiefiles.com/packages/lf20_8CeqKMzpWz.json")
lottie_file_4 = load_image("https://assets5.lottiefiles.com/packages/lf20_iwmd6pyr.json")
lottie_file_5 = load_image("https://assets10.lottiefiles.com/packages/lf20_6ft9bypa.json")
with st.container():
    st.write("----")
    st.header("My Projects")
    image_c, text_c = st.columns((1,2))
    with text_c:
        st.subheader(":blue[Blackjack in Java]")
        st.write(
            """
            - The popular card game built using Object-Oriented Programming.\n
            - Utilized Card, Deck, and Player classes to build the main program.
            """)
        st.markdown("[View Project](https://github.com/rishp66/blackjack)")
        st.caption("----------------------------------------------------")
        st.subheader(":blue[Linux Videogame]")
        st.write(
            """
            - Utitlized a Bash Script to automate a videogame utilizing Bash commands.\n
            - Reads user input as a command to test whether their command was correct against the videogame.
            """)
        st.markdown("[View Project](https://github.com/rishp66/Linux-Game)")
        st.caption("----------------------------------------------------")
        st.subheader(":blue[Analysis of the Pokédex using R]")
        st.write(
            """
            - A complete analysis of the Pokédex using p-values, hypothesis-testing, and data visualization.\n
            - Completed by using R's library of ggplot2 and dplyr.
            """)
        st.markdown("[View Project](https://github.com/rishp66/Pokedex_Analysis)")
        st.caption("----------------------------------------------------")
        st.subheader(":blue[An Equation Solver]")
        st.write(
            """
            - Utilized Point, Rational, and Line classes to solve an equation utilizing OOP.  
            """)
        st.markdown("[View Project](https://github.com/rishp66/system-of-equations)")
        with image_c:
            st_lottie(lottie_file_2, height=200,width=350, key="blackjack")
            st_lottie(lottie_file_3, height=200,width=200, key="scripting")
            st_lottie(lottie_file_4,height=200,width=150, key="pokemon")
            st_lottie(lottie_file_5,height=200,width=150, key="solving")

