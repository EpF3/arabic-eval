'''Paragraph Metrics'''
from utils import split_into_paragraphs, calculate_cosine_similarity, calculate_overlap

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
    sim = []
    for i in range(len(paragraphs)-1):
        tmp = calculate_cosine_similarity(paragraphs[i], paragraphs[i+1])
        sim.append(tmp)
    # sim = avg(sim)
    coherence = 0.5
    return coherence

def evaluate_entity_consistency(paragraphs: list[str]) -> float:
    """Evaluate entity consistency"""
    entities = []
    for i in range(len(paragraphs)):
        tmp = entities(paragraphs[i])
        entities.append(tmp)
    overlap = []
    for i in range(len(entities)-1):
        tmp = calculate_overlap(entities[i], entities[i+1])
        overlap.append(tmp)
    # overlap = avg(overlap)
    entity_consistency = 0.5
    return entity_consistency

def evaluate_readability(paragraphs: list[str]) -> float:
    """Evaluate readability"""
    readability = []
    for paragraph in paragraphs:
        readability = 0.5 # calculate_readability(paragraph)
    # readibility = avg(readability)
    return readability

def evaluate_richness(paragraphs: list[str]) -> float:
    """Evaluate richness"""
    richness = []
    for paragraph in paragraphs:
        readability = 0.5 # calculate_richness(paragraph)
    # richness = avg(richness)
    return richness
