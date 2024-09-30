import streamlit as st
from QAWithPDF.data_ingestion import load_data
from QAWithPDF.embedding import download_gemini_embedding
from QAWithPDF.model_api import load_model

def main():
    # Set page configuration with a title and layout
    st.set_page_config(page_title="Document QnA", layout="wide")

    # Add a title and some description
    st.title("🔍 QnA from Your Document")
    st.write(
        "Upload a document and ask any questions regarding its content. "
        "Press 'Enter' or click 'Submit' to get answers!"
    )

    #Sidebar
    st.sidebar.header("Instructions")
    st.sidebar.write("1. Upload your document.")
    st.sidebar.write("2. Type your question in the input box.")
    st.sidebar.write("3. Press 'Enter' or click 'Submit' to see the answer.")
    st.sidebar.write("By Bhumish Dayal")
    
    doc = st.file_uploader("Upload your document")

    st.header("Ask Your Question")
    
    with st.form(key="qa_form"):
        user_question = st.text_input("Type your question here:")
        submit_button = st.form_submit_button("Submit")

    if submit_button:
        if doc is not None and user_question:
            with st.spinner("Processing your question..."):
                document = load_data(doc)
                model = load_model()
                query_engine = download_gemini_embedding(model, document)
                
                response = query_engine.query(user_question)
                
                st.success("Here's your answer:")
                st.write(response.response)
        else:
            st.error("Please make sure to upload a document and enter a question.")
    
    st.markdown("---") 

if __name__ == "__main__":
    main()

