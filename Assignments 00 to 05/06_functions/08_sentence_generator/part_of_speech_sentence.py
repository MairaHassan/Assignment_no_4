# part_of_speech_sentence.py

def make_sentence(word, part_of_speech):
    """
    Prints a sentence based on the part of speech and the word provided.

    Parameters:
        word (str): The word to insert into the sentence.
        part_of_speech (int): 0 for noun, 1 for verb, 2 for adjective.
    """
    if part_of_speech == 0:
        print(f"I am excited to add this {word} to my vast collection of them!")
    elif part_of_speech == 1:
        print(f"It's so nice outside today it makes me want to {word}!")
    elif part_of_speech == 2:
        print(f"Looking out my window, the sky is big and {word}!")
    else:
        print("Invalid part of speech. Please enter 0, 1, or 2.")

def main():
    word = input("Please type a noun, verb, or adjective: ")
    try:
        part = int(input("Is this a noun, verb, or adjective? Type 0 for noun, 1 for verb, 2 for adjective: "))
        make_sentence(word, part)
    except ValueError:
        print("Invalid input. Please enter a number (0, 1, or 2).")

if __name__ == "__main__":
    main()
