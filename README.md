# 💬 Question Answering App

An AI-powered Question Answering application built using Hugging Face Transformers and Streamlit.

This app allows users to input a context paragraph and ask questions related to the text. The model analyzes the context and returns the most relevant answer.

---

## Features
- Interactive web-based UI
- Real-time question answering
- Uses transformer-based NLP models
- Fast and simple interface
- Efficient model loading with Streamlit caching

---

## Technologies Used
- Python
- Streamlit
- Hugging Face Transformers
- DistilBERT
- NLP

---

## Model Used

```python
distilbert-base-uncased-distilled-squad
```

This is a pre-trained transformer model fine-tuned for extractive question answering tasks.

---

## Installation

### 1. Create Virtual Environment

```bash
python -m venv venv
```

### 2. Activate Virtual Environment

#### Windows
```bash
venv\Scripts\activate
```

#### Linux / Mac
```bash
source venv/bin/activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

---

## Run the Application

```bash
streamlit run app.py
```

---

## Project Structure

```text
question-answering-app/
│
├── question.py
├── README.md
```

---

## Example Usage

1. Enter a context paragraph
2. Type a question related to the context
3. Click "Get Answer"
4. View the AI-generated answer instantly

---

## Demo Video
[Demo Video Here.](question-demo_)

---
## CODE
[Check out my python file](question.py)

