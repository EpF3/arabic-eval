'''Response Metrics'''

def evaluate_response(reply, time) -> dict[str, float]:
    """Evaluate response metrics"""
    structure = evaluate_structure()
    presentation = evaluate_presentation()
    cohesion = evaluate_cohesion()
    response_level_metrics = {
        'structure': structure,
        'presentation': presentation,
        'cohesion': cohesion,
        'time': time
    }
    return response_level_metrics

def evaluate_structure() -> float:
    """Evaluate structure"""
    structure = 0.5
    return structure

def evaluate_presentation() -> float:
    """Evaluate presentation"""
    presentation = 0.5
    return presentation

def evaluate_cohesion() -> float:
    """Evaluate cohesion"""
    cohesion = 0.5
    return cohesion
