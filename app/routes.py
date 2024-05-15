from flask import Blueprint, request, jsonify, render_template
from transformers import BertTokenizer
from .model.py import SentimentModel

main = Blueprint('main', __name__)

# Load model and tokenizer
model_path = "path_to_saved_model"
tokenizer = BertTokenizer.from_pretrained('bert-base-uncased')
model = SentimentModel(model_path, tokenizer)

@main.route('/')
def index():
    return render_template('index.html')

@main.route('/predict', methods=['POST'])
def predict():
    data = request.json
    text = data['text']
    sentiment = model.predict(text)
    return jsonify({'sentiment': sentiment})
