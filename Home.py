import streamlit as st
import pandas 

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

st.write("Below you can find some of the apps I have built in Python. Feel free to contact me!")

col3, emptyCol, col4 = st.columns([1.5, 0.5, 1.5])

df = pandas.read_csv("data.csv", sep=";")
with col3:
    for index, row in df[:10].iterrows():
        st.header(row["title"])
        st.write(row["description"])
        st.image("images/" + row["image"])
        st.write(f"[Source Code]({row['url']})")




with col4:
    for index, row in df[10:].iterrows():
        st.header(row["title"])
        st.write(row["description"])
        st.image("images/" + row["image"])
        st.write("[Source Code](https://pythonhow.com)")
        st.write(f"[Source Code]({row['url']})")


