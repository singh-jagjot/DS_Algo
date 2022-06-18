def cce(s: str, key: int) -> str:
    enc = []
    key %= 26
    for ch in s:
        new_ord = ord(ch) + key
        if new_ord > 122:
            new_ord = 96 + (new_ord % 122)
        enc.append(chr(new_ord))
    return ''.join(enc)


print(cce("xyz", 2))

# if you can't use unicode the create an array of the given alphabet and use
# array indices just like you used unicode. For eg see below:


def caesar_cipher_encryptor(string, key):
    new_letters = []
    new_key = key % 26
    alphabet = list("abcdefghijklmnopqrstuvwxyz")
    for letter in string:
        new_letters.append(get_new_letter(letter, new_key, alphabet))
    return "".join(new_letters)


def get_new_letter(letter, key, alphabet):
    new_letter_code = alphabet.index(letter) + key
    return alphabet[new_letter_code] if new_letter_code <= 25 else alphabet[-1 + new_letter_code % 25]


print(caesar_cipher_encryptor('cryptography', 13))