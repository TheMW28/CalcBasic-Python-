#addition
def addition(Num1, Num2):
	return Num1 + Num2

#subtraktion
def subtraktion(Num1, Num2):
	return Num1 - Num2

#multiplikation
def multiplikation(Num1, Num2):
	return Num1 * Num2

#divison
def division(Num1, Num2):
	return Num1 / Num2
	
def main():
	Var1 = int(input("1.Zahl : "))
	Var2 = int(input("2.Zahl : "))
	operation = input("Womit soll gerechnet werden? (+,-,*,/) : ")
	if (operation != "+" and operation != "-" and operation != "*" and operation != "/"):
		print("Falsches Rechenzeichen")
	else:
		if (operation == "+"):
			print(addition(Var1, Var2))
		elif (operation == "-"):
			print(subtraktion(Var1, Var2))
		elif (operation == "*"):
			print(multiplikation(Var1, Var2))
		elif (operation == "/"):
			print(division(Var1, Var2))

		
main()