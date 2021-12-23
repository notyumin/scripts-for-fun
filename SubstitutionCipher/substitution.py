alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"


def generateKeyFromPhrase(keyPhrase: str) -> str:
    keyPhrase = keyPhrase.upper()
    key = ""
    for letter in keyPhrase:
        key = key.__add__(letter)
    for letter in alphabet:
        if key.find(letter) == -1:
            key = key.__add__(letter)

    return key


def encryptMessage(plainText: str, alphabet: str, key: str) -> str:
    cipherText = ""
    for letter in plainText:
        index = alphabet.find(letter.upper())
        # if char is not a letter
        if index != -1:
            cipherLetter = key[index]
        else:
            cipherLetter = letter
        cipherText = cipherText.__add__(cipherLetter)

    return cipherText


def decryptMessage(cipherText: str, alphabet: str, key: str) -> str:
    plainText = ""
    for letter in cipherText:
        index = key.find(letter.upper())
        # if char is not a letter
        if index != -1:
            plainLetter = alphabet[index]
        else:
            plainLetter = letter
        plainText = plainText.__add__(plainLetter)

    return plainText


"""
keyPhrase = "LMAO"
plainText = "Is this the real life?"
key = generateKeyFromPhrase(keyPhrase)
cipherText = encryptMessage(plainText, alphabet, key)
plainText = decryptMessage(cipherText, alphabet, key)
print(cipherText)
print(plainText)
"""

eOrD = input("Enter 'e' to encrypt and 'd' to decrypt")
keyPhrase = input("Please enter key phrase: ")
key = generateKeyFromPhrase(keyPhrase)

if eOrD.lower() == 'e':
    plainText = input("Please enter text to be encrypted: ")
    cipherText = encryptMessage(plainText, alphabet, key)
    print(cipherText)
elif eOrD.lower() == 'd':
    cipherText = input("Please enter text to be decrypted: ")
    plainText = decryptMessage(cipherText, alphabet, key)
    print(plainText)
else:
    print("Invalid option")
