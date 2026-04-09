# Programa del trabajo 2

# Datos
nombres = ["Diego", "Juan", "Daniel", "Rolando", "Andres"]
edades = [15, 14, 15, 15, 16]
musica = ["cumbia", "Fhonk", "Pop" "Vallenato", "Rock"]

# Promedio de edad

promedio = sum(edades) / len (edades)
print('Promedio de edad:', promedio) 

# mayores de 15
mayores = [edad for edad in edades if edad > 15 ]
print("Edades mayores de 15 son: ", mayores)

# Fans del Rock
fans_rock = [gen for gen in musica if gen == "Rock"]
print("Total de chicos que le gustanel rock son: ", len(fans_rock))
