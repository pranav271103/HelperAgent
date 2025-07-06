# HelperAgent

**HelperAgent** is an easy-to-use AI homework assistant. It lets you upload a photo of your question (like a math problem or science question) **or** just type your question — and it will give you a clear, step-by-step answer using Google's Gemini AI.

No coding skills required.

---

## What Can It Do?

- Upload an image of a question → it extracts the text using OCR
- Or, type your question directly
- Gemini AI will then solve it and show the steps
- Works for: **Math, Science, English, SST, Computer Science**

---

## Tools Used

- Python
- Streamlit (for the user interface)
- Tesseract (for reading text from images)
- Google Gemini (for AI-powered answers)

---

## How to Run This Project

> These steps are for running the app **on your own computer**

### 1. Clone the Project

```bash
git clone https://github.com/yourusername/HelperAgent.git
cd HelperAgent
```

### 2. Install Python Packages

Make sure you have Python 3.10+ installed.

Then run:

```bash
pip install -r requirements.txt
```

Also install Tesseract (if you're on Ubuntu):

```bash
sudo apt install tesseract-ocr
```

### 3. Get Gemini API Key

1. Go to: [https://makersuite.google.com/app/apikey](https://makersuite.google.com/app/apikey)
2. Click **Create API Key**
3. Copy the key

### 4. Add the Key to the App

Create a folder named `.streamlit` in the project folder:

```bash
mkdir .streamlit
```

Then create a file named `secrets.toml` inside it:

```toml
# .streamlit/secrets.toml
GEMINI_API_KEY = "paste-your-key-here"
```

### 5. Run the App

```bash
streamlit run app.py
```

It will open a browser window where you can:

* Upload an image of a question, or
* Type your question

---

## How to Use

### Option 1: Upload Image

Take a clear picture of your homework question (like: "Solve for x: 3x + 6 = 15") and upload it.

The app will:

1. Read the text from the image
2. Show it
3. Give a step-by-step answer

### Option 2: Type Your Question

Just type any question (like "What is Newton's Second Law?") and click **Submit**.

---

## Optional: Use the Notebooks

The project also includes:

* `TextPip.ipynb` – Use this to test questions by typing only
* `ImagePip.ipynb` – Use this for trying image-based questions in Jupyter/Colab

---

## 🛠 Example Questions

* `Solve for x: 4x - 8 = 12`
* `What caused the French Revolution?`
* `Explain working of an operating system`

---

## Need Help?

If anything breaks or doesn't work:

* Make sure your API key is active
* Make sure your image is clear

---

## License

This project is MIT licensed. You can use and modify it freely.

---

**Built with 💡 by Pranav**

---

## Summary for Beginners

| Step | Description |
|------|-------------|
| 1️   | Clone the repo |
| 2️   | Install requirements |
| 3️   | Get Gemini API key |
| 4️   | Add `.streamlit/secrets.toml` |
| 5️   | Run: `streamlit run app.py` |

--- 