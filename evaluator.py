'''Defines all the evaluation metrics at all levels'''
from metrics.io_metrics import evaluate_io
from metrics.response_metrics import evaluate_response
from metrics.paragraph_metrics import evaluate_paragraphs
from metrics.sentence_metrics import evaluate_sentences
from metrics.word_metrics import evaluate_words
from metrics.character_metrics import evaluate_characters

def evaluate_all_metrics(ip):
    """Evaluate all metrics"""
    io_level_metrics = evaluate_io()
    response_level_metrics = evaluate_response()
    paragraph_level_metrics = evaluate_paragraphs()
    sentence_level_metrics = evaluate_sentences()
    word_level_metrics = evaluate_words()
    character_level_metrics = evaluate_characters()
    return {
        'io_level_metrics': io_level_metrics,
        'response_level_metrics': response_level_metrics,
        'paragraph_level_metrics': paragraph_level_metrics,
        'sentence_level_metrics': sentence_level_metrics,
        'word_level_metrics': word_level_metrics,
        'character_level_metrics': character_level_metrics,
    }
