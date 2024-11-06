'''Response Metrics'''

def evaluate_response(reply: str, time: float) -> dict[str, float]:
    """Evaluate response metrics"""
    structure = evaluate_structure(reply)
    presentation = evaluate_presentation(reply)
    cohesion = evaluate_cohesion(reply)
    response_level_metrics = {
        'structure': structure,
        'presentation': presentation,
        'cohesion': cohesion,
        'time': time
    }
    return response_level_metrics

def evaluate_structure(reply: str) -> float:
    """Evaluate structure"""
    structure = 0.5
    return structure

def evaluate_presentation(reply: str) -> float:
    """Evaluate presentation"""
    presentation = 0.5
    return presentation

def evaluate_cohesion(reply: str) -> float:
    """Evaluate cohesion"""
    cohesion = 0.5
    return cohesion
