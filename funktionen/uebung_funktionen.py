##########################################
# U. Böhmer                              #
# Datum: 27.01.2025                      #
# Datei: uebung_funktionen.py            #
# Kommentar: Funktionen erstellen        #
##########################################
#import funktionen       #alle Funktionen importieren
#import funktionen as fun                   # einen Alias vergeben
from funktionen import spannung_aus_IR

#H A U P T P R O G R A M M


# Ohmsches Gesetz U = R * I
stromstaerke  = float(input("Stromstärke (A): "))
widerstand = float(input("Wiederstand(\u2126): "))

spannung = spannung_aus_IR(stromstaerke, widerstand)




print("Spannung:",spannung, "V")
print(spannung_aus_IR(10, 5000))


if spannung_aus_IR(7,56) > 500:
    print("Hohe Spannung")


# Elektrische Leistung p = U * I
spannung  = float(input("Spannung(V): "))
stromstaerke  = float(input("Stromstärke(A): "))
print("Leistung:",leistung(spannung,stromstaerke),"W")

# Kapazität: C = Q / U
ladung  = float(input("Ladung(Coulomb): "))
spannung  = float(input("Spannung(V): "))
print("Kapazität:",kapazitaet(ladung,spannung),"Farad")
