# Starting part of the sentence
SENTENCE_START = "Code in Place is fun. I learned to program and used Python to make my"

# Prompt the user for words
adjective = input("Please type an adjective and press enter: ")
noun = input("Please type a noun and press enter: ")
verb = input("Please type a verb and press enter: ")

# Combine and display the final sentence
print(f"{SENTENCE_START} {adjective} {noun} {verb}!")
