message = "Zest1"
def rot13(message):
    res = ""
    for element  in message:
        if str(element).isupper() != True:
            asciiValue = ord(element)
            alphabetIndex = asciiValue - ord('a')
            alphabetIndex = (alphabetIndex + 13) % 26
            asciiValue = alphabetIndex + ord('a')
            res += chr(asciiValue)
        else: 
            asciiValue = ord(element)
            alphabetIndex = asciiValue - ord('A')
            alphabetIndex = (alphabetIndex + 13) % 26
            asciiValue = alphabetIndex + ord('A')
            res += chr(asciiValue)
    return(res)
print(rot13(message))