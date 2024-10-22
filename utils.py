'''Utility functions for the entire system.'''
import re
from polyglot.text import Text
def store_results(metric_type: str, results: dict) -> None:
    """Store evaluation results in a database or log them."""
    print(f"Storing {metric_type} metrics: {results}")

def word_filter(words: list[str]) -> list[str]:
    """Filters list of words for punctuation"""
    valid_arabic_regex = re.compile(r'^[\u0600-\u06FF]+$')
    contraction_regex = re.compile(r"^'.+|.+'$")
    punctuation = '،؟":;!–‘“”'
    filtered_words = []
    for word in words:
        stripped_word = word.strip(punctuation)
        if not stripped_word:
            continue
        if valid_arabic_regex.match(stripped_word):
            filtered_words.append(stripped_word)
        elif contraction_regex.match(stripped_word):
            filtered_words.append(stripped_word)
    return filtered_words

def split_into_paragraphs(text: str) -> list[str]:
    """Splits a body of text into paragraphs"""
    paragraphs = re.split(r'\n\s*|\r\n\s*|\r\s*', text.strip())
    paragraphs = [para.strip() for para in paragraphs if para.strip()]
    return paragraphs

def split_into_words(text: str) -> list[str]:
    """Splits a body of text into a words"""
    polyglot_text = Text(text, hint_language_code='ar')
    words = [word.string for word in polyglot_text.words]
    filtered_words = word_filter(words)
    return filtered_words

def split_into_sentences(text: str) -> list[str]:
    """Splits a body of text into sentences"""
    polyglot_text = Text(text, hint_language_code='ar')
    sentences = [sent.string for sent in polyglot_text.sentences]
    return sentences
