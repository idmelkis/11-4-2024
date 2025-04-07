# Praktiski - Lietotājs tabula - izveide, datu ievade, izvade
class Lietotajs:
    def __init__(self, id, lietotajvards, parole, epasts):
        self.id = id
        self.lietotajvards = lietotajvards
        self.parole = parole
        self.epasts = epasts
    
    def uz_vaicajumu(self):
        return (self.lietotajvards, self.parole, self.epasts)

    def __str__(self):
        return f"[{self.id}] <{self.lietotajvards}>:<{self.parole}> -- {self.epasts}"
    
    @classmethod
    def no_rezultata(cls, *args):
        args = args[0]
        return cls(args[0], args[1], args[2], args[3])

    
import sqlite3
db = sqlite3.connect("22_nodarbiba.db")
cur = db.cursor()

# Izveidojam tabulu
query = "CREATE TABLE IF NOT EXISTS Lietotajs (" \
"Id INTEGER UNIQUE NOT NULL," \
"Lietotajvards TEXT NOT NULL," \
"Parole TEXT NOT NULL," \
"Epasts TEXT," \
"PRIMARY KEY (Id AUTOINCREMENT)" \
")"
cur.execute(query)

def izveidot_lietotaju(cursor :sqlite3.Cursor) -> Lietotajs:
    lietotajvards = input("Lietotajvards: ")
    parole = input("Parole: ")
    epasts = input("E-pasts: ")
    query = f"INSERT INTO Lietotajs (lietotajvards, parole, epasts) VALUES (?,?,?);"
    # Piezīme: paroli vajadzētu šifrēt, piem. ar SHA256 funkciju
    cursor.execute(query, (lietotajvards, parole, epasts))
    # Piezīme: Šeit vajadzētu arī tikt galā ar kļūdām (piem. lietotājs eksistē)

    query = 'SELECT * FROM Lietotajs ORDER BY "Id" DESC LIMIT 1'
    cursor.execute(query)
    rows = cur.fetchall()
    return Lietotajs.no_rezultata(rows[0])

def autentificet_lietotaju(cursor :sqlite3.Cursor) -> Lietotajs:
    # Uzdevums: Uzrakstat vaicājumus un python kodu, kas
    # Pieņem lietotājvārdu un paroli kā ievadi
    lietotajvards = input("Lietotajvards: ")
    parole = input("Parole: ")
    # Meklē šo lietotājvārdu un paroli datu bāzē
    query = 'SELECT * FROM Lietotajs WHERE Lietotajvards == ? AND Parole == ? ORDER BY "Id" DESC LIMIT 1'
    cursor.execute(query, (lietotajvards, parole))

    # Izvada lietotāja detaļas ja lietotājvārds un parole atbilst
    rows = cursor.fetchall()
    if len(rows) > 0:
        return Lietotajs.no_rezultata(rows[0])
    else:
    # Izvada kļūdu, ja neatbilst
        print("Lietotājs neeksistē!")
        return None
    
# Uzdevums (i/ni):
# Pievienot profila funkcionalitāti.
# 1. Izveidot jaunu tabulu (Profils) - 
# Lauki - Id, LietotajaId, Vards, Uzvards, ParMani
# LietotajaId vajadzētu būt saistīts ar Lietotajs.Id (ON DELETE CASCADE)

# Ja lietotājs programmā ir autentificējies, tad
# Lietotājam vajadzētu varēt izvadīt savu profilu (ja tāds ir).
# Lietotājam vajadzētu varēt izveidot vai izmainīt (ja tāds ir) savu profilu.

lietotajs = None
while True:
    if lietotajs is not None:
        print(f"Aktīvais lietotājs: {lietotajs}")
    print("Izvēlne")
    print(" -- 1. Lietotāja izveide ")
    print(" -- 2. Autorizācija ")
    print(" -- 0. Iziet ")

    ievade = int(input("Ievade: "))
    if ievade == 0:
        break
    elif ievade == 1:
        lietotajs = izveidot_lietotaju(cur)
    elif ievade == 2:
        lietotajs = autentificet_lietotaju(cur)


cur.close()
db.commit()
db.close()