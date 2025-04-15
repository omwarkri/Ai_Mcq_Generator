from flask import Flask, render_template, request
import google.generativeai as genai

app = Flask(__name__)

# Configure Gemini
genai.configure(api_key="AIzaSyBnrbH9pVK6-xFrHIlcrY6ONAhAC7gFItI")

@app.route('/', methods=['GET', 'POST'])
def index():
    mcqs = ""
    error = None
    question_count = 10
    difficulty = "easy"
    
    if request.method == 'POST':
        topic = request.form.get('topic', '').strip()
        question_count = int(request.form.get('question_count', 10))
        difficulty = request.form.get('difficulty', 'easy')
        
        if not topic:
            error = "Please enter a topic to generate questions."
        else:
            try:
                model = genai.GenerativeModel("gemini-1.5-flash")
                
                prompt = f"""
Generate exactly {question_count} {difficulty}-level multiple-choice questions on: {topic}

Each question must follow **exactly** this format:
1. [Question text]
   a) Option 1
   b) Option 2
   c) Option 3
   d) Option 4
   Correct answer: [letter] [correct answer text]
   Explanation: [4-5 sentence explanation]

Ensure:
- All questions are numbered
- Options are labeled a) to d)
- 'Correct answer:' and 'Explanation:' are present
- Format is consistent and readable
"""
                response = model.generate_content(prompt)
                mcqs = response.text
                print(mcqs)  # For debugging
                
            except Exception as e:
                error = f"Error generating questions: {str(e)}"
                print(f"API Error: {e}")
    
    return render_template('index.html', 
                         mcqs=mcqs, 
                         error=error,
                         question_count=question_count,
                         difficulty=difficulty)

if __name__ == '__main__':
    app.run(debug=True)