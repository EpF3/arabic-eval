''' Entry point for the program'''
from input_handler import process_input

def main() -> None:
    input_data = {
    "prompt": "كيف حالك؟ What do you think?",
    "reply": "أنا بخير، شكرا! I'm fine, thank you!"
    }
    try:
        output_data = process_input(input_data)
        print("Prompt:", output_data['prompt'])
        print("Reply:", output_data['reply'])
    except ValueError as err:
        print("Error:", err)

if __name__ == "__main__":
    main()
