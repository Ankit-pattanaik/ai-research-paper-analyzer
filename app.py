import streamlit as st
from pdf_utils import extract_text_from_pdf
from paper_analyzer import summarize_paper, explain_simple, ask_question

st.set_page_config(page_title=" Research Paper Assistant")

st.title("📚 AI Research Paper Assistant")

uploaded_file = st.file_uploader("Upload Research Paper (PDF)", type=["pdf"])

if uploaded_file:

    text = extract_text_from_pdf(uploaded_file)

    st.success("Paper loaded successfully")

    option = st.selectbox(
        "Choose an action",
        [
            "Summarize Paper",
            "Explain Paper Simply",
            "Ask Question"
        ]
    )

    if option == "Summarize Paper":

        if st.button("Generate Summary"):

            with st.spinner("Analyzing paper..."):
                result = summarize_paper(text)

            st.subheader("Summary")
            st.write(result)

    elif option == "Explain Paper Simply":

        if st.button("Explain Paper"):

            with st.spinner("Generating explanation..."):
                result = explain_simple(text)

            st.subheader("Simple Explanation")
            st.write(result)

    elif option == "Ask Question":

        question = st.text_input("Enter your question")

        if st.button("Get Answer"):

            with st.spinner("Searching answer..."):
                result = ask_question(text, question)

            st.subheader("Answer")
            st.write(result)