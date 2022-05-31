Eingabe1 = float(input("Bitte Zahl1 eingeben: "))
Eingabe2 = float(input("Bitte Zahl2 eingeben: "))

def summe(Eingabe1, Eingabe2):          # Funktion -> def Funktionsnamen(Parameter1, Parameter2,...)
    zwischensumme = Eingabe1 + Eingabe2
    return(zwischensumme)

def differenz(Eingabe1, Eingabe2):          
    differenz = Eingabe1 - Eingabe2
    return(differenz)

def produkt(Eingabe1, Eingabe2):
    produkt = Eingabe1 * Eingabe2
    return(produkt)

def quotient(Eingabe1, Eingabe2):
    if Eingabe2 == 0:
        print("Quotient nicht lösbar!")
        return
    quotient = Eingabe1 / Eingabe2
    return(quotient)

output1 = summe(Eingabe1, Eingabe2)
output2 = differenz(Eingabe1, Eingabe2)
output3 = produkt(Eingabe1, Eingabe2)
output4 = quotient(Eingabe1, Eingabe2)

print("Summe: ",output1)
print("Differenz: ",output2)
print("Produkt: ",output3)
print("Quotient: ",output4)

