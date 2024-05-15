from flask import Blueprint, request, jsonify
from transformers import pipeline

main = Blueprint('main', __name__)

# Load pre-trained sentiment analysis pipeline
sentiment_pipeline = pipeline("sentiment-analysis")

@main.route('/predict', methods=['POST'])
def predict():
    data = request.json
    text = data['text']
    
    # Analyze sentiment
    result = sentiment_pipeline(text)
    label = result[0]['label']
    
    return jsonify({'sentiment': label})

# Other routes and functions...
