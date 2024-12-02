'''Paragraph Metrics'''
from utils import split_into_paragraphs
from metrics.metrics_utils import calculate_cosine_similarity, find_entities, calculate_overlap, calculate_readability, calculate_richness

def evaluate_paragraphs(reply: str) -> dict[str, float]:
    """Evaluate paragraph metrics"""
    paragraphs = split_into_paragraphs(reply)
    coherence = evaluate_coherence(paragraphs)
    entity_consistency = evaluate_entity_consistency(paragraphs)
    readability = evaluate_readability(paragraphs)
    richness = evaluate_richness(paragraphs)
    paragraph_level_metrics = {
        'coherence': coherence,
        'entity_consistency': entity_consistency,
        'readability': readability,
        'richness': richness
    }
    return paragraph_level_metrics

def evaluate_coherence(paragraphs: list[str]) -> float:
    """Evaluate coherence"""
    similarities = []
    for i in range(len(paragraphs)-1):
        tmp = calculate_cosine_similarity(paragraphs[i], paragraphs[i+1])
        similarities.append(tmp)
    # coherence = avg(similarities)
    coherence = 0.5
    return coherence

def evaluate_entity_consistency(paragraphs: list[str]) -> float:
    """Evaluate entity consistency"""
    entities = []
    for i in range(len(paragraphs)):
        tmp = find_entities(paragraphs[i])
        entities.append(tmp)
    overlaps = []
    for i in range(len(entities)-1):
        tmp = calculate_overlap(entities[i], entities[i+1])
        overlaps.append(tmp)
    # entity_consistency = avg(overlaps)
    entity_consistency = 0.5
    return entity_consistency

def evaluate_readability(paragraphs: list[str]) -> float:
    """Evaluate readability"""
    readability_scores = []
    for paragraph in paragraphs:
        tmp = calculate_readability(paragraph)
        readability_scores.append(tmp)
    # readibility = avg(readability_scores)
    readability = 0.5
    return readability

def evaluate_richness(paragraphs: list[str]) -> float:
    """Evaluate richness"""
    richness_scores = []
    for paragraph in paragraphs:
        tmp = calculate_richness(paragraph)
        richness_scores.append(tmp)
    # richness = avg(richness_scores)
    richness = 0.5
    return richness
