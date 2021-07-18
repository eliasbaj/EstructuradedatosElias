"""Uso de while infinito"""
C= "1"
while True:
    print(C)
    break
#While validation
Vocal = input("Ingrese vocal:")
while Vocal not in("a","e","i","o","u"):
    if Vocal == ".":
        break
    Vocal = input("Vocal:")
print("Su vocal o punto es:{}".format(Vocal))