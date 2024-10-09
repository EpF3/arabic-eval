'''Utility functions for the entire system.'''

def store_results(metric_type: str, results: dict) -> None:
    """Store evaluation results in a database or log them."""
    print(f"Storing {metric_type} metrics: {results}")
