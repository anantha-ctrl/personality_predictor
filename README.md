# 🌟 Personality Prediction System Through CV Analysis

A simple web-based system that analyzes uploaded PDF or DOCX CV files and predicts personality traits based on keyword analysis using NLP (SpaCy).

---

## 🚀 Features

- Upload CV in PDF or DOCX format.
- Extract text content from the document.
- Analyze text for personality traits:  
  - Extroversion  
  - Openness  
  - Conscientiousness  
  - Agreeableness  
  - Neuroticism  
- Display prediction results in a sleek, responsive interface using Bootstrap.

---

## ⚙️ Tech Stack

- 🐍 Python 3.x
- 🚀 Flask
- 📚 SpaCy (for NLP analysis)
- 📄 PyPDF2 (for PDF text extraction)
- 📃 python-docx (for DOCX file handling)
- 🎨 Bootstrap 5 (for front-end design)

---

## 📁 Project Structure

```

personality\_predictor/
├── app.py
├── requirements.txt
├── templates/
│   └── index.html
├── uploads/        # Temp folder for uploaded CVs
├── README.md

````

---

## ✅ Installation & Setup

1. Clone the repo:
    ```bash
    git clone https://github.com/your-username/personality_predictor.git
    cd personality_predictor
    ```

2. Create and activate a virtual environment:
    ```bash
    python -m venv .venv
    .venv\Scripts\activate      # Windows
    source .venv/bin/activate   # Mac/Linux
    ```

3. Install dependencies:
    ```bash
    pip install -r requirements.txt
    ```

4. Download SpaCy language model:
    ```bash
    python -m spacy download en_core_web_sm
    ```

5. Run the app:
    ```bash
    python app.py
    ```

6. Open your browser and visit:
    ```
    http://127.0.0.1:5000/
    ```

---

## 🚀 Usage

1. Upload your PDF or DOCX CV.
2. Click **Predict Personality**.
3. View the personality trait prediction results displayed in a clean interface.

---

## 🎯 Future Improvements

- Use a trained ML model instead of keyword analysis for real prediction accuracy.
- Add graphs (Chart.js) to visualize personality traits.
- Add user authentication.
- Save prediction history in a database.

---

## 📜 License

This project is open-source and available under the MIT License.

---

💡 Feel free to ⭐ the project if you find it useful!
````


Want me to help you write a fancy LICENSE file or integrate database logging next? 🌟
