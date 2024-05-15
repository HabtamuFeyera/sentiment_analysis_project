import torch
from transformers import BertForSequenceClassification

class SentimentModel:
    def __init__(self, model_path, tokenizer):
        self.model = BertForSequenceClassification.from_pretrained(model_path)
        self.tokenizer = tokenizer
    
    def predict(self, text):
        inputs = self.tokenizer.encode_plus(
            text,
            add_special_tokens=True,
            max_length=128,
            pad_to_max_length=True,
            return_attention_mask=True,
            return_tensors='pt'
        )
        
        input_ids = inputs['input_ids']
        attention_mask = inputs['attention_mask']
        
        with torch.no_grad():
            outputs = self.model(input_ids, attention_mask=attention_mask)
        
        logits = outputs[0]
        prediction = torch.argmax(logits, dim=1).item()
        
        return 'positive' if prediction == 1 else 'negative'
