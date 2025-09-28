'''
Le pedimos al dividendo y el divisor (numeros enteros) al usuario y luego mostramos: 
dividendo = divisor * cociente + resto 

'''

dividendo = int(input("Dividendo: "))
divisor = int(input("Divisor: "))
cociente = dividendo // divisor
resto = dividendo % divisor 
print(f'{dividendo} = {divisor} * {cociente} + {resto}')
