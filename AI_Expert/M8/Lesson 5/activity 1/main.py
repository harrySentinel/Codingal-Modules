import streamlit as st
import google.generativeai as genai
from config import GEMINI_API_KEY

genai.configure(api_key=GEMINI_API_KEY)
model = genai.GenerativeModel("gemini-pro")

def ask(prompt):
    return model.generate_content(prompt).text

st.set_page_config(page_title="Multi-Tool AI App", page_icon="🤖", layout="wide")
st.title("🤖 Multi-Tool AI App — Part 1")
st.caption("Powered by Gemini API")

tool = st.sidebar.selectbox("Choose a Tool", [
    "📝 Essay Writer",
    "🔤 Grammar Checker",
    "📖 Story Generator",
    "🌍 Language Translator",
])

st.sidebar.markdown("---")
st.sidebar.info("Select a tool from the menu above to get started.")

if tool == "📝 Essay Writer":
    st.header("📝 Essay Writer")
    topic = st.text_input("Essay Topic", placeholder="e.g. Climate Change")
    tone = st.selectbox("Tone", ["Formal", "Casual", "Persuasive", "Academic"])
    length = st.select_slider("Length", ["Short (150 words)", "Medium (300 words)", "Long (500 words)"])
    word_count = {"Short (150 words)": 150, "Medium (300 words)": 300, "Long (500 words)": 500}[length]

    if st.button("Write Essay"):
        if topic:
            with st.spinner("Writing..."):
                prompt = f"Write a {word_count}-word {tone.lower()} essay about '{topic}'. Include introduction, body, and conclusion."
                result = ask(prompt)
            st.write(result)
            st.download_button("Download Essay", result, "essay.txt")
        else:
            st.warning("Enter a topic.")

elif tool == "🔤 Grammar Checker":
    st.header("🔤 Grammar Checker")
    text = st.text_area("Paste your text here", height=200)

    if st.button("Check Grammar"):
        if text:
            with st.spinner("Checking..."):
                prompt = f"Check this text for grammar, spelling, and punctuation errors. List each mistake and the correction:\n\n{text}"
                result = ask(prompt)
            st.markdown("### Feedback")
            st.write(result)

            with st.spinner("Generating corrected version..."):
                corrected = ask(f"Rewrite this text with all grammar and spelling errors fixed:\n\n{text}")
            st.markdown("### Corrected Version")
            st.success(corrected)
        else:
            st.warning("Paste some text first.")

elif tool == "📖 Story Generator":
    st.header("📖 Story Generator")
    genre = st.selectbox("Genre", ["Adventure", "Mystery", "Sci-Fi", "Fantasy", "Horror", "Romance", "Comedy"])
    character = st.text_input("Main Character Name", placeholder="e.g. Aditya Srivastava")
    setting = st.text_input("Story Setting", placeholder="e.g. A space station in 2075")
    twist = st.checkbox("Add a surprise twist at the end")

    if st.button("Generate Story"):
        if character and setting:
            with st.spinner("Writing your story..."):
                prompt = f"Write a short {genre} story (around 300 words) with a character named {character} set in {setting}."
                if twist:
                    prompt += " Include a surprising twist at the end."
                result = ask(prompt)
            st.write(result)
            st.download_button("Download Story", result, "story.txt")
        else:
            st.warning("Fill in character name and setting.")

elif tool == "🌍 Language Translator":
    st.header("🌍 Language Translator")
    text = st.text_area("Text to translate", placeholder="Type anything here...")
    target_lang = st.selectbox("Translate to", [
        "Hindi", "French", "Spanish", "German", "Japanese",
        "Arabic", "Chinese", "Portuguese", "Russian", "Korean"
    ])

    if st.button("Translate"):
        if text:
            with st.spinner("Translating..."):
                prompt = f"Translate the following text to {target_lang}. Return only the translation:\n\n{text}"
                result = ask(prompt)
            st.markdown(f"### Translation ({target_lang})")
            st.success(result)
        else:
            st.warning("Enter text to translate.")
