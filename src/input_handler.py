'''The core input processing unit'''
import re
from typing import Dict

def process_input(arabic_input: Dict) -> Dict:
    """
    Process the input dictionary containing 'prompt' and 'reply'.

    Args:
        arabic_input (dict): A dictionary containing 'prompt' and 'reply' strings.
    Returns:
        processed_input (dict): A dictionary containing the validated 'prompt' and 'reply'.
    Raises:
        TypeError: If the input type is incorrect.
        ValueError: If the input format is invalid or if any validation fails.
    """

    # Step 1: Input Validation
    if not isinstance(arabic_input, dict):
        raise TypeError(f"Input must be a dictionary, it is a {type(arabic_input)}")

    # Step 2: Field Extraction
    prompt = arabic_input.get('prompt')
    reply = arabic_input.get('reply')

    # Step 3: Non-Empty Check
    if not isinstance(prompt, str):
        raise TypeError(f"Prompt should be a string, not {type(prompt)}")
    if not isinstance(reply, str):
        raise TypeError(f"Reply should be a string, not {type(reply)}")
    if not prompt.strip():
        raise ValueError("Prompt cannot be empty.")
    if not reply.strip():
        raise ValueError("Reply cannot be empty.")

    # Step 4: Arabic Text Check
    invalid_chars = re.findall(r'[^\\u0600-\\u06FF\\s،؛؟.!(){}[\\]\'\"0-9]', reply)
    if invalid_chars:
        raise ValueError(f"Invalid characters found in 'reply': {', '.join(set(invalid_chars))}. Only Arabic characters and common punctuation are allowed.")

    processed_input = {'prompt': prompt.strip(), 'reply': reply.strip()}
    return processed_input
