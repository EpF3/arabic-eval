''' Entry point for the program'''
from input_handler import process_input

input_data = {
    "prompt": "كيف حالك؟ What do you think?",
    "reply": "كيف حالك"
    }

def main() -> None:
    try:
        output_data = process_input(input_data)
        print("Prompt:", output_data['prompt'])
        print("Reply:", output_data['reply'])
    except ValueError as err:
        print("Error:", err)

if __name__ == "__main__":
    main()
