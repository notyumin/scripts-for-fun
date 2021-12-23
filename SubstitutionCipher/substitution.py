alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"


def getCipherAlpha(keyword: str) -> str:
    keyword = keyword.upper()
    cipherAlphabet = ""
    for letter in keyword:
        cipherAlphabet = cipherAlphabet.__add__(letter)
    for letter in alphabet:
        if cipherAlphabet.find(letter) == -1:
            cipherAlphabet = cipherAlphabet.__add__(letter)

    return cipherAlphabet


def encryptMessage(plainText: str, alphabet: str, cipherAlphabet: str) -> str:
    cipherText = ""
    for letter in plainText:
        index = alphabet.find(letter.upper())
        # if char is not a letter
        if index != -1:
            cipherLetter = cipherAlphabet[index]
        else:
            cipherLetter = letter
        cipherText = cipherText.__add__(cipherLetter)

    return cipherText


def decryptMessage(cipherText: str, alphabet: str, cipherAlphabet: str) -> str:
    plainText = ""
    for letter in cipherText:
        index = cipherAlphabet.find(letter.upper())
        # if char is not a letter
        if index != -1:
            plainLetter = alphabet[index]
        else:
            plainLetter = letter
        plainText = plainText.__add__(plainLetter)

    return plainText


"""
keyword = "LMAO"
plainText = "Is this the real life?"
cipherAlphabet = generateKeyFromPhrase(keyword)
cipherText = encryptMessage(plainText, alphabet, cipherAlphabet)
plainText = decryptMessage(cipherText, alphabet, cipherAlphabet)
print(cipherText)
print(plainText)
"""

eOrD = input("Enter 'e' to encrypt and 'd' to decrypt: ")
keyword = input("Please enter keyword: ")
cipherAlphabet = getCipherAlpha(keyword)

if eOrD.lower() == 'e':
    plainText = input("Please enter text to be encrypted: ")
    cipherText = encryptMessage(plainText, alphabet, cipherAlphabet)
    print(cipherText)
elif eOrD.lower() == 'd':
    cipherText = input("Please enter text to be decrypted: ")
    plainText = decryptMessage(cipherText, alphabet, cipherAlphabet)
    print(plainText)
else:
    print("Invalid option")
