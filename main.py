a = float(input("Dime un numero real: "))

unidades = a % 10 
decenas = (a // 10) % 10
centenas = (a // 100) % 10

print("| Unidades | Decenas | Centenas |")
print(f"|{unidades:10}| {decenas:9} | {centenas:10} |")

decimal1 = int((a * 10) % 10)
decimal2 = int((a * 100) % 10)
decimal3 = int((a * 1000) % 10)

print("| 1er decimal | 2º decimal | 3er decimal |")
print("| {decimal1:13} | {decimal2:12} | {decimal3:13} |")



