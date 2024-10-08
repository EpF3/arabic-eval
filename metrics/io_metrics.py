'''I/O Metrics'''

def evaluate_io(prompt, reply) -> dict[str, float]:
    """Evaluate I/O metrics"""
    relevance = evaluate_relevance()
    completeness = evaluate_completeness()
    cost = evaluate_cost()
    adherance = evaluate_adherance()
    io_level_metrics = {
        'relevance': relevance,
        'completeness': completeness,
        'cost': cost,
        'adherance': adherance
    }
    return io_level_metrics

def evaluate_relevance() -> float:
    """Evaluate relevance"""
    relevance = 0.5
    return relevance

def evaluate_completeness() -> float:
    """Evaluate completeness"""
    completeness = 0.5
    return completeness

def evaluate_adherance() -> float:
    """Evaluate adherance"""
    adherance = 0.5
    return adherance

def evaluate_cost() -> float:
    """Evaluate cost"""
    cost = 0.5
    return cost
