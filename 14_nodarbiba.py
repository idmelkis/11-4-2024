# Uzdevums (i/ni) no iepriekšējās nodarbības.
class BankasKonts:
    atlikums :float = 0.0
    def __init__(self):
        self.atlikums = 0.0
    def ieskaitit(self, summa):
        self.atlikums += summa
    def iznemt(self, summa):
        if self.atlikums > 50 or self.atlikums-summa > 30:
            self.atlikums -= summa
        else:
            print("Nepietiek līdzekļi")
class Krajkonts(BankasKonts):
    def iznemt(self, summa):
        summa *= 1.10
        return super().iznemt(summa)

pirmais_konts = BankasKonts()
pirmais_konts.ieskaitit(100)
pirmais_konts.iznemt(60)
pirmais_konts.iznemt(80)
otrais_konts = Krajkonts()
otrais_konts.ieskaitit(100)
otrais_konts.iznemt(30)

# 1. Uzdevums
class Prece:
    nosaukums: str
    cena: float
    def __init__(self, nos, cena):
        self.nosaukums = nos
        self.cena = cena
class Grozs:
    preces: 'list[Prece]'
    def __init__(self):
        self.preces = []
    def pievienotPreci(self, prece :Prece):
        self.preces.append(prece)
    def iznemtPreci(self, precesNos):
        for iii in range(0, self.preces):
            if self.preces[iii].nosaukums == precesNos:
                self.preces.pop(iii)
                break
    def aprekinatVertibu(self):
        vertiba = 0.0
        for iii in range(0, self.preces):
            vertiba += self.preces[iii].cena
        return vertiba
    
# piem.
piens = Prece("piens", 1.0)
grozs = Grozs()
grozs.pievienotPreci(piens)
grozs.iznemtPreci("piens")
print(grozs.aprekinatVertibu)

# 2. Uzdevums
class Darbinieks:
    id :str
    vards :str
    alga :float
    amats :str
    nostradats :int
    def __init__(self, id, vards, alga, amats, nostradats):
        self.id = id
        self.vards = vards
        self.alga = alga
        self.amats = amats
        self.nostradats = nostradats
    def __str__(self):
        return f"{self.vards} - {self.amats} ({self.alga} EUR/Mēn)"
    def aprekinatAlgu(self):
        return self.alga * self.nostradats

janis = Darbinieks("01", "Jānis", 1000, "Slotas operators", 24)
eriks = Darbinieks("02", "Ēriks", 2000, "Tirgotājs",	30)
anna = Darbinieks("03", "Anna",  500,  "Laborante",	2)
karlis = Darbinieks("04", "Kārlis", 9001, "Direktors", 36)
print(janis)
print(eriks)
print(anna)
print(karlis)
print(karlis.izmaksataAlga())

# 3. Uzdevums
class Darbinieks:
    vards :str
    uzvards :str
    stazs :int
    alga :float
    amats :str
    def __init__(self, vards, uzvards, stazs, alga, amats):
        self.vards = vards
        self.uzvards = uzvards
        self.stazs = stazs
        self.alga = alga
        self.amats = amats
    def aprekiniBonusu(self):
        return 0
    def aprekiniKopalgu(self):
        return self.alga * self.stazs + self.aprekiniBonusu()
    def __str__(self):
        return f"{self.vards} {self.uzvards} nopelna {self.aprekiniKopalgu()}"
class Menedzeris(Darbinieks):
    darbinieki :int
    def __init__(self, vards, uzvards, stazs, alga, amats, darbinieki):
        self.darbinieki = darbinieki
        super().__init__(vards, uzvards, stazs, alga, amats)
    def aprekiniBonusu(self):
        return self.darbinieki * 100
class Programmetajs(Darbinieks):
    projekts :str
    def __init__(self, vards, uzvards, stazs, alga, amats, projekts):
        self.projekts = projekts
        super().__init__(vards, uzvards, stazs, alga, amats)
    def aprekiniBonusu(self):
        return self.alga * 0.10
class Testetajs(Darbinieks):
    projekts :str
    stunduSkaits :float
    def __init__(self, vards, uzvards, stazs, alga, amats, projekts, stunduSkaits):
        self.projekts = projekts
        self.stunduSkaits = stunduSkaits
        super().__init__(vards, uzvards, stazs, alga, amats)
    def aprekiniBonusu(self):
        return self.alga * 0.5
    def aprekiniKopalgu(self):
        return self.stunduSkaits * 7 + self.aprekiniBonusu()
janis = Menedzeris("Jānis", "Uzvārds", 10, 10, "Menedžeris", 10)
pēteris = Programmetajs("Pēteris", "Uzvārds", 10, 10, "Menedžeris", "Proj1")
gunita = Testetajs("Gunita", "Uzvārds", 1, 0, "Testētājs", "Proj1", 10)
print(janis)
print(pēteris)
print(gunita)