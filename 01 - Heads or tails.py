import random

x = int(input("0 for tails / 1 for heads: "))

if random.randint(0,100)%2 == x:
	print ("You've won!")
else:
	print ("You've lost :(")
