nota1 = float(input("Ingresa la primera nota: "))
nota2 = float(input("Ingresa la segunda nota: "))
promedio = (nota1 + nota2) / 2
nombre = input("Ingresa el nombre del alumno: ")
print(f"El promedio de {nombre} es {promedio}")
notas_aprobadas = [6.0, 6.5, 7.0, 7.5, 8.0, 8.5, 9.0, 9.5, 10.0]
aprobo = promedio in notas_aprobadas
print(f"¿{nombre} aprobó la materia? {aprobo}")

nombre = "erick"