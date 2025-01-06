#class Nosaukums:
#    pass

# Klase - abstrakcija datiem
class Automašīna:
    krāsa :str = ""
    marka :str = ""

    ātrums :float = 0.0
    virziens_x :float = 0.0
    virziens_y :float = 0.0

    def __init__(self, krāsa, marka):
        self.krāsa = krāsa
        self.marka = marka
        print(f"Izveidota klase {krāsa} {marka}!")
    def __str__(self) -> str:
        return f"Informācija par auto: {self.krāsa} {self.marka}"
           
    # Vienkārša funkcija
    def nosaukums(self):
        print("Izsaukta funkcija")
    
    def paatrinat(self, paatrinajums) -> None:
        self.ātrums += paatrinajums
    def bremzet(self, bremz_straujums) -> None:
        self.ātrums -= bremz_straujums

    # Getter & setter funkcijas
    # encapsulation - slēpjam implementāciju no pārējā koda
    def getAtrums(self):
        return self.ātrums
    def setAtrums(self, ātrums):
        self.ātrums = ātrums

    # Statiska funkcija
    @classmethod
    def no_kautka(cls):
        # Atgriež jaunu klases instanci (objektu)
        return cls("", "")

# Objekts ir mainīgais, kurā dati ir klases formātā
objekts = Automašīna("Sarkans", "BMW")
print(objekts)
print(objekts.__dict__) # Izvada visus objekta mainīgos kā vārdnīcu
# Ar vienu klasi var izveidot vairākus objektus - tie nav saistīti
objekts2 = Automašīna("Pelēks", "Audi")

# objekts.paatrinat(0.5)
# objekts.bremzet(0.5)
# print(objekts.ātrums)

# Piemērs
# import time
# nobraukts = 0.0
# while True:
#     time.sleep(1)
#     # Ievade -- vajadzētu nebloķēt
#     i = input()
#     if i == "w":
#         objekts.paatrinat(0.5)
#     elif i == "s":
#         objekts.bremzet(0.5)
#     nobraukts += objekts.getAtrums()
#     print(f"Ātrums: {objekts.getAtrums()}, kopā nobraukts: {nobraukts}")

# Statiskas funkcijas - nevajag izveidot objektu lai izmantotu
#Automašīna.no_kautka()

# Uzdevums:
# Izveidot klasi, kas aprakstītu priekšmetu e-klasē
# Vismaz 5 mainīgie, un 2 funkcijas kas strādā ar šiem datiem.
# Izveidojat objektu, un uzrakstat kodu, kas pielieto šīs funkcijas.
class Skolens:
    vards = ""
    def __init__(self, vards, uzvards):
        self.vards = vards + " " + uzvards
class Nodarbiba:
    datums = ""
    tema = ""
    def __init__(self, datums, tema):
        self.datums = datums
        self.tema = tema
class Prieksmets:
    nosaukums: str = ""
    skolotajs: str = ""
    skolenu_skaits: int = 0
    skoleni: 'list[Skolens]' = []
    nodarbibas: 'list[Nodarbiba]' = []

    def __init__(self, nosaukums, skolotajs):
        self.nosaukums = nosaukums
        self.skolotajs = skolotajs
    def izveidotNodarbibu(self, nosaukums, tema):
        self.nodarbibas.append(Nodarbiba(nosaukums, tema))
    def pievienotSkolenu(self, skolens :Skolens):
        self.skoleni.append(skolens)
        self.skolenu_skaits = len(self.skoleni)
    def __str__(self):
        return f"Priekšmets {self.nosaukums} ar {self.skolenu_skaits} skolēniem..."

programmesana = Prieksmets("Programmēšana I", "Ingmārs")
programmesana.pievienotSkolenu(Skolens("Jānis", "Bērziņš"))
print(programmesana)

# Uzdevums 2: 
# Uzrakstīt klasi "Lampa", kas apraksta lampu, un spuldzi tajā.
# Lampas objektam vajadzētu uzglabāt informāciju par lampas stāvokli, un spuldzi tajā.