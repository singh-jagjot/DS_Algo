# O(n) time | O(n) space
def caesarCipherEncryptor(string, key):
    # Write your code here.
    alpha = list('abcdefghijklmnopqrstuvwxyz')
    key %= 26
    encList = []
    for letter in string:
        encCharKey = (alpha.index(letter) + key) % 26
        encList.append(alpha[encCharKey])
    return ''.join(encList)

# Other solution
def caesarCipherEncryptor(s, key):
    # Write your code here.
    enc = []
    key %= 26
    for ch in s:
        new_ord = ord(ch) + key
        if new_ord > 122:
            new_ord = 96 + (new_ord % 122)
        enc.append(chr(new_ord))
    return ''.join(enc)
