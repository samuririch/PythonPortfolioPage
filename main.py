import streamlit as st

st.set_page_config(layout="wide")

col1, col2 = st.columns(2)

with col1:
    st.image("images/MeAndPhillie.jpg", width=300)

with col2:
    st.title("Samuel Richards")
    content = """
Hello There, I'm Samuel! I am a Web/Software Developer with almost a decade of experience!
I graduated with my Bachelor's of Science degree from Shepherd University (Go Rams!). I primarily worked with Java in school - but now I work with the .NET Framework (Core, MVC, etc)
I love building things and solving puzzles - so programming is a perfect fit for me!
    """
    st.info(content)