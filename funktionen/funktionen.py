###########################################################
# Kopfkommentar
# U. Böhmer
# 03.03.2025
# Dateiname: funktionen.py
# Kommentar: Funktionen zur Berechnung Elektrotechnischer Größen
##########################################################

# Funktionen
def spannung_aus_IR(strom, wider):
    U = strom * wider
    return U

def leistung(spannung, strom):
    P = spannung *strom
    return P

def kapazitaet(ladung , spannung):
    K = ladung / spannung
    return K

