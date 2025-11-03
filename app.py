from flask import Flask, render_template, request, jsonify
import google.generativeai as genai
import markdown
import os
from config import Config

app = Flask(__name__)
app.config.from_object(Config)
from flask import Flask, render_template, request, jsonify
import google.generativeai as genai
import markdown
import os
from config import Config

app = Flask(__name__)
app.config.from_object(Config)

# Configure Gemini
genai.configure(api_key=app.config['GEMINI_API_KEY'])


class AcademicAssistant:
    def __init__(self):
        # Lightweight Gemini model
        self.model = genai.GenerativeModel("models/gemini-2.5-flash-lite")

    def generate_content(self, prompt, task_type):
        """
        Generate content using Gemini model based on task type.
        """
        try:
            if task_type == "summarize":
                enhanced_prompt = f"""Summarize the following academic content clearly and concisely.
                Focus on key ideas, methods, and conclusions. 
                Use Markdown formatting with sections and bullet points.

                Content:
                {prompt}"""

            elif task_type == "categorize":
                enhanced_prompt = f"""Analyze and categorize the following academic content.
                Identify the main subject, discipline, related topics, and suitable academic tags.
                Present the result in Markdown with tables and bullet points.

                Content:
                {prompt}"""

            elif task_type == "explain":
                enhanced_prompt = f"""Explain this academic concept in detail using simple language and real-world examples.
                Add Markdown formatting for clarity, and include short explanations, equations, or analogies where useful.

                Concept:
                {prompt}"""

            elif task_type == "quiz":
                enhanced_prompt = f"""Generate a short academic quiz on the following topic.
                - Include 5 multiple choice questions (MCQs)
                - Each question should have options A, B, C, D
                - Mark the correct answer clearly at the end
                - Use Markdown for clean structure

                Topic:
                {prompt}"""

            else:  # generate
                enhanced_prompt = f"""Generate detailed, structured academic content on the following topic.
                Use Markdown for formatting:
                - Headings and subheadings
                - Bullet points and numbered lists
                - Tables or examples if relevant
                - Keep it factual, clear, and formal.

                Topic:
                {prompt}"""

            # Generate content using Gemini
            response = self.model.generate_content(enhanced_prompt)
            return response.text

        except Exception as e:
            print(f"[ERROR] Gemini generation failed: {e}")
            return f"⚠️ Sorry, something went wrong: {str(e)}"


assistant = AcademicAssistant()


def convert_markdown_to_html(markdown_text):
    """
    Convert markdown text to HTML with extensions for better formatting.
    """
    html = markdown.markdown(
        markdown_text,
        extensions=["extra", "codehilite", "toc", "nl2br"],
        extension_configs={
            'codehilite': {
                'use_pygments': True,
                'css_class': 'codehilite'
            }
        }
    )
    return html


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/process', methods=['POST'])
def process_content():
    """
    Handles content processing requests from frontend.
    """
    data = request.get_json()
    content = data.get('content', '')
    task_type = data.get('task_type', 'generate')

    if not content:
        return jsonify({'error': 'No content provided'}), 400

    result = assistant.generate_content(content, task_type)
    html_result = convert_markdown_to_html(result)

    return jsonify({
        'result': html_result,
        'raw_markdown': result,
        'task_type': task_type
    })


if __name__ == '__main__':
    # Run Flask app
    app.run(debug=True, host='0.0.0.0', port=5000)

# Configure Gemini
genai.configure(api_key=app.config['GEMINI_API_KEY'])

class AcademicAssistant:
    def __init__(self):
        self.model = genai.GenerativeModel("models/gemini-2.5-flash-lite")
    
    def generate_content(self, prompt, task_type):
        try:
            if task_type == "summarize":
                enhanced_prompt = f"""Please provide a comprehensive summary of the following academic content. 
                Focus on key points, main arguments, and important findings. Format the response using Markdown with clear headings, bullet points, and sections:
                
                {prompt}"""
            elif task_type == "categorize":
                enhanced_prompt = f"""Analyze and categorize the following academic content. 
                Identify the main subject, field of study, key themes, and suggest appropriate academic categories.
                Format the response using Markdown with tables, bullet points, and clear sections:
                
                {prompt}"""
            elif task_type == "explain":
                enhanced_prompt = f"""Explain the following academic concept in detail, providing examples and practical applications.
                Format the response using Markdown with headings, code blocks (if applicable), bullet points, and examples:
                
                {prompt}"""
            else:  # generate
                enhanced_prompt = f"""Generate comprehensive academic content about:
                
                {prompt}
                
                Please provide well-structured, scholarly content with clear sections. Use Markdown formatting with:
                - Headers (#, ##, ###)
                - Bullet points and numbered lists
                - **Bold** and *italic* text
                - Code blocks if applicable
                - Tables for comparisons
                - Clear section breaks"""
            
            response = self.model.generate_content(enhanced_prompt)
            return response.text
        except Exception as e:
            return f"Error: {str(e)}"

assistant = AcademicAssistant()

def convert_markdown_to_html(markdown_text):
    """Convert markdown text to HTML with proper extensions"""
    html = markdown.markdown(
        markdown_text,
        extensions=[
            'extra',  # Adds tables, footnotes, etc.
            'codehilite',  # Syntax highlighting
            'toc',  # Table of contents
            'nl2br',  # Convert newlines to breaks
        ],
        extension_configs={
            'codehilite': {
                'use_pygments': True,
                'css_class': 'codehilite'
            }
        }
    )
    return html

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/process', methods=['POST'])
def process_content():
    data = request.get_json()
    content = data.get('content', '')
    task_type = data.get('task_type', 'generate')
    
    if not content:
        return jsonify({'error': 'No content provided'}), 400
    
    result = assistant.generate_content(content, task_type)
    
    # Convert markdown to HTML
    html_result = convert_markdown_to_html(result)
    
    return jsonify({
        'result': html_result,
        'raw_markdown': result,  # Keep original markdown if needed
        'task_type': task_type
    })

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)