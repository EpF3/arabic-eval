'''I/O Metrics'''
from settings import logger, COST_PER_PROMPT_TOKEN, COST_PER_REPLY_TOKEN
from utils import count_tokens

def evaluate_io(prompt: str, reply: str) -> dict[str, float]:
    """Evaluate I/O metrics"""
    relevance = evaluate_relevance(prompt, reply)
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

def evaluate_relevance(prompt: str, reply: str) -> float:
    """Evaluate relevance"""
    relevance = 0.5
    return relevance

def evaluate_completeness(prompt: str, reply: str) -> float:
    """Evaluate completeness"""
    completeness = 0.5
    return completeness

def evaluate_adherance(prompt: str, reply: str) -> float:
    """Evaluate adherance"""
    adherance = 0.5
    return adherance

def evaluate_cost(prompt: str, reply: str) -> float:
    """Evaluate cost"""
    prompt_tokens = count_tokens(prompt)
    prompt_cost = COST_PER_PROMPT_TOKEN * prompt_tokens
    logger.info(f"Prompt: \"{prompt[:10]}\" || Length: {prompt_tokens} || Cost: {prompt_cost}")
    reply_tokens = count_tokens(reply)
    reply_cost = COST_PER_REPLY_TOKEN * reply_tokens
    logger.info(f"Reply: \"{reply[:10]}\" || Length: {reply_tokens} || Cost: {reply_cost}")
    cost = prompt_cost + reply_cost
    return cost
