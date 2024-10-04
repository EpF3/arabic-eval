''' Entry point for the program'''
from input_handler import process_input

def main() -> None:
    input_data = {
        "prompt": "كيف حالك؟",
        "reply": "أنا بخير، شكرا!"  # Valid input
    }

    try:
        prompt, reply = process_input(input_data)
        print("Prompt:", prompt)
        print("Reply:", reply)
    except ValueError as err:
        print("Error:", err)

if __name__ == "__main__":
    main()
