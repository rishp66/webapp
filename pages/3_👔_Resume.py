from pathlib import Path

import streamlit as st
from PIL import Image

current_dir = Path(__file__).parent if "__file__" in locals() else Path.cwd()
css = current_dir / "styles" / "main.css"
resume = current_dir / "assets" / "Resume_Rish_Pednekar.pdf"
profile_pic = current_dir / "assets" / "profile-pic.png"



# titles
PAGE_TITLE = "Resume | Rish Pednekar"
PAGE_ICON = ":wave:"
NAME = "Rish Pednekar"
DESCRIPTION = "An IT & Data Science Student at Rutgers University"
EMAIL = "rishped.31@gmail.com"

SOCIAL_MEDIA = {
    "Github": "https://github.com/rishp66",
    "LinkedIn": "https://www.linkedin.com/in/rish-pednekar/"
}

st.set_page_config(page_title=PAGE_TITLE, page_icon=PAGE_ICON)

st.title("Resume")

# --- LOAD RESOURCES ----
with open(css) as f:
    st.markdown("<style>{}</style>".format(f.read()), unsafe_allow_html=True)
with open(resume, "rb") as pdf_file:
    PDFByte = pdf_file.read()
profile_pic = Image.open(profile_pic)


# display
col1, col2 = st.columns(2, gap="small")
with col1:
    st.image(profile_pic,width=230)

with col2:
    st.title(NAME)
    st.write(DESCRIPTION)
    st.download_button(
        label="⬇️ Download Resume",
        data=PDFByte,
        file_name=resume.name,
        mime="application/octet-stream"
    )
    st.write("📮️",EMAIL)

#-----socials
st.write("#")

cols = st.columns(len(SOCIAL_MEDIA))
for index, (platform,link) in enumerate(SOCIAL_MEDIA.items()):
    cols[index].write(f"[{platform}]({link})")

#----experiences
st.write("#")
st.write("---")
st.subheader("Programming Knowledge")
st.write("""
- ⌨️ Languages: Java | SQL | Python | R
- 🔖 Certifications: Google Data Analytics| LinkedIn Python | Microsoft Azure Fundamentals | Linux
- 👨‍💻 Software: Pycharm | Eclipse | BigQuery | Microsoft Azure | Excel | Word | Linux | Adobe
- 📈 Skills: Trend Analysis | Azure Cloud | dplyr | ggplot2 | Bash Scripting | IT Fundamentals

"""
)
st.write("---")
st.subheader("Work History")


st.write("***Geek Squad | Consultation Agent***")
st.write("09/22 - 11/22")
st.write(
    """
    - Ticketed over 100+ items utilizing Nova software and learning GSX exchange and troubleshot various errors on computers, laptops, televisions, etc.
    - Aided 75+ patrons by showing them how to navigate systems such as macOS, Windows, and Linux.
    """
)
st.write("---")
st.write("***YMCA Community Center | Lifeguard & Flyer Designer***")
st.write("08/20 - 9/22")
st.write(
    """
    - Taught over 25+ kids essentials of marine skills & promotes pool safety.
    - Conducted pH water safety checks to ensure water was safe.
    - Designed flyers for the company building and assisted patrons daily.
    """
)
st.write("---")
st.write("***Ricochet Health Club | Lifeguard***")
st.write("2019 - 2020")
st.write("""
         - Conducted over 100+ swim tests for children and assisted other lifeguards in group lessons.
         """)