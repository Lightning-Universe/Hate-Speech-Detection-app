"""This module implements the demo for Hate speech detection model.

This demo is inspired from the work of []().
Checkout the original implementation [here](()

The app integration is done at `research_app/components/model_demo.py`.
"""
import torch
from loguru import logger
from transformers import AutoModelForSequenceClassification, AutoTokenizer


class HPDModel:
    def __init__(self):
        self.tokenizer = AutoTokenizer.from_pretrained("Hate-speech-CNERG/english-abusive-MuRIL")
        self.model = AutoModelForSequenceClassification.from_pretrained("Hate-speech-CNERG/english-abusive-MuRIL")

    @torch.no_grad()
    def predict(self, x: str):
        logger.debug(f"received request:{x}")
        inputs = self.tokenizer(x, return_tensors="pt")
        logits = self.model(**inputs).logits
        predicted_class_id = logits.argmax().item()
        result = self.model.config.id2label[predicted_class_id]
        if result == "LABEL_0":
            return "Normal"
        else:
            return "Abusive"
