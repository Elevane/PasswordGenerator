import random, string

LENGTH = 20 
characters = ['lowerLetter','number', 'upperLetter','ponctuation']
ponctuation = ['?', '!', ';', ':', '/', '§', '.', '%', 'µ', '^']
LowerCaseLetters = list(string.ascii_lowercase)
UpperCaseLetters = list(string.ascii_uppercase)


lenCharacters = len(characters) -1
lenLowerCase = len(LowerCaseLetters) -1
lenUpperCase = len(UpperCaseLetters) -1
lenPonctuation = len(ponctuation) - 1



def generate():
    password = ""
    for l in range(LENGTH) :
        randomChar = characters[random.randint(0, lenCharacters )]
        if randomChar == "lowerLetter":
            password += LowerCaseLetters[random.randint(0, lenLowerCase)]
            
        elif randomChar == "number":
            password += str(random.randint(0, 9))
        
        elif randomChar =="upperLetter":
            password += UpperCaseLetters[random.randint(0, lenUpperCase)]
        
        elif randomChar == "ponctuation":
            password += ponctuation[random.randint(0, lenPonctuation)]

    return password


password = generate()
print(password)