# Tuplas – Listas - Diccionarios
usuario = ('Jeymi','2001',"jmejiag2@unemi.edu.ec")
materias = ["Python","PHP","POO","Sistemas Operativos"]
Estudiante = {"nombre":"Jimmy Daniel","edad":19,"facultad": "faci"}
print(usuario[0],materias[1],Estudiante['nombre'])
print(usuario[0:2],Estudiante.keys(),Estudiante.values())
materias.append("Estructura de datos")
Estudiante["sexo"], Estudiante["edad"]="Masculino", 19
print(materias,Estudiante)
#tupla,lista,diccionario=(),[],{}
# Recorridos tuplas y listas con in
for valor in usuario: print(valor)
# Recorridos listas con enumerate
for i, c in enumerate(materias): print(i,':',c)
# Recorridos diccionario con items
for c, v in Estudiante.items(): print(c,':',v)