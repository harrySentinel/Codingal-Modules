import streamlit as st
import google.generativeai as genai
from PIL import Image
from config import GEMINI_API_KEY

genai.configure(api_key=GEMINI_API_KEY)
text_model = genai.GenerativeModel("gemini-pro")
vision_model = genai.GenerativeModel("gemini-pro-vision")

def ask(prompt):
    return text_model.generate_content(prompt).text

def ask_vision(prompt, image):
    return vision_model.generate_content([prompt, image]).text

st.set_page_config(page_title="Multi-Tool AI App", page_icon="🤖", layout="wide")
st.title("🤖 Multi-Tool AI App — Part 2")
st.caption("Extended with Vision, Quiz & Chat — Powered by Gemini")

tool = st.sidebar.selectbox("Choose a Tool", [
    "🖼️ Image Analyzer",
    "❓ Quiz Generator",
    "💬 AI Chatbot",
    "📊 Text Summarizer",
    "💡 Idea Brainstormer",
])

st.sidebar.markdown("---")
st.sidebar.info("This is the complete Multi-Tool AI App with 5 more tools.")

if tool == "🖼️ Image Analyzer":
    st.header("🖼️ Image Analyzer")
    uploaded = st.file_uploader("Upload an image", type=["jpg", "jpeg", "png"])
    mode = st.radio("What do you want?", ["Describe the image", "Ask a question about it"])
    question = ""
    if mode == "Ask a question about it":
        question = st.text_input("Your question about the image")

    if uploaded and st.button("Analyze"):
        img = Image.open(uploaded)
        st.image(img, caption="Uploaded Image", use_column_width=True)
        with st.spinner("Analyzing..."):
            prompt = question if question else "Describe this image in detail. What do you see?"
            result = ask_vision(prompt, img)
        st.markdown("### AI Response")
        st.write(result)

elif tool == "❓ Quiz Generator":
    st.header("❓ Quiz Generator")
    topic = st.text_input("Topic", placeholder="e.g. Solar System")
    num_q = st.slider("Number of Questions", 3, 10, 5)
    difficulty = st.selectbox("Difficulty", ["Easy", "Medium", "Hard"])

    if st.button("Generate Quiz"):
        if topic:
            with st.spinner("Creating quiz..."):
                prompt = f"Create a {difficulty.lower()} multiple choice quiz about '{topic}' with {num_q} questions. For each question provide 4 options (A/B/C/D) and mark the correct answer at the end."
                result = ask(prompt)
            st.markdown("### Your Quiz")
            st.write(result)
            st.download_button("Download Quiz", result, "quiz.txt")
        else:
            st.warning("Enter a topic.")

elif tool == "💬 AI Chatbot":
    st.header("💬 AI Chatbot")

    if "chat_log" not in st.session_state:
        st.session_state.chat_log = []

    persona = st.selectbox("Chatbot Persona", [
        "Helpful Assistant", "Science Teacher", "History Expert",
        "Motivational Coach", "Coding Tutor"
    ])

    for role, msg in st.session_state.chat_log:
        st.chat_message("user" if role == "You" else "assistant").write(msg)

    user_input = st.chat_input("Type your message...")
    if user_input:
        st.session_state.chat_log.append(("You", user_input))
        history = "\n".join([f"{r}: {m}" for r, m in st.session_state.chat_log])
        prompt = f"You are a {persona}. Respond helpfully.\n\n{history}\nAssistant:"
        with st.spinner("Typing..."):
            reply = ask(prompt)
        st.session_state.chat_log.append(("AI", reply))
        st.rerun()

    if st.button("Clear Chat"):
        st.session_state.chat_log = []
        st.rerun()

elif tool == "📊 Text Summarizer":
    st.header("📊 Text Summarizer")
    text = st.text_area("Paste your text here", height=250, placeholder="Paste article, notes, or any long text...")
    style = st.selectbox("Summary Style", ["Bullet Points", "Short Paragraph", "One Sentence", "Detailed"])
    length_map = {"One Sentence": 1, "Short Paragraph": 3, "Bullet Points": 5, "Detailed": 10}

    if st.button("Summarize"):
        if text.strip():
            with st.spinner("Summarizing..."):
                prompt = f"Summarize the following text as {style.lower()}:\n\n{text}"
                result = ask(prompt)
            st.markdown("### Summary")
            st.write(result)
            st.info(f"Original: {len(text.split())} words → Summary: {len(result.split())} words")
        else:
            st.warning("Paste some text first.")

elif tool == "💡 Idea Brainstormer":
    st.header("💡 Idea Brainstormer")
    category = st.selectbox("Category", [
        "Project Ideas", "Business Ideas", "Science Experiments",
        "Story Ideas", "App Ideas", "Social Media Content"
    ])
    keyword = st.text_input("Keyword or Theme", placeholder="e.g. environment, space, food")
    num_ideas = st.slider("Number of Ideas", 3, 10, 5)

    if st.button("Generate Ideas 💡"):
        if keyword:
            with st.spinner("Brainstorming..."):
                prompt = f"Generate {num_ideas} creative {category.lower()} related to '{keyword}'. Number each idea and give a one-line description."
                result = ask(prompt)
            st.markdown("### Ideas")
            st.write(result)
        else:
            st.warning("Enter a keyword.")
