import math
#Winkel_Grad = 0

#while Winkel_Grad <= 180:
#    Winkel_rad = Winkel_Grad * math.pi / 180
#    cosinus = math.cos(Winkel_rad)

 #   print("Winkel : ", Winkel_Grad, "-> cosinus: ", cosinus)
#    Winkel_Grad += 10
    

i = 0

while i <= 180:
    b = i * math.pi / 180
    a = math.cos(b)
    print("Winkel: ", i, "->cosinus: ", a)
    i += 10