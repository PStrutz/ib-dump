#string methods




def length_of_sentence(sentence):
    return len(sentence)

#breaks long string into tokens and compiles into list
def tokenize(sentence):
    words = []
    for letter in sentence:
        last_space = 0
        if letter == ' ' or letter == "." or letter == "!" or letter == "?":
            words.append(sentence[last_space:sentence.find(letter)])
            last_space = sentence.find(letter) + 1
            sentence = sentence[last_space:]
    print(words)
    return words


def main():
    sentence = input("Input a compatible sentence: ")
    sentence = tokenize(sentence)
    print("Length: ", length_of_sentence(sentence))
    new_sentence = sorted(sentence)
    print("Rearranged alphabetically: ")
    print(new_sentence)

main()
    



