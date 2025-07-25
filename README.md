#  Sentiment-Aware Chatbot with Langchain Memory

This is a simple yet powerful chatbot built with [Langchain](https://github.com/langchain-ai/langchain), [Hugging Face Transformers](https://huggingface.co/transformers/), and [Streamlit](https://streamlit.io/). 
The chatbot detects sentiment in user input and responds empathetically, cheerfully, or neutrally .

---

## 💡 Features

-  **Conversation Memory** using Langchain's `ConversationBufferMemory`
-  **Sentiment Detection** using Hugging Face's `distilbert-base-uncased-finetuned-sst-2-english`
-  **Streamlit Chat Interface**

---

## Setup Instructions

### 1. Clone the repository
```bash
git clone https://github.com/Arbin17/Chatbot-with-Langchain-Memory.git
```
### 2.Create a virtual environment
```bash
python -m venv venv
venv/Scripts/activate
```

### 3. Install dependencies
```bash
pip install -r requirements.txt
```
### 4. Run the application
```bash
streamlit run app.py
```