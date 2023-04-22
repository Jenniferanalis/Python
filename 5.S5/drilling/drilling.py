#declarar variable que almacena la palabra "paralelepípedo"

palabra ="paralelepípedo"

consonantes = ""

for i in range(len(palabra)):
    if palabra[i] not in "aeiíouAEIOU":
        consonantes += palabra[i]
        print(f"La letra {palabra[i]} se encuentra en la posición {i}")

print(consonantes)