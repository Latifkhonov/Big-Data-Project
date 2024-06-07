import random
def generateTransitionTable(text, k=4):
    T = {}
    for i in range(len(text) - k):
        seq = text[i:i+k]
        next_char = text[i+k]

        if seq not in T:
            T[seq] = {}
        if next_char not in T[seq]:
            T[seq][next_char] = 0
        T[seq][next_char] += 1
    return T
def convertToProbabilities(T):
    for seq in T:
        total = float(sum(T[seq].values()))
        for char in T[seq]:
            T[seq][char] /= total
    return T

def generateText(T, starting_seq, max_chars=1000):
    sequence = starting_seq
    output = sequence
    for _ in range(max_chars):
        if sequence not in T:
            break
        possible_chars = list(T[sequence].keys())
        possible_probs = list(T[sequence].values())
        next_char = random.choices(possible_chars, weights=possible_probs)[0]
        output += next_char
        sequence = output[len(output)-k:]
    return output

text = "Happy birthday to you, happy birthday to you, happy birthday dear university, happy birthday to you! May you continue to shine and inspire, may you always be the place of higher learning and desire."
T = generateTransitionTable(text)
T = convertToProbabilities(T)
starting_seq = "Happy"
song = generateText(T, starting_seq, max_chars=500)
print(song)