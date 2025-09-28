ciudad = "Valencia"
año = 2024
lluvia = 150.2598
print("En", ciudad, "en el año", año, ", llovió", lluvia, "Litros")
#En Valencia en el 2024 , llovió 150.2598 Litros

print("En", ciudad, "en el año", año, ", llovió", lluvia, "Litros", sep='')
#EnValenciaen el año2024, llovió150.2598Litros
#sep = _ para cambiar los espacios que quiero que haya entre cada palabra.

print("En", ciudad, "en el año", año, ", llovió", lluvia, "Litros", sep=' ', end=", ")
print("más o menos")
#poner el end hará que el sigueinte print salga al lado del anterior con el separador que yo indique.
#En Valencia en el año 2024 , llovió 150.2598 Litros, más o menos

#otros comandos
#\n > salto de linea
#\t > tabulación 
#\' > para poner comillas sin que la maquinita se confunda 
#\\ > contrabarra

print("En " +ciudad+ " en el año "+ str(año)+" llovió "+str(round(lluvia, 2))+" litros")
#En Valencia en el año 2024 llovió 150.26 Litros

print(f'En {ciudad}, en {año}, llovió, {lluvia} litros')
#En Valencia en el año 2024 llovió 150.26 litros

agente = 7
print(f"soy el agente {agente}")
#soy el agente 7

print(f"soy el agente {agente:3}")
#soy el agente   7

print(f"soy el agente {agente:03}")
#soy el agente 007

print(f"soy el agente {agente:<03}")
#soy el agente 700

print(f"soy el agente {agente:^03}")
#soy el agente 070
