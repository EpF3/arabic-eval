'''Sentence Metrics'''

def evaluate_sentences(reply) -> dict[str, float]:
    """Evaluate paragraph metrics"""
    grammar = evaluate_grammar()
    fluency = evaluate_fluency()
    verbosity = evaluate_verbosity()
    sentence_level_metrics = {
        'grammar': grammar,
        'fluency': fluency,
        'verbosity': verbosity,
    }
    return sentence_level_metrics

def evaluate_grammar() -> float:
    """Evaluate grammar"""
    grammar = 0.5
    return grammar

def evaluate_fluency() -> float:
    """Evaluate fluency"""
    fluency = 0.5
    return fluency

def evaluate_verbosity() -> float:
    """Evaluate verbosity"""
    verbosity = 0.5
    return verbosity
