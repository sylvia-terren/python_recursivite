def factorielle(n):
    if n == 0:
        return 1
    else:
        return n * factorielle(n-1)

nombre = int(input("Entrez un nombre"))
resultat = factorielle(nombre)

print("La factorielle de ce nombres est", resultat)
