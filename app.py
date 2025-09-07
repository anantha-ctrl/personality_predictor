import os
from flask import Flask, render_template, request
import spacy
from PyPDF2 import PdfReader
from docx import Document

UPLOAD_FOLDER = 'uploads'
ALLOWED_EXTENSIONS = {'pdf', 'docx'}

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# Load SpaCy model
nlp = spacy.load('en_core_web_sm')

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

def extract_text(filepath):
    if filepath.endswith('.pdf'):
        text = ''
        reader = PdfReader(filepath)
        for page in reader.pages:
            text += page.extract_text() + ' '
        return text
    elif filepath.endswith('.docx'):
        doc = Document(filepath)
        return ' '.join([para.text for para in doc.paragraphs])
    return ''

def predict_personality(text):
    doc = nlp(text.lower())

    keywords = {
        'Extroversion': ['team', 'lead', 'communication', 'collaborate', 'organized'],
        'Openness': ['creative', 'innovative', 'imagination', 'explore', 'vision'],
        'Conscientiousness': ['organized', 'efficient', 'detail', 'responsible', 'plan'],
        'Agreeableness': ['support', 'help', 'understand', 'cooperate', 'friendly'],
        'Neuroticism': ['stress', 'anxious', 'worry', 'nervous', 'uncertain']
    }

    scores = {trait: 0 for trait in keywords.keys()}

    for token in doc:
        for trait, words in keywords.items():
            if token.lemma_ in words:
                scores[trait] += 1

    total = sum(scores.values()) or 1
    normalized = {k: round((v / total) * 100, 2) for k, v in scores.items()}

    return normalized

@app.route('/', methods=['GET', 'POST'])
def index():
    personality = None
    if request.method == 'POST':
        if 'file' not in request.files:
            return "No file part in the request."

        file = request.files['file']

        if file.filename == '':
            return "No file selected."

        if file and allowed_file(file.filename):
            filepath = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
            file.save(filepath)

            text = extract_text(filepath)
            personality = predict_personality(text)

            os.remove(filepath)  # Clean up after prediction

    return render_template('index.html', personality=personality)

if __name__ == '__main__':
    os.makedirs(UPLOAD_FOLDER, exist_ok=True)
    app.run(debug=True)
