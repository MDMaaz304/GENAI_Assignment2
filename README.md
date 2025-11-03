# Smart Academic Companion using Gemini API

![AI-Powered](https://img.shields.io/badge/AI-Powered-blue?style=for-the-badge&logo=ai)
![Flask](https://img.shields.io/badge/Flask-2.3.3-green?style=for-the-badge&logo=flask)
![Gemini](https://img.shields.io/badge/Gemini-API-orange?style=for-the-badge&logo=google)
![Markdown](https://img.shields.io/badge/Markdown-Rendering-lightgrey?style=for-the-badge&logo=markdown)

**Smart Academic Companion** is an intelligent web application designed to assist students, researchers, and educators in generating, summarizing, categorizing, explaining, and creating quizzes from academic content using **Google’s Gemini API**.

## 🚀 Features
- 🤖 AI-Powered content generation
- 📊 Smart summarization of long texts
- 🏷️ Automatic categorization by field/theme
- 💡 Concept explanation with examples
- 🎯 Quiz generation for self-practice
- 📝 Markdown-formatted output
- 🎨 Responsive modern UI with dark/light mode
- ⚡ Fast real-time AI response

## 🛠️ Tech Stack
- Backend: Flask (Python)
- AI Engine: Google Gemini API
- Frontend: HTML + CSS + JavaScript
- Markdown: Python-Markdown extensions

## 🔧 Setup Instructions

1️⃣ Clone
   git clone https://github.com/your-username/smart-academic-companion.git
   cd smart-academic-companion

2️⃣ Get Gemini API Key
   • Visit https://aistudio.google.com/
   • Generate and copy your key

3️⃣ Virtual Env  
   python -m venv venv
   venv\Scripts\activate   # (Windows)
   source venv/bin/activate  # (Mac/Linux)

4️⃣ Install Deps  
   pip install -r requirements.txt

5️⃣ Create .env  
   GEMINI_API_KEY=your_key_here

6️⃣ Run App  
   python app.py

7️⃣ Open  
   http://127.0.0.1:5000

## 🎯 How It Works
1. Select a task: Generate | Summarize | Categorize | Explain | Quiz  
2. Enter your topic or text  
3. Gemini AI processes it and returns formatted Markdown output  
4. View, copy, or download the result instantly

## 🧠 Examples
- Generate: “AI in Healthcare” → full structured article  
- Summarize: paste paper → concise key-points summary  
- Categorize: article → subject & theme list  
- Explain: “Quantum Entanglement” → simplified detailed note  
- Quiz: “Basics of Machine Learning” → 5–10 practice Q&As

## 📁 Structure
smart-academic-companion/
├── app.py
├── config.py
├── requirements.txt
├── .env
├── static/
│   ├── css/style.css
│   └── js/script.js
└── templates/index.html

## 👨‍💻 Developer
**Mohammed Maaz** — AI & DS ,Web Development

## 🙏 Credits
- Google Gemini AI  
- Flask Community  
- Python-Markdown  

## 📄 License
This project is open-source under the MIT License

### Quick Commands
# After cloning and activating environment
pip install -r requirements.txt

# Add your API key
echo "GEMINI_API_KEY=your_key_here" > .env

# Run the app
python app.py

# Open in browser
http://localhost:5000
