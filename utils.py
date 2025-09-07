import spacy
from PyPDF2 import PdfReader
from docx import Document

nlp = spacy.load('en_core_web_sm')


def extract_text_from_pdf(file_path):
    reader = PdfReader(file_path)
    text = ''
    for page in reader.pages:
        text += page.extract_text() + '\n'
    return text


def extract_text_from_docx(file_path):
    doc = Document(file_path)
    text = ''
    for para in doc.paragraphs:
        text += para.text + '\n'
    return text


def analyze_text(text):
    doc = nlp(text)

    word_count = len([token.text for token in doc if token.is_alpha])
    sentences = list(doc.sents)
    sentence_count = len(sentences)
    avg_sentence_length = word_count / max(sentence_count, 1)

    # Simple heuristic rules
    traits = {
        'Openness': 'High' if 'creative' in text.lower() or 'innovative' in text.lower() else 'Medium',
        'Conscientiousness': 'High' if 'organized' in text.lower() or 'detailed' in text.lower() else 'Medium',
        'Extraversion': 'High' if 'team' in text.lower() or 'collaborated' in text.lower() else 'Medium',
        'Agreeableness': 'High' if 'helped' in text.lower() or 'assisted' in text.lower() else 'Medium',
        'Neuroticism': 'Low' if avg_sentence_length > 20 else 'Medium'
    }

    return traits
