# Web-Based Personality Prediction System Through CV Analysis

A **Flask web application** that predicts personality traits from a candidate’s CV using NLP and heuristic analysis. This system analyzes uploaded PDF or DOCX CVs and provides a Big Five personality prediction.

---

## 🌟 Features
- Upload CVs in **PDF** or **DOCX** format.
- Extract text from CVs using **PyPDF2** and **python-docx**.
- Analyze text using **spaCy NLP**.
- Predict Big Five personality traits:  
  - Openness  
  - Conscientiousness  
  - Extraversion  
  - Agreeableness  
  - Neuroticism
- Modern and responsive **UI with Bootstrap 5**.
- Animated **loading spinner** while analysis is running.
- Results displayed in a clean, animated card layout.
- Optionally extendable to export results as PDF or store predictions in a database.

---

## 🧱 Technologies Used
- **Frontend:** HTML, CSS, Bootstrap 5
- **Backend:** Python, Flask
- **NLP:** spaCy
- **Document Parsing:** PyPDF2, python-docx
- **Other Libraries:** werkzeug for secure file handling

---

## ⚙️ Setup & Installation

### 1. Clone the repository
```bash
git clone https://github.com/yourusername/personality_predictor.git
cd personality_predictor
````

### 2. Create a virtual environment

```bash
python -m venv .venv
```

### 3. Activate the virtual environment

* **Windows:**

```bash
.venv\Scripts\activate
```

* **Linux/Mac:**

```bash
source .venv/bin/activate
```

### 4. Install dependencies

```bash
pip install -r requirements.txt
python -m spacy download en_core_web_sm
```

### 5. Run the application

```bash
python app.py
```

Open your browser at `http://127.0.0.1:5000` and start uploading CVs.

---

## 🚀 Deployment

* Compatible with **Render**, **Heroku**, and other cloud platforms.
* Add a `Procfile`:

```text
web: python app.py
```

* Ensure the app listens on all interfaces:

```python
app.run(host='0.0.0.0', port=int(os.environ.get('PORT', 5000)))
```

* Push to GitHub and connect your repo to Render/Heroku.

---

## 🖼️ Screenshots

*(Include screenshots of the upload page, loading spinner, and results page)*

---

## ⚡ Next Steps / Improvements

* Integrate **machine learning models** for more accurate predictions.
* Export personality reports as **PDF**.
* Add **database storage** for CVs and predictions.
* Implement **user authentication** for secure access.
* Add **real-time feedback** and tips for improving CV writing.

---

## 📜 License

MIT License © 2025 Anantha Kumar G

---

## 💡 Notes

* This tool provides **suggestive personality insights** based on CV content; it is not a definitive psychological assessment.
* Always ensure **user privacy** and **data security** when handling CV uploads.

