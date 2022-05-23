def cce(s: str, key: int) -> str:
    enc = []
    key %= 26
    for ch in s:
        newOrd = ord(ch) + key
        if newOrd > 122:
            newOrd = 96 + (newOrd % 122)
        enc.append(chr(newOrd))
    return ''.join(enc)


print(cce("xyz", 2))

# if you can't use unicode the create an array of the given alphabet and use
# array indices just like you used unicode. For eg see below:


def caesarCipherEncryptor(string, key):
    newLetters = []
    newKey = key % 26
    alphabet = list("abcdefghijklmnopqrstuvwxyz")
    for letter in string:
        newLetters.append(getNewLetter(letter, newKey, alphabet))
    return "".join(newLetters)


def getNewLetter(letter, key, alphabet):
    newLetterCode = alphabet.index(letter) + key
    return alphabet[newLetterCode] if newLetterCode <= 25 else alphabet[-1 + newLetterCode % 25]

print(caesarCipherEncryptor('xyz', 2))