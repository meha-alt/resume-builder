import streamlit as st
from main import main
from main2 import ats_scanner


st.set_page_config(
    page_title="ResumeBuilder",
    layout="centered",
    initial_sidebar_state="collapsed"
)

if 'page' not in st.session_state:
    st.session_state.page = 'home'

def back_button():
    col1, col2, col3 = st.columns([1, 8, 1])
    with col2:
        if st.button("← Back", key="back_button"):
            st.session_state.page = 'home'
            st.rerun()

def home_page():
    st.title("Smart Resume Builder")
    if st.button("Build my Resume"):
        st.session_state.page="resume_builder"
        st.rerun()
    if st.button("Ats Scanner"):
        st.session_state.page="ats_scanner"
        st.rerun()
    st.markdown("[Click here to open Job Search 🚀](https://ai-powered-job-search.streamlit.app/)")

if st.session_state.page == "home":
    home_page()
elif st.session_state.page == "resume_builder":
    back_button()
    main()
elif st.session_state.page == "ats_scanner":
    back_button()
    ats_scanner()
