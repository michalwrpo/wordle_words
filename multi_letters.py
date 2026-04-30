from typing import List, Tuple

# returns the list of words that contain only three letters
# the first list contains words with a triple letter
# the second list contains words with two double letters
# the second list contains words with double letter
def multiLetters(words: List[str]) -> Tuple[List[str], List[str], List[str]]:
    triple = []
    doublepair = []
    double = []

    for word in words:
        counts = [word.count(chr(letter)) for letter in range(ord('A'), ord('Z')+1)]
        has_double = False
        for c in counts:
            if (c == 3):
                triple.append(word)
                break
            elif (c == 2):
                if has_double:
                    doublepair.append(word)
                else:
                    has_double = True
                    double.append(word)            

    return triple, doublepair, double


if __name__ == "__main__":
    data = open("list_filtered.txt", "r").read().splitlines()

    triple, doublepair, double = multiLetters(data)

    print(f"Words with three letters [{len(triple)}]")
    for word in triple:
        print(word, end=", ")
    print("\b\b ")

    print(f"Words with two double letters [{len(doublepair)}]")
    for word in doublepair:
        print(word, end=", ")
    print("\b\b ")

    print(f"Words with double letters [{len(double)}]")
    for word in double:
        print(word, end=", ")
    print("\b\b ")
