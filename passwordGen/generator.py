import random 
import string

numberList = [0,1,2,3,4,5,6,7,8,9]
alphabetString = string.ascii_letters
alphabetList = list(alphabetString)
symbolsString = string.punctuation
symbolsList = list(symbolsString)
generatePasswordList = []
check1 = random.randint(1,2)
x = 0

passwordStrength = input("How strong would you like your password to be? Strong or Weak ")
if passwordStrength == "Weak":
    while (x < check1):
        with open("dictionnary.txt", "r") as file:
            allText = file.read()
            words = list(map(str, allText.split()))
            generatePasswordList.append(random.choice(words))
            x += 1
elif passwordStrength == "Strong":
    while (x < 10):
        pickAlph = random.choice(alphabetList)
        pickSym = random.choice(symbolsList)
        pickNum = random.choice(numberList)
        possibleChar = [pickAlph, pickNum, pickSym]
        generatePasswordList.append(random.choice(possibleChar))
        x += 1
else:
    print("Please enter a correct input!")

generatePassword = "".join(map(str, generatePasswordList))

print(generatePassword)

#Write a password generator in Python. Be creative with how you generate passwords - strong passwords have a mix of lowercase letters, uppercase letters, numbers, and symbols. 
#The passwords should be random, generating a new password every time the user asks for a new password.
#Extra:
#Ask the user how strong they want their password to be. For weak passwords, pick a word or two from a list.