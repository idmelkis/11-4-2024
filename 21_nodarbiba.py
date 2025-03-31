# Dokumentācija: https://docs.python.org/3/library/sqlite3.html
# SQL Injekcijas: https://github.com/swisskyrepo/PayloadsAllTheThings/blob/master/SQL%20Injection/SQLite%20Injection.md
import sqlite3

############## SQLITE 3 Bibliotēka
# # .find("sad") = # SELECT * FROM Table WHERE Name = "Sad"

# SQLite3 operatīvajā atmiņā
#db = sqlite3.connect(":memory:")

db = sqlite3.connect("21_nodarbiba.db")

cur = db.cursor()

# Izvēlamies datus ar parametriem
# 1. Metode - Parametri ir vārdnīcā, un tiem ir nosaukums
data = (
    { "id": 3 }
)
select_query = f"SELECT * FROM Tabula WHERE ID = :id;"
cur.execute(select_query, data)

# 2. Metode - Parametri ir sarakstā
# parametri = (2,)
# select_query = f"SELECT * FROM Tabula WHERE ID = ?;"
# cur.execute(select_query, parametri)

# Atgrieztie rezultāti ir Tuple datu tipā
rows = cur.fetchall() # Atgriež visus rezultātus
# cur.fetchmany(size=3) # Atgriež noteiktu skaitu rezultātu, līdzīgs LIMIT
# cur.fetchone() # Atgriež VIENU rezultātu

for row in rows:
    print(row)

# Saglabā visus datus failā - neaizmirst!
cur.close()
db.commit()
db.close()

############## Lietotājs tabula
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

lietotajs = Lietotajs(0, "lietotajs", "******", "pasts@pasts.lv")
# print(lietotajs)

import sqlite3
db = sqlite3.connect("21_nodarbiba.db")
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

# Ievietojam datus
#query = f"INSERT INTO Lietotajs (lietotajvards, parole, epasts) VALUES (?,?,?);"
#cur.execute(query, lietotajs.uz_vaicajumu())

# Iegūstam datus
# query = "SELECT * FROM Lietotajs"
# cur.execute(query)
# rows = cur.fetchall()
# for row in rows:
#     print(Lietotajs.no_rezultata(row))

# Datu dzēšana
# query = "DELETE FROM Lietotajs WHERE id = 1"
# cur.execute(query)

# Tabulu dzēšana 
query = "DROP TABLE Lietotajs"
cur.execute(query)

cur.close()
db.commit()
db.close()