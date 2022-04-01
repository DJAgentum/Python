intVariable = 0
foatPi = 0
summe = 0

strTerme = input("Bitte Anzahl der Terme eingeben: ")
intTerme = int(strTerme)

while intVariable <= intTerme:
    
    floatPi = (((-1)**intVariable) / (2*intVariable +1))
    summe += floatPi
    intVariable += 1

print("Annäherung von Pi ", summe*4)