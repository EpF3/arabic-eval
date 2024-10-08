'''Utility functions for the entire system.'''
import re
import spacy

# Load the Arabic NLP model
nlp = spacy.load("ar_core_news_sm")

def split_text(text: str, level: str) -> list:
    if level == 'paragraph':
        return re.split(r'\n\n+', text.strip())
    elif level == 'character':
        return list(text.strip())
    elif level == 'sentence':
        doc = nlp(text)
        return [sent.text for sent in doc.sents]
    elif level == 'word':
        doc = nlp(text)
        return [token.text for token in doc]
    else:
        raise ValueError(f'Unsupported level: {level}')

def average_metrics(metrics: list, level: str) -> dict:
    if not metrics:
        return {}
    average_result = {}
    num_metrics = len(metrics)
    for key in metrics[0].keys():
        average_result[key] = sum([m[key] for m in metrics]) / num_metrics
    return {f'{level}_average': average_result}

def store_results(metric_type: str, results: dict) -> None:
    """Store evaluation results in a database or log them."""
    print(f"Storing {metric_type} metrics: {results}")
