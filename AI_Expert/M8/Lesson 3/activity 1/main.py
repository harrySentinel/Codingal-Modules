import streamlit as st
import google.generativeai as genai
from config import GEMINI_API_KEY

genai.configure(api_key=GEMINI_API_KEY)
model = genai.GenerativeModel("gemini-pro")

def solve(problem, mode):
    if mode == "Step-by-Step Solution":
        prompt = f"Solve this math problem step by step, explaining each step clearly for a school student:\n\n{problem}"
    elif mode == "Hint Only":
        prompt = f"Give only a helpful hint (no full solution) to help a student start solving this math problem:\n\n{problem}"
    elif mode == "Generate Similar Problem":
        prompt = f"Create a similar math problem to this one with a different set of numbers, then solve it step by step:\n\n{problem}"
    else:
        prompt = f"Check if this math solution is correct and explain any mistakes:\n\n{problem}"
    return model.generate_content(prompt).text

st.set_page_config(page_title="Math Mastermind", page_icon="🧮")
st.title("🧮 Math Mastermind")
st.caption("AI-Powered Math Problem Solver — Powered by Gemini")

topic = st.selectbox("Math Topic", [
    "Any", "Algebra", "Geometry", "Trigonometry",
    "Calculus", "Statistics", "Arithmetic", "Word Problems"
])

mode = st.radio("Mode", [
    "Step-by-Step Solution",
    "Hint Only",
    "Generate Similar Problem",
    "Check My Solution"
])

problem = st.text_area("Enter Math Problem", placeholder="e.g. Solve: 2x + 5 = 15")

if mode == "Check My Solution":
    user_solution = st.text_area("Your Solution", placeholder="Show your working here...")
    if user_solution:
        problem = f"Problem: {problem}\n\nStudent's Solution:\n{user_solution}"

if st.button("Solve with AI 🚀"):
    if problem.strip():
        full_problem = f"[Topic: {topic}]\n{problem}" if topic != "Any" else problem
        with st.spinner("Solving..."):
            result = solve(full_problem, mode)
        st.markdown("### Result")
        st.write(result)

        if st.download_button("Download Solution", result, file_name="solution.txt"):
            pass
    else:
        st.warning("Please enter a math problem.")

st.markdown("---")
st.info("Tip: The more clearly you write your problem, the better the AI can help!")
