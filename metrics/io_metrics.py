'''I/O Metrics'''

async def evaluate_io(prompt, reply):
    """Evaluate I/O metrics"""
    relevance = evaluate_relevance(prompt, reply)
    completeness = evaluate_completeness(prompt, reply)
    cost = evaluate_cost(prompt, reply)
    adherance = evaluate_adherance(reply, GUIDELINES)
    io_level_metrics = {
        'relevance': relevance,
        'completeness': completeness,
        'cost': cost,
        'adherance': adherance
    }
    return io_level_metrics
