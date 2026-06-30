import streamlit as st
import google.generativeai as genai
from config import GEMINI_API_KEY

genai.configure(api_key=GEMINI_API_KEY)
model = genai.GenerativeModel("gemini-pro")

SYSTEM_PROMPT = """You are an AI Teaching Assistant for school students (Grade 9-12).
Explain concepts clearly with examples. Be encouraging and concise.
You remember the full conversation and can refer back to earlier questions."""

def build_prompt(history, new_question):
    conversation = ""
    for role, msg in history:
        conversation += f"{role}: {msg}\n"
    conversation += f"Student: {new_question}"
    return f"{SYSTEM_PROMPT}\n\n{conversation}\nAssistant:"

st.set_page_config(page_title="AI Teaching Assistant", page_icon="🎓")
st.title("🎓 AI Teaching Assistant with Conversation History")
st.caption("Powered by Gemini API — remembers your conversation!")

if "history" not in st.session_state:
    st.session_state.history = []

if st.session_state.history:
    st.markdown("### Conversation")
    for role, msg in st.session_state.history:
        if role == "Student":
            st.chat_message("user").write(msg)
        else:
            st.chat_message("assistant").write(msg)

question = st.chat_input("Ask a question...")

if question:
    st.session_state.history.append(("Student", question))
    with st.spinner("Thinking..."):
        prompt = build_prompt(st.session_state.history[:-1], question)
        answer = model.generate_content(prompt).text
    st.session_state.history.append(("Assistant", answer))
    st.rerun()

col1, col2 = st.columns(2)
with col1:
    if st.button("Clear Conversation"):
        st.session_state.history = []
        st.rerun()
with col2:
    if st.button("Save Chat"):
        with open("chat_history.txt", "w") as f:
            for role, msg in st.session_state.history:
                f.write(f"{role}: {msg}\n\n")
        st.success("Saved to 'chat_history.txt'")
