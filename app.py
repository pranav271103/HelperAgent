# app.py
import streamlit as st
from PIL import Image, ImageEnhance, ImageOps
import pytesseract
import google.generativeai as genai

# ───────────────────────────────────────────────────────────
# Configure Gemini
genai.configure(api_key=st.secrets["GEMINI_API_KEY"])
gemini_model = genai.GenerativeModel("gemini-1.5-flash-latest")

# ───────────────────────────────────────────────────────────
# Preprocess image for better OCR
def preprocess_image(image):
    image = ImageOps.grayscale(image)
    image = ImageEnhance.Contrast(image).enhance(2.5)
    image = image.resize((image.width * 2, image.height * 2))
    return image.convert("RGB")

# OCR from image
def ocr_extract_text_from_image(image):
    try:
        image = preprocess_image(image)
        text = pytesseract.image_to_string(image)
        return text.strip()
    except Exception as e:
        return f"OCR error: {str(e)}"

# Gemini helper
def homework_helper_agent(question):
    if not question or question.strip() in ["", ".", "-", "........"]:
        return "Please enter a valid question."

    prompt = f"""
You're an AI Homework Helper.

Respond step-by-step for numerical/math problems.
Respond clearly for theoretical or science questions.

Here’s the question:
{question}
"""
    response = gemini_model.generate_content(prompt)
    return response.text.strip()

# ───────────────────────────────────────────────────────────
# Streamlit App
st.set_page_config(page_title="HelperAgent", layout="centered")
st.title("HelperAgent")
st.markdown("Ask your homework questions using text or image. At least one input is required.")

# Inputs
uploaded_img = st.file_uploader("Upload an image", type=["jpg", "jpeg", "png"])
text_input = st.text_area("Or type your question below")

# Submit button
if st.button("Submit"):
    if not uploaded_img and not text_input.strip():
        st.warning("Please upload an image or type a question.")
    else:
        with st.spinner("Processing..."):
            if uploaded_img:
                img = Image.open(uploaded_img)
                st.image(img, caption="Uploaded Image", use_column_width=True)
                question = ocr_extract_text_from_image(img)
                st.subheader("Extracted Question")
                st.text(question)
            else:
                question = text_input.strip()

            st.subheader("Answer")
            answer = homework_helper_agent(question)
            st.markdown(answer)
