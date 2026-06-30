import streamlit as st
import google.generativeai as genai
import requests
from PIL import Image
from io import BytesIO
from config import GEMINI_API_KEY

genai.configure(api_key=GEMINI_API_KEY)
text_model = genai.GenerativeModel("gemini-pro")

HF_TOKEN = "hf_xKq9mTzLpRv2nYwBdJcAeFs7Ug3NhXoiQk"
HF_URL = "https://api-inference.huggingface.co/models/stabilityai/stable-diffusion-2"

BLOCKED_WORDS = ["violence", "weapon", "blood", "adult", "nsfw", "hate", "drugs", "gore"]

def is_safe(prompt):
    for word in BLOCKED_WORDS:
        if word in prompt.lower():
            return False
    safety_check = text_model.generate_content(
        f"Is this image prompt safe and appropriate for school students? Answer only YES or NO.\nPrompt: {prompt}"
    ).text.strip().upper()
    return safety_check.startswith("YES")

def enhance_prompt(prompt):
    return text_model.generate_content(
        f"Improve this image generation prompt to be more descriptive and visually detailed. Keep it school-appropriate. Return only the improved prompt.\n\nOriginal: {prompt}"
    ).text.strip()

def generate_image(prompt):
    headers = {"Authorization": f"Bearer {HF_TOKEN}"}
    response = requests.post(HF_URL, headers=headers, json={"inputs": prompt})
    if response.status_code == 200:
        return Image.open(BytesIO(response.content))
    return None

st.set_page_config(page_title="Safe AI Image Generator", page_icon="🎨")
st.title("🎨 Safe AI Image Generation")
st.caption("Gemini safety check + Stable Diffusion generation")

prompt = st.text_input("Describe your image", placeholder="e.g. A robot reading books in a library")

col1, col2 = st.columns(2)
with col1:
    enhance = st.checkbox("✨ Auto-enhance prompt with AI")
with col2:
    show_prompt = st.checkbox("Show final prompt used")

if st.button("Generate Image 🖼️"):
    if not prompt.strip():
        st.warning("Please enter a description.")
    elif not is_safe(prompt):
        st.error("⚠️ This prompt was flagged as unsafe. Please try a different description.")
    else:
        final_prompt = enhance_prompt(prompt) if enhance else prompt
        if show_prompt:
            st.info(f"Final prompt: {final_prompt}")
        with st.spinner("Generating image..."):
            img = generate_image(final_prompt)
        if img:
            st.image(img, caption=final_prompt)
            buf = BytesIO()
            img.save(buf, format="PNG")
            st.download_button("Download Image", buf.getvalue(), "generated.png", "image/png")
        else:
            st.error("Could not generate image. Try again.")

st.markdown("---")
st.markdown("**Safe to try:** landscapes, animals, space, cartoons, food, nature, robots")
