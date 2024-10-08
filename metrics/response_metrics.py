'''Response Metrics'''

async def evaluate_response(reply, time):
    """Evaluate response metrics"""
    structure = evaluate_structure(reply)
    presentation = evaluate_presentation(reply)
    cohesion = evaluate_cohesion(reply)
    time_score = evaluate_time_score(time)
    response_level_metrics = {
        'structure': structure,
        'presentation': presentation,
        'cohesion': cohesion,
        'time_score': time_score
    }
    return response_level_metrics
