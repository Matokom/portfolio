import streamlit as st
from PIL import Image


def main():
    languages = ['Python', 'Matlab']
    st.title("Portfolio Martin Komák")
    st.text("""Na tomto webe nájdete moju poslednú tvorbu v programovacích jazykoch
    Python a Matlab. Prosím, vľavo si zvolte programovací jazyk, ktorý Vás zaujíma.""")

    #vyber programovacieho jazyka
    language = st.sidebar.selectbox("Ktorý jazyk chcete zobraziť?", ("Python", "Matlab"))
    st.subheader("")
    st.header("Moja tvorba v jazyku {}:".format(language))


    if language == "Python":
        st.subheader("Model priemyselneho robota vytvoreny v jazyku Python")
        img = Image.open("pr1.jpg")
        st.image(img, width=500, caption="hash siet PR v Pythone")

    if language == "Python":
        st.subheader("")
        st.subheader('Mobilný robot v bludisku. Video:')
        vid_file = open("MobilnyRobot.avi", 'rb').read()
        st.video(vid_file)

    if language == "Matlab":
        st.subheader('Obchádzanie prekážky')
        st.text("""Program na hľadanie najkratšej dráhy v 2D priestore s prekážkou. Video:""")

    if language == "Matlab":
        vid_file1 = open("obchadzanieprekazky.webm", 'rb').read()
        st.video(vid_file1)

