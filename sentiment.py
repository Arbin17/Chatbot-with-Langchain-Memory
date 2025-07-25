from transformers import pipeline

# Load sentiment analysis model (Hugging Face)
sentiment_pipeline = pipeline("sentiment-analysis", model="distilbert-base-uncased-finetuned-sst-2-english")

def get_sentiment(text):
    result = sentiment_pipeline(text)[0]
    return result['label'], result['score']
