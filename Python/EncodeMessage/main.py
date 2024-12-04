
alphabet = [
    "a", "b", "c", "d", "e", "f", "g", "h", "i", "j",
    "k", "l", "m", "n", "o", "p", "q", "r", "s", "t",
    "u", "v", "w", "x", "y", "z"
]

def decision():
    decision = str(input("Type 'encode' to encrypt, type 'decode' to decrypt :"))

    if decision == "encode":
        name, location = nameAndLocation()
        encode(name, location)
    elif decision == "decode":
        name, location = nameAndLocation()
        decode(name, location)
    else:
        return print("Decision unavailable.")

def nameAndLocation():
    name = str(input("Type your message: "))
    location = int(input("Type your shift number: "))
    return name, location

def encode(name, location):
    global alphabet

    encodeMessage = []
    for letterName in name:
        for letterAlphabet in alphabet:
            if letterName == letterAlphabet:
                index = alphabet.index(letterAlphabet)
                newIndex = index + location
                if newIndex > 25:
                    residual = newIndex - 25
                    newIndex = residual - 1
                else:
                    pass
                newLetterName = alphabet[newIndex]
                break
        encodeMessage.append(newLetterName)

    encodedMessage = "".join(encodeMessage)

    return print(f"The encoded message is {encodedMessage}")

def decode(name, location):
    decodeMessage = []
    for letterName in name:
        for letterAlphabet in alphabet:
            if letterName == letterAlphabet:
                index = alphabet.index(letterAlphabet)
                newIndex = index - location
                if newIndex < 0:
                    residual = 25 + newIndex
                else:
                    pass
                newLetterName = alphabet[newIndex]
                break
        decodeMessage.append(newLetterName)
    decodedMessage = "".join(decodeMessage)

    return print(f"The encoded message is {decodedMessage}")


decision()





