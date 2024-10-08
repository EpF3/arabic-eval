''' Entry point for the program'''
from evaluator import evaluate_all_metrics
from input_handler import process_input

input_data = {
    "prompt": "كيف حالك؟ What do you think?",
    "reply": "كيف حالك",
    'time': 0.5
    }

def main() -> None:
    clean_input = process_input(input_data)
    metrics = evaluate_all_metrics(clean_input)
    print(metrics)

if __name__ == "__main__":
    main()
