"""
Le pedimos al usuario un codigo de pais y un numero de telefono y lo mostramos con el formato +(pais) XXX XX XX XXX
"""

pais = int(input("Codigo del pais: "))
tel = int(input("nº de tlf: "))

p1 = tel // 1000000 
p2 = (tel // 10000) % 100
p3 = (tel // 100) % 100
p4 = tel % 100
print(f"+({pais}) {p1} {p2} {p3} {p4}")

