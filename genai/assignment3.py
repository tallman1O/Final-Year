import os
os.environ["TRANSFORMERS_NO_TF"] = "1"
os.environ["TOKENIZERS_PARALLELISM"] = "false"

import streamlit as st
from transformers import pipeline

import streamlit as st
from transformers import pipeline

st.set_page_config(page_title="NLP Task Executor", layout="centered")

st.title("🧠 NLP Task Executor (Hugging Face)")
st.write("Select an NLP task and enter text to process it.")

# ----------------------------
# Task selection
# ----------------------------
task = st.selectbox(
    "Choose an NLP Task",
    [
        "Sentiment Analysis",
        "Text Generation",
        "Summarization",
        "Named Entity Recognition",
        "Question Answering"
    ]
)

# ----------------------------
# Load pipelines (lazy loading)
# ----------------------------
@st.cache_resource
def load_pipeline(task_name):
    if task_name == "Sentiment Analysis":
        return pipeline("sentiment-analysis")
    elif task_name == "Text Generation":
        return pipeline("text-generation", model="distilgpt2")
    elif task_name == "Summarization":
        return pipeline("summarization", model="facebook/bart-large-cnn")
    elif task_name == "Named Entity Recognition":
        return pipeline("ner", aggregation_strategy="simple")
    elif task_name == "Question Answering":
        return pipeline("question-answering", model="distilbert-base-cased-distilled-squad")

# ----------------------------
# Inputs
# ----------------------------
text = st.text_area("Enter Text", height=200)

question = None
if task == "Question Answering":
    question = st.text_input("Enter Question")

# ----------------------------
# Execute
# ----------------------------
if st.button("Run Task 🚀"):
    if not text.strip():
        st.warning("Enter some text first.")
    else:
        with st.spinner("Processing..."):
            nlp = load_pipeline(task)

            if task == "Sentiment Analysis":
                result = nlp(text)

            elif task == "Text Generation":
                result = nlp(text,max_new_tokens=50,do_sample=True,temperature=0.9,top_k=50,top_p=0.95)

            elif task == "Summarization":
                result = nlp(text, max_length=130, min_length=30, do_sample=False)

            elif task == "Named Entity Recognition":
                result = nlp(text)

            elif task == "Question Answering":
                if not question:
                    st.warning("Please enter a question.")
                    st.stop()
                result = nlp(question=question, context=text)

        # ----------------------------
        # Display output
        # ----------------------------
        st.subheader("Result")
        st.json(result)
