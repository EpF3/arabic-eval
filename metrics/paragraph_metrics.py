'''Paragraph Metrics'''

def evaluate_paragraphs(reply):
    """Evaluate paragraph metrics"""
    coherence = evaluate_coherence()
    entity_consistency = evaluate_entity_consistency()
    readability = evaluate_readability()
    richness = evaluate_richness()
    paragraph_level_metrics = {
        'coherence': coherence,
        'entity_consistency': entity_consistency,
        'readability': readability,
        'richness': richness
    }
    return paragraph_level_metrics

def evaluate_coherence() -> float:
    """Evaluate coherence"""
    coherence = 0.5
    return coherence

def evaluate_entity_consistency() -> float:
    """Evaluate entity consistency"""
    entity_consistency = 0.5
    return entity_consistency

def evaluate_readability() -> float:
    """Evaluate readability"""
    readability = 0.5
    return readability

def evaluate_richness() -> float:
    """Evaluate richness"""
    richness = 0.5
    return richness
