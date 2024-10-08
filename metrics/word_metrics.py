''' Word Metrics'''

def evaluate_words(reply):
    """Evaluate word metrics"""
    syntax = evaluate_syntax()
    grammar = evaluate_grammar()
    pos = evaluate_pos()
    semantics = evaluate_semantics()
    paragraph_level_metrics = {
        'syntax': syntax,
        'grammar': grammar,
        'pos': pos,
        'semantics': semantics
    }
    return paragraph_level_metrics

def evaluate_syntax() -> float:
    """Evaluate syntax"""
    syntax = 0.5
    return syntax

def evaluate_grammar() -> float:
    """Evaluate grammar"""
    grammar = 0.5
    return grammar

def evaluate_pos() -> float:
    """Evaluate part of speech"""
    pos = 0.5
    return pos

def evaluate_semantics() -> float:
    """Evaluate semantic appropriateness"""
    semantics = 0.5
    return semantics
