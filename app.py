import nltk
nltk.download('punkt')
nltk.download('punkt_tab')

# app.py
import streamlit as st
from utils.agent import LegalAgent
from utils.document_processing import extract_text_from_pdf
from utils.legal_analysis import analyze_legal_document
from utils.summarization import summarize_text
from utils.pdf_generation import generate_case_pdf

# Initialize the agent
agent = LegalAgent()

# Streamlit app
st.title("AI-Powered Legal Research Assistant")
tab1, tab2 = st.tabs(["Chat with AI", "Upload Document"])

# Chat Tab
with tab1:
    st.header("Chat with AI")
    user_input = st.chat_input("Ask your legal question:")
    if user_input:
        with st.chat_message("user"):
            st.write(user_input)
        with st.chat_message("assistant"):
            response = agent.handle_query(user_input)
            st.write(response)

# Document Upload Tab
with tab2:
    st.header("Upload Legal Document")
    uploaded_file = st.file_uploader("Choose a PDF file", type="pdf")
    if uploaded_file:
        text = extract_text_from_pdf(uploaded_file)
        analysis = analyze_legal_document(text)
        summary = summarize_text(text)
        st.write("Extracted Information:", analysis)
        st.write("Summary:", summary)
        # Chat with document context
        doc_query = st.chat_input("Ask a question about this document:")
        if doc_query:
            with st.chat_message("user"):
                st.write(doc_query)
            with st.chat_message("assistant"):
                response = agent.handle_query(doc_query, document_text=text)
                st.write(response)
        # PDF generation
        if st.button("Generate Case PDF"):
            pdf_content = generate_case_pdf(analysis, summary)
            st.download_button(
                label="Download PDF",
                data=pdf_content,
                file_name="case_summary.pdf",
                mime="application/pdf"
            )