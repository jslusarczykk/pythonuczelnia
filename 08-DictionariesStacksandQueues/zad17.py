dic = {
    "A": "Argentine",
    "B": "Bravo",
    "C": "Charlie",
    "D": "Delta",
    "E": "Echo",
    "F": "Foxtrot",
    "G": "Golf",
    "H": "Hotel",
    "I": "India",
    "J": "Juliet",
    "K": "Kilo",
    "L": "Lima",
    "M": "Mike",
    "N": "November",
    "O": "Oscar",
    "P": "Papa",
    "Q": "Quebec",
    "R": "Romeo",
    "S": "Sierra",
    "T": "Tango",
    "U": "Uniform",
    "V": "Victor",
    "W": "Whiskey",
    "X": "X-ray",
    "Y": "Yankee",
    "Z": "Zulu"
}

#spell your name and 3 other words
def bigL(dana):
    output=""
    for i in range(len(dana)):
        output+=dana[i].upper()
    return output

def ICAO(word):
    final_words=""
    word=bigL(word)
    for i in range(len(word)):
        final_words+=dic[word[i]]
        final_words+=" "
    return final_words

print(ICAO("slusarczyk"))