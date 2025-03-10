###########################################################
# Kopfkommentar
# U. Böhmer
# 03.03.2025
# Dateiname: kontrollstrukturen.py
# Kommentar: Kontrollstr. in P.
##########################################################

#Anweisunfungsfolge (Sequenz)
x = 10
y = 0
z = -10

#Verzweigung (Alternative)
#einseitige Verzweigung
if x > 0:
    print(x,"ist größer als 0");

#zweiseitig
if z<0:
    print(z,"ist negativ")
else:
    print("nicht negativ!")

#mehrseitig
if x<0:
    print(z,"ist negativ")
else:
    if x==0:
        print(x,"ist Null")
    else:
        print(x ,"ist echt größer als Null")

if x<0:
    print(z,"ist negativ")
elif x==0:
        print(x,"ist Null")
else:
    print(x ,"ist echt größer als Null")

#Schleife (Iteration)
#kopfgesteuert

while y<=10:
    print(y)
    y=y+1

#mehr Schleifentype gibt es (erstmal) nicht in Phython



#fußgesteuert