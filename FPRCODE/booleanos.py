'''
Un año es bisiesto si es divisible entre 4, excepto los divisibles entre 100 y no entre 400. 
'''
a = int(input("Dime el año: "))
bisiesto = a % 400 == 0 or (a%4 == 0 and a % 100 != 0) 
print(f" Es bisiesto: {bisiesto}")
