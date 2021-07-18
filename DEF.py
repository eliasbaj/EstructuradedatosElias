"""Funciones de retorno"""
def vocales(frase):
    for car in frase:
        if car in ('a', 'e', 'i', 'o', 'u'):
            print(car)
"""Llamada a función"""
oracion = input('Ingrese una oracion: ')
vocales(oracion.lower())

"""Funcion con retorno de valor"""
def promedio(notas):
    summ = 0
    for n in notas:
        summ += n
    return summ / len(notas)

"""llamada a funcion"""
Sumadenotas = [15, 14, 12, 12, 10]
prom = promedio(Sumadenotas)
print('Promedio: {} = {}'.format(Sumadenotas, prom))