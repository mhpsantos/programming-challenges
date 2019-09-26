alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z','A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9', ' ','\n']
total = 64
ratio = 15
import os
def cipher_letter(letter):
	a = (alphabet.index(letter))
	if (a+ratio)>total:
		a = (a+ratio)-total
	else:
		a=a+ratio
	return alphabet[a]

def cipher(string):	
	string = list(string)
	for x in range(len(string)):
		string[x] = cipher_letter(string[x])
	string = "".join(string)
	return string

def decipher_letter(letter):
	a = (alphabet.index(letter))
	if(a-ratio)<0:
		a = (total+a)-ratio
	else:
		a=a-ratio
	return alphabet[a]

def decipher(string):
	string = list(string)
	for x in range(len(string)):
		string[x] = decipher_letter(string[x])
	string = "".join(string)
	return string
def createfile():
        f = open("input.txt", "w+")

file = open("input.txt", "r+")
inputfile= file.read()
file.close

file = open("output.txt","w+")
outputfile = file.read()

print(" (C)reate input file")
print("C(Y)pher input file")
print(" (D)ecipher input file")
print(" (T)ype to cipher")
a = input("Choose an option: ")

os.system('cls' if os.name == 'nt' else 'clear')

if a== 't' or a == 'T':
	a=input("Type to cipher: ")
	for x in range(len(a)):
		file.write(cipher(a[x]))

if a == 'C' or a == 'c':
    b = input("Are you sure?")
    if a == 'Y' or a == 'y':
        createfile()

os.system('cls' if os.name == 'nt' else 'clear')

if a == 'Y' or a == 'y':
	for x in range(len(inputfile)):
		file.write(cipher(inputfile[x]))

if a == 'D' or a == 'd':
	for x in range(len(inputfile)):
		file.write(decipher(inputfile[x]))

file.close
