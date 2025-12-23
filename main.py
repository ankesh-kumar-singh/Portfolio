import streamlit as st
from PIL import Image

st.set_page_config(page_icon= "portfolio.png", page_title= "My Portfolio(Powered by Streamlit)", layout = "centered", initial_sidebar_state= "expanded")



image = Image.open("000000.png")



st.sidebar.image(image, use_container_width = True)
st.sidebar.title("Ankesh Kumar Singh")
st.sidebar.subheader("Data Science and ML Enthusiast")
st.sidebar.write("📍 Phagwāra, Kapurthala, Punjab, IND")
st.sidebar.write("📧 science02infinity@gmail.com")

# Social Media Links
st.sidebar.markdown("""
[![LinkedIn](https://img.icons8.com/color/48/000000/linkedin.png)](https://www.linkedin.com/in/bigdatakingsingh/)
[![GitHub](https://img.icons8.com/ios-glyphs/48/000000/github.png)](https://github.com/Ankesh-Singh-12220182)
[![Kaggle](https://img.icons8.com/external-tal-revivo-filled-tal-revivo/48/000000/external-kaggle-an-online-community-of-data-scientists-and-machine-learners-owned-by-google-logo-filled-tal-revivo.png)](https://www.kaggle.com/ankeshsinghkaggle)
""")


st.title("About Me")

# Introduction
st.write(
    "I am a **B.Tech Computer Science Engineering student** specializing in **Data Science and Machine Learning**. "
    "Passionate about solving real-world problems using **AI, NLP, and Big Data**, "
    "I am constantly expanding my skill set to stay ahead in the ever-evolving tech landscape."
)

# Experience & Expertise
st.write(
    "With a strong foundation in **Machine Learning, Deep Learning, and Data Analytics**, I have worked on projects involving "
    "**Exploratory Data Analysis (EDA), NLP, and Big Data processing**. I am also exploring **FastAPI, PySpark, and Polars** "
    "to enhance my expertise in scalable data solutions."
)

st.title("Education")
st.write("""- Lovely Professional University, Punjab | B.Tech CSE (Data Science with ML) | Aug 2022 - July 2026 | CGPA: 6.72
- Saraswati Vidya Mandir School, Jharkhand | Matriculation + Intermediate | April 2018 - March 2021
- Aakash Institute, Ranchi, Jharkhand | Joint Entrance Examination(JEE Mains + Advanced) Coaching | May 2019 - Jan 2020""")

# Skills & Technologies
st.title("Skills & Technologies")
st.markdown("""
- 💡 **Programming:** Python, SQL  
- 📊 **Data Science:** Pandas, NumPy, Matplotlib, Seaborn  
- 🤖 **Machine Learning:** Scikit-Learn, TensorFlow, PyTorch  
- 🗣️ **NLP:** SpaCy, NLTK, Transformers  
- 🚀 **Big Data:** PySpark, Polars  
- 🌐 **Web Frameworks:** FastAPI, Streamlit  
- 📡 **Version Control & Deployment:** Git, Docker  
""")

st.title("Certifications")

st.write("- Complete Machine Learning and Data Science Program | GeeksforGeeks | July 2024 [Link ↗️](https://media.geeksforgeeks.org/courses/certificates/728f9bc8508e1b4e674684c535f46006.pdf)")

st.write("- Machine Learning & its Applications | Indian Institute of Technology, Roorkee | September 2024 [Link ↗️](https://www.linkedin.com/in/bigdatakingsingh/details/certifications/1726907444267/single-media-viewer/?profileId=ACoAAD1yMUIBjSapLVW4WipRB3RQnt7vEP7KKMo)")

st.title("Projects")

st.subheader("➡️ 🔐 **Smart Password Manager Using Java**")
st.write("A secure and efficient password management system built using **Java**. This project helps users generate, store, and manage strong passwords securely with encryption mechanisms. Designed for enhanced security and ease of access.")

st.write("**Skills:** Java Programming, Data Structures etc.")
st.write("[GitHub Repository ↗️](https://github.com/Ankesh-Singh-12220182/Password_Manager)")


st.image("img2.png", caption = "Screenshot 1")
st.image("img1.png", caption = "Screenshot 2")

st.subheader("➡️ 🌍 **Earthquake Magnitude Prediction Using Machine Learning**")
st.write(
    "Earthquake Magnitude Prediction using Machine Learning",
    "This project utilizes machine learning techniques to predict earthquake magnitudes based on historical seismic data. "
    "By analyzing various geophysical parameters, the model aims to provide insights that can aid in early warning systems. "
    "The project involves data preprocessing, feature engineering, model training, and evaluation to enhance prediction accuracy."
)

st.write("**Skills:** Pandas, NumPy, Seaborn, Machine Learning Algorithms, Calculus, Linear Algebra etc.")

st.image("Screenshot 2025-04-03 013742.png")

st.title("Resume")

st.write("Download my resume")

# Load the PDF file
with open("AnkeshSinghGeneralCV.pdf", "rb") as file:
    pdf_bytes = file.read()

# Create a download button
st.download_button(
    label="👆 Click here",
    data=pdf_bytes,
    file_name="AnkeshSinghResume.pdf",
    mime="application/pdf"
)



