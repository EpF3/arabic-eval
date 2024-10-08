'''Character metrics'''

def evaluate_characters(reply) -> dict[str, float]:
    """Evaluate character metrics"""
    form = evaluate_form()
    modifier = evaluate_modifier()
    ligature = evaluate_ligature()
    sentence_level_metrics = {
        'grammar': form,
        'fluency': modifier
    }
    return sentence_level_metrics

def evaluate_form() -> float:
    """Evaluate form"""
    form = 0.5
    return form

def evaluate_modifier() -> float:
    """Evaluate modifier"""
    modifier = 0.5
    return modifier

def evaluate_ligature() -> float:
    """Evaluate ligature"""
    ligature = 0.5
    return ligature
