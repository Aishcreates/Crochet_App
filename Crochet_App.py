import requests
import streamlit as st
from streamlit_lottie import st_lottie


st.set_page_config(page_title="Homemade Sunshine", page_icon=":tada:", layout="wide")

def load_lottieur(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

lottie_coding = load_lottieurl("https://lottie.host/35d882dd-7b61-41a3-8ecb-ccb1523427c4/Zk4ru4jjNI.json")


with st.container():
    st.subheader("Welocme to Homemade sunshine! :wave:")
    st.title("Homemade sunshine")
    st.write("Me and my friends are passionate about makeing crochet items and selling them for profit ")



with st.container():
    st.write("---")
    left_column, right_column = st.columns(2)
    with left_column:
        st.header("What our team does . . .")
        st.write("##")
        st.write(
          """
          On our website (designed by the buisness's co-owner) we sell items that were crocheted by hand as well as other crochet items that are very cheap compared to some original prices,
          these crochet items are good for:
          - Gifting (Options such as handbags, amugarami etc.)
          - Your passion for crochet 
          - Or just fashion in general!

          If this sounds interesting to you, consider buying our products and supporing us!
          """
        ) 
