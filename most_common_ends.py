from typing import List, Dict, Tuple

def commonEnds(words: List[str]) -> Tuple[Dict[str, int], Dict[str, List[str]]]:
    endings : Dict[str, int] = {}

    words_with_end : Dict[str, List[str]] = {}
    for word in words:
        word_end : str = word[1:]
        if endings.get(word_end) == None:
            endings[word_end] = 1
            words_with_end[word_end] = [word]
        else:
            endings[word_end] += 1
            words_with_end[word_end].append(word)


    return endings, words_with_end

if __name__ == "__main__":
    data = open("list_filtered.txt", "r").read().splitlines()

    endings_dict, words_with_end = commonEnds(data)

    endings = list(endings_dict.items())
    endings.sort(key = (lambda x : x[1]), reverse=True)

    i = 0
    while (endings[i][1] > 3):
        word = endings[i][0]
        print(f"{endings[i][1]} - {word}: {words_with_end[word]}")
        i += 1

    counts = [0 for _ in range(9)]

    for _, count in endings:
        counts[count - 1] += 1

    for i in range(len(counts)-1,-1,-1):
        print(f"There are {counts[i]} groups of endings of size {i + 1}") 