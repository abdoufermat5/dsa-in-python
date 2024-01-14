import re


def hash_code(s):
    mask = 1 << 32 - 1  # limit to 32-bit
    h = 0
    for c in s:
        h = (h << 5 & mask) | (h >> 27)
        h += ord(c)

    return h


def detect_collision(filename: str):
    with open(filename, "r") as f:
        words = set()
        pattern = re.compile(r"\W+", re.UNICODE)
        for line in f:
            words.update(pattern.sub(" ", line).strip().split())
    hashes = {}
    for word in words:
        h = hash_code(word)
        if h in hashes:
            hashes[h].append(word)
        else:
            hashes[h] = [word]

    return hashes


def detect_collision_using_builtin_hash(filename: str):
    with open(filename, "r") as f:
        words = set()
        pattern = re.compile(r"\W+", re.UNICODE)
        for line in f:
            words.update(pattern.sub(" ", line).strip().split())
    hashes = {}
    for word in words:
        h = hash(word)
        if h in hashes:
            hashes[h].append(word)
        else:
            hashes[h] = [word]

    return hashes


if __name__ == "__main__":
    file_name = "./data/alice-in-wonderland.txt"
    hash_codes = detect_collision(file_name)
    num_words = sum([len(hash_codes[key]) for key in hash_codes])
    print("---------------------------- USING OUR OWN HASH -----------------------------")
    print("----------------------------------------------------------------------------")
    print("Number of words:", num_words)
    print("--------------------------- COLLISION DETAILS ----------------------------")
    for key in hash_codes:
        if len(hash_codes[key]) > 1:
            print(key, hash_codes[key])
    print()
    print("---------------------------- CHECKING --------------------------")
    print("laughter", hash_code("laughter"))
    print("muscular", hash_code("muscular"))
    print()
    print("*" * 80)
    print("*" * 80)
    print()
    print("---------------------------- USING BUILTIN HASH -----------------------------")
    print("----------------------------------------------------------------------------")
    hash_codes = detect_collision_using_builtin_hash(file_name)
    num_words = sum([len(hash_codes[key]) for key in hash_codes])
    print("Number of words:", num_words)
    print("--------------------------- COLLISION DETAILS ----------------------------")
    C = 0
    for key in hash_codes:
        if len(hash_codes[key]) > 1:
            print(key, hash_codes[key])
            C += 1
    if C == 0:
        print("No collision detected")
    print()
    print("---------------------------- CHECKING COLLISION --------------------------")
    print("laughter", hash("laughter"))
    print("muscular", hash("muscular"))
