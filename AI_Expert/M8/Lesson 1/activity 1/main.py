import streamlit as st
import google.generativeai as genai
from config import GEMINI_API_KEY

genai.configure(api_key=GEMINI_API_KEY)
model = genai.GenerativeModel("gemini-pro")

SYSTEM_PROMPT = """You are an AI Teaching Assistant for school students (Grade 9-12).
Your job is to explain concepts clearly and simply.
Always give examples. Encourage the student. Keep answers concise."""

def ask(question):
    prompt = f"{SYSTEM_PROMPT}\n\nStudent Question: {question}"
    return model.generate_content(prompt).text

st.set_page_config(page_title="AI Teaching Assistant", page_icon="🎓")
st.title("🎓 AI Teaching Assistant")
st.caption("Powered by Gemini API")

st.markdown("Ask me anything about your school subjects!")

subject = st.selectbox("Select Subject", ["General", "Math", "Science", "History", "English", "Computer Science"])

question = st.text_area("Your Question", placeholder="e.g. What is photosynthesis?")

if st.button("Ask AI"):
    if question.strip():
        with st.spinner("Thinking..."):
            full_q = f"Subject: {subject}\n{question}"
            answer = ask(full_q)
        st.success("Answer:")
        st.write(answer)
    else:
        st.warning("Please type a question.")

st.markdown("---")
st.markdown("**Tips for better answers:** Be specific! Instead of 'explain math', try 'explain quadratic equations with an example'.")
