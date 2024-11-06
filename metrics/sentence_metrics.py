'''Sentence Metrics'''

from utils import split_into_sentences


def evaluate_sentences(reply: str) -> dict[str, float]:
    """Evaluate paragraph metrics"""
    sentences = split_into_sentences(reply)
    grammar = evaluate_grammar(sentences)
    fluency = evaluate_fluency(sentences)
    verbosity = evaluate_verbosity(sentences)
    sentence_level_metrics = {
        'grammar': grammar,
        'fluency': fluency,
        'verbosity': verbosity,
    }
    return sentence_level_metrics

def evaluate_grammar(sentences: list[str]) -> float:
    """Evaluate grammar"""
    grammar = 0.5
    return grammar

def evaluate_fluency(sentences: list[str]) -> float:
    """Evaluate fluency"""
    fluency = 0.5
    return fluency

def evaluate_verbosity(sentences: list[str]) -> float:
    """Evaluate verbosity"""
    verbosity = 0.5
    return verbosity
