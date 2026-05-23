import streamlit as st
from transformers import pipeline
# Title and description
st.title("💬 Question Answering App")
st.markdown("""
This app uses a pre-trained Hugging Face Transformer model to
answer questions based on a given context paragraph.
""")
# Load question-answering pipeline
@st.cache_resource
def load_model():
 return pipeline("question-answering",
model="distilbert-base-uncased-distilled-squad")
qa_pipeline = load_model()
# Input fields
context = st.text_area("📝 Enter the context paragraph here:",
height=200)
question = st.text_input("❓ Ask your question:")
# Button to trigger answer
if st.button("🔍 Get Answer"):
 if not context or not question:
    st.warning("Please provide both context and question.")
 else:
    with st.spinner("Finding the answer..."):
        result = qa_pipeline({'question': question,'context': context})
        st.success("Answer:")
        st.markdown(f"**{result['answer']}**")
# Footer
st.markdown("---")
st.markdown("🔗 Powered by [Hugging FaceTransformers](https://huggingface.co/models) and[Streamlit](https://streamlit.io/)")
