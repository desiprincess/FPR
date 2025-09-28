import random 
n = random.randint(1,100)
a = int(input("He elegido un numero del 1 al 100, intenta adivinarlo: ")) 
while a!= n:

if a > n: 
    print("El número es mayor") 
elif a < n: 
    print("El número es menor")
else: 
    print("Has adivinado el número")
