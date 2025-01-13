# Uzdevums 2: 
# Uzrakstīt klasi "Lampa", kas apraksta lampu, un spuldzi tajā.
# Lampas objektam vajadzētu uzglabāt informāciju par lampas stāvokli, un spuldzi tajā.
class Spuldze:
    energijas_paterins :float = 0.0
    krasa :str = 0.0
    ieslegts :bool = True
class Lampa:
    spuldze :Spuldze = Spuldze()
    ieslegts :bool = True

# ===
class Transportlīdzeklis:
    krāsa :str = ""
    marka :str = ""
    ātrums :float = 0.0
    def __init__(self):
        print("Izveidots transportlīdzeklis")
    def funkcija(self):
        print("!!!")

    def paatrinat(self) -> None:
        self.ātrums += 0
    def bremzet(self) -> None:
        self.ātrums -= 0

class Automašīna(Transportlīdzeklis):
    riteņu_skaits :int = 0
    def __init__(self):
        super().__init__()
    def funkcija(self):
        print("???")

    def paatrinat(self) -> None:
        self.ātrums += 1
    def bremzet(self) -> None:
        self.ātrums -= 1

class Lidmašīna(Transportlīdzeklis):
    spārnu_skaits = 2;

    def paatrinat(self) -> None:
        self.ātrums += 4
    def bremzet(self) -> None:
        self.ātrums -= 4


masina = Automašīna()
masina.paatrinat()
masina.paatrinat()
print(masina.ātrums)

lidmasina = Lidmašīna()
lidmasina.paatrinat()
lidmasina.paatrinat()
print(lidmasina.ātrums)

from enum import Enum
class Krāsa(Enum):
    Sarkana = 1,
    Zaļa = 2,
    Zila = 3

lidmasina.krāsa = Krāsa.Sarkana
if lidmasina.krāsa == Krāsa.Zaļa:
    print("Jā!")

# Uzdevums: 1 Bāzes un vismaz 2 apakšklases. Par brīvu tēmu.
# Bāzes klasei vajag būt 2-3 mainīgie un vismaz viena funkcija
# Apakšklasēm jāizmanto polimorfisms lai pārrakstītu bāzes klases funkciju
# Tā, lai tā dara kaut ko citu (pietiek ar primitīvu print() funkc.)
# Pamēģinat izveidot objektus no šīm klasēm un izsaukt funkcijas/mainīgos.

# Uzdevums i/ni: Izveidot programmu
# Jāizveido klase "Banka Konts". 
# * Šai klasei jāglabā informācija par lietotājam pieejamajiem naudas līdzekļiem.
# * Izveidojat funkcijas, kas ļauj ieskaitīt vai izņemt naudu no konta
# * Neļaut lietotājam izņemt naudu, 
#   ja kontā ir zem €50,
#   vai, ja izņemot paliktu zem €30 (piem. ja ir €100, un izņem €71, izņemt neļauj)
# Izveidojat apakšklasi "Krājkonts".
# * Izmantot polimorfismu lai pārrakstītu izņemšanas funkciju, 
#   lai tā kopā ar izņemto naudu izņem vēl 10%
#   (t.i. izņemot €100, izņems €110)
# * Neļaut lietotājam izņemt naudu, 
#   ja kontā ir zem €50,
#   vai, ja izņemot paliktu zem €30 (piem. ja ir €100, un izņem €71, izņemt neļauj)

# Izveidojat objektus no šīm klasēm (viena - vienkāršs bankas konts, otra - krājkonts).
# Pirmajā kontā ieskaitat €100, tad izņemat €60 un €80
# Otrajā kontā ieskaitat €100, tad izņemat €30
# Izmantojat izveidotās izņemšanas un ieskaitīšanas funkcijas!