import subprocess as sp

def clscreen():
	tmp = sp.call('clear',shell=True)

exit = 0
while exit == 0:
	
	op = int(input("Input: 1 - Fahrenheit\n       2 - Celsius\n       3 - Kelvin\n       0 - Exit\n"))
	if op == 0: 
		clscreen()
		break

	elif op == 1:
		clscreen()
		x = float(input("Value: "))
		print(x,"Fahrenheit is",round(5/9*(x-32),2),"Celsius")
		print(x,"Fahrenheit is",round(5/9*(x-32)+273,2),"Kelvin")	

	elif op == 2:
		clscreen()
		x = float(input("Value: "))
		print(x,"Celsius is",round(((9/5)*x)+32,2),"Fahrenheit")		
		print(x,"Celsius is",round(x-273.15,2),"Kelvin")

	elif op == 3:
		clscreen()
		x = float(input("Value: "))
		print(x,"Kelvin is",round(9/5*(x-273)+32,2),"Fahrenheit")		
		print(x,"Kelvin is",round(x+273.15,2),"Celsius")

	
	input()
	clscreen()