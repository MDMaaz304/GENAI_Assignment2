class AcademicAssistant {
    constructor() {
        this.currentTask = 'generate';
        this.initializeEventListeners();
    }

    initializeEventListeners() {
        // Task buttons
        document.querySelectorAll('.task-btn').forEach(btn => {
            btn.addEventListener('click', (e) => {
                this.setActiveTask(e.target.dataset.task);
            });
        });

        // Process button
        document.getElementById('processBtn').addEventListener('click', () => {
            this.processContent();
        });

        // Ctrl + Enter shortcut
        document.getElementById('contentInput').addEventListener('keydown', (e) => {
            if (e.ctrlKey && e.key === 'Enter') {
                this.processContent();
            }
        });
    }

    setActiveTask(task) {
        this.currentTask = task;

        // Update button UI
        document.querySelectorAll('.task-btn').forEach(btn => btn.classList.remove('active'));
        document.querySelector(`[data-task="${task}"]`).classList.add('active');

        // Change placeholder text based on selected task
        const textarea = document.getElementById('contentInput');
        const placeholders = {
            generate: 'Enter a topic to generate academic content (e.g., "Neural Networks in AI")...',
            summarize: 'Paste text or research article to summarize...',
            categorize: 'Paste content to categorize (e.g., subject or field)...',
            explain: 'Enter a complex concept to get a simple explanation...',
            quiz: 'Enter a topic to generate a short quiz (e.g., "Photosynthesis" or "World War II")...'
        };
        textarea.placeholder = placeholders[task];
    }

    async processContent() {
        const content = document.getElementById('contentInput').value.trim();
        const processBtn = document.getElementById('processBtn');
        const loading = document.getElementById('loading');
        const output = document.getElementById('outputContent');

        if (!content) {
            alert('Please enter some content first.');
            return;
        }

        // Show loading UI
        processBtn.disabled = true;
        processBtn.textContent = 'Processing...';
        loading.style.display = 'block';
        output.innerHTML = '<em>Working on your request...</em>';

        try {
            const response = await fetch('/process', {
                method: 'POST',
                headers: { 'Content-Type': 'application/json' },
                body: JSON.stringify({
                    content: content,
                    task_type: this.currentTask
                })
            });

            const data = await response.json();

            if (response.ok) {
                // If quiz task, format the output differently
                if (this.currentTask === 'quiz') {
                    output.innerHTML = `<div class="quiz-section">${data.result}</div>`;
                } else {
                    output.innerHTML = data.result;
                }
            } else {
                output.innerHTML = `<div class="error">Error: ${data.error}</div>`;
            }
        } catch (error) {
            output.innerHTML = `<div class="error">Error: ${error.message}</div>`;
        } finally {
            processBtn.disabled = false;
            processBtn.textContent = 'Process Content';
            loading.style.display = 'none';
        }
    }
}

document.addEventListener('DOMContentLoaded', () => {
    new AcademicAssistant();
});
// ===== Extra Utilities (Theme Toggle + Copy/Download) =====
document.addEventListener('DOMContentLoaded', () => {
    const themeToggle = document.getElementById('themeToggle');
    const body = document.body;

    if (themeToggle) {
        themeToggle.addEventListener('click', () => {
            body.classList.toggle('dark');
            themeToggle.textContent = body.classList.contains('dark') ? '☀️' : '🌙';
        });
    }

    // Copy output
    const copyBtn = document.getElementById('copyBtn');
    if (copyBtn) {
        copyBtn.addEventListener('click', () => {
            const text = document.getElementById('outputContent').innerText;
            navigator.clipboard.writeText(text);
            copyBtn.textContent = '✅ Copied!';
            setTimeout(() => copyBtn.textContent = '📋 Copy', 1500);
        });
    }

    // Download output
    const downloadBtn = document.getElementById('downloadBtn');
    if (downloadBtn) {
        downloadBtn.addEventListener('click', () => {
            const text = document.getElementById('outputContent').innerText;
            const blob = new Blob([text], { type: 'text/plain' });
            const link = document.createElement('a');
            link.href = URL.createObjectURL(blob);
            link.download = 'output.txt';
            link.click();
        });
    }
});
