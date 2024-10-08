'''Defines all the evaluation metrics at all levels'''

import logging
from typing import Dict
from metrics.io_metrics import evaluate_io
from metrics.response_metrics import evaluate_response
from metrics.paragraph_metrics import evaluate_paragraph
from metrics.sentence_metrics import evaluate_sentence
from metrics.word_metrics import evaluate_word
from metrics.character_metrics import evaluate_character
from utils import split_text, average_metrics

# Mapping of levels to their corresponding async evaluation functions
EVALUATION_FUNCTIONS = {
    'paragraph': evaluate_paragraph,
    'sentence': evaluate_sentence,
    'word': evaluate_word,
    'character': evaluate_character
}

async def evaluate_all(input_data: Dict[str, str]) -> Dict:
    """Asynchronously evaluate all metrics"""
    prompt = input_data.get('prompt')
    reply = input_data.get('reply')
    time = input_data.get('time')

    logging.info('Starting evaluation of all metrics...')    
    io_level_result = await evaluate_io_level(prompt, reply)
    logging.info('I/O level evaluation complete')
    response_level_result = await evaluate_response_level(reply, time)
    logging.info('Response level evaluation complete')
    paragraph_level_result = await evaluate_text_level(reply, 'paragraph')
    logging.info('Paragraph level evaluation complete')
    sentence_level_result = await evaluate_text_level(reply, 'sentence')
    logging.info('Sentence level evaluation complete')
    word_level_result = await evaluate_text_level(reply, 'word')
    logging.info('Word level evaluation complete')
    character_level_result = await evaluate_text_level(reply, 'character')
    logging.info('Character level evaluation complete')
    logging.info('All evaluations completed successfully.')

    return {
        'io_level': io_level_result,
        'response_level': response_level_result,
        'paragraph_level': paragraph_level_result,
        'sentence_level': sentence_level_result,
        'word_level': word_level_result,
        'character_level': character_level_result,
    }

async def evaluate_io_level(prompt: str, reply: str) -> Dict:
    """Asynchronously evaluates I/O level metrics"""
    logging.info('Starting I/O level evaluation...')
    result = await evaluate_io(prompt, reply)
    logging.info('I/O level evaluation complete')
    return result

async def evaluate_response_level(reply: str, time: str) -> Dict:
    """Asynchronously evaluates response level metrics"""
    logging.info('Starting response level evaluation...')
    result = await evaluate_response(reply, time)
    logging.info('Response level evaluation complete')
    return result

async def evaluate_text_level(reply: str, level: str) -> Dict:
    """Generalized function to asynchronously evaluate at a specific text level: paragraph, sentence, word, character)"""
    logging.info(f'Starting {level} level evaluation...')
    split_elements = split_text(reply, level)
    evaluation_function = EVALUATION_FUNCTIONS[level]

    aggregate_metrics = []
    for element in split_elements:
        logging.info(f'Evaluating {level}: {element}')
        element_metrics = await evaluation_function(element)
        aggregate_metrics.append(element_metrics)
        logging.info(f'{level} evaluation for {element} complete')
    logging.info(f'{level} level evaluation complete')

    return average_metrics(aggregate_metrics, level)  # Synchronous average function