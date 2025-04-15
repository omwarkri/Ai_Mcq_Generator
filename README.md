# 🧠 AI MCQ Generator with Explanations (Gemini-powered)

This is a Flask-based web application that uses Google's **Gemini 1.5 Flash** model to generate multiple-choice questions (MCQs) based on a user-provided topic. You can choose the number of questions and difficulty level (Easy, Medium, Hard). Each question includes options, the correct answer, and a brief explanation.

## 🚀 Features

- 🔤 Enter any topic (e.g., Machine Learning, Indian History, etc.)
- 🔢 Select number of questions: 5, 10, 15, or 20
- 🎯 Choose difficulty: Easy / Medium / Hard
- 🤖 Uses Gemini 1.5 Flash model via Generative AI API
- 📋 Displays questions, options, correct answer, and explanation
- 💡 Show/Hide answer functionality

---

## 🛠️ Tech Stack

- **Frontend:** HTML, CSS, JavaScript (vanilla)
- **Backend:** Python, Flask
- **AI Model:** Gemini 1.5 Flash (via Google Generative AI API)

---

## 📦 Installation

1. **Clone the repository**

```bash
git clone https://github.com/omwarkri/Ai_Mcq_Generator.git
cd Ai_Mcq_Generator
```

2. **Create and activate a virtual environment (optional but recommended)**

```bash
python -m venv venv
venv\Scripts\activate     # For Windows
# or
source venv/bin/activate  # For Linux/Mac
```

3. **Install dependencies**

```bash
pip install -r requirements.txt
```

4. **Set up your Google Generative AI API key**

Edit the Python file (e.g., `app.py`) and set your Gemini API key:

```python
genai.configure(api_key="YOUR_API_KEY_HERE")
```

You can get a free API key from: [https://makersuite.google.com/app](https://makersuite.google.com/app)

---

## ▶️ Run the App

```bash
python app.py
```

Then open your browser and visit:  
📍 `http://127.0.0.1:5000/`

---

## 📸 Screenshots

*(Optional: Add screenshots of your app here to visually explain how it works)*

---

## 📝 Example Output

**Topic:** Python Basics  
**Difficulty:** Easy  
**Sample Question:**

```
1. What is the output of the expression 3 + 2 * 2 in Python?
   a) 10
   b) 7
   c) 9
   d) 8
   Correct answer: b) 7
   Explanation: Multiplication has higher precedence, so 2 * 2 = 4, then 3 + 4 = 7.
```

---

## 🧠 Notes

- Ensure your Google API key has access to the Gemini models.
- You may hit rate limits if using the free tier excessively.
- Model responses may vary, so some basic formatting cleanup may be required in production.

---

## 📄 License

MIT License

---

## 🙋‍♂️ Author

**Om Bandu Warkari**  
📍 [Ambernath, Thane]  
🎓 BCA 3rd Year | Brijlal Biyani Science College, Amravati  
🔗 [GitHub Profile](https://github.com/omwarkri)

---

```