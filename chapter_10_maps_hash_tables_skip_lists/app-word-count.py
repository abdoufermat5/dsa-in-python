import re


def cleanup_and_count(s):
    pattern = re.compile(r"\W+", re.UNICODE)
    res = pattern.sub(" ", s).strip().split()
    freq = {}
    for w in res:
        freq[w] = freq.get(w, 0) + 1
    return freq


def word_count1(filename: str):
    with open(filename, "r") as f:
        frequency = {}
        for line in f:
            freq = cleanup_and_count(line.strip().lower())
            for key in freq:
                frequency[key] = frequency.get(key, 0) + freq[key]
    frequency = sorted(frequency.items(), key=lambda x: x[1], reverse=True)
    return frequency


if __name__ == "__main__":
    file_name = "./data/alice-in-wonderland.txt"
    print(*word_count1(file_name), sep="\n")
