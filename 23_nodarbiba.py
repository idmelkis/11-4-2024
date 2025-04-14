# Datubāze: https://s.ayy.lv/chinook

import sqlite3
db = sqlite3.connect("C:\\Users\\idmelkis\\Downloads\\Chinook_Sqlite.sqlite")
cur = db.cursor()

# 1. Uzdevums
# Iegūt no tabulas "Employee" visus cilvēku vārdus, uzvārdus un e-pastus
#query = "SELECT FirstName, LastName, Email FROM Employee"
#cur.execute(query)
#result = cur.fetchall()
#print(result)

# 2. Uzdevums: Iegūt māksliniekus/grupas no tabulas "Artist" 
# kurām nosaukumā ir vārds "Black". Grupu nosaukumi ir kolonā "Name".
#query = "SELECT * FROM Artist WHERE \"Name\" LIKE \"%Black%\""
#cur.execute(query)
#result = cur.fetchall()
#print(result)

# 3. Uzdevums
# Iegūt pirmos 3 ierakstus no tabulas "InvoiceLine" kur InvoiceId ir 3.
#query = "SELECT * FROM InvoiceLine WHERE InvoiceId == 3 LIMIT 3"
#cur.execute(query)
#result = cur.fetchall()
#result = cur.fetchmany(3) # Alternatīva
#print(result)

# 4. Uzdevums
# Izvadat no tabulas "Customer" informāciju par to cik klienti ir atbalsta personālam ar lietotāja ievadītu identifikatoru 
# Personāla ID tiek glabāts kolonā "SupportRepId".
# ievade = int(input("Identifikators: "))
# query = "SELECT SupportRepId, COUNT(*) FROM Customer WHERE SupportRepId = ? GROUP BY SupportRepId"
# cur.execute(query, (ievade, ))
# result = cur.fetchall()
# print(result)

# 5. Uzdevums
# Izveidot datu bāzi/tabulas kas glabās informāciju par CSN pārkāpumu sodiem
# 1. Tabula - Pārkāpējs [ ID, Vecums, Vārds, Uzvārds, PersonasKods ]
# 2. Tabula - Sods [ ID, SodaPunkti, Pants, NaudasSods, ApmaksasTermiņš, MašīnasNr, Laiks, Vieta ]
# Tabulas ir saistīts (1 pārkāpējs, N sodi)

# query = 'CREATE TABLE IF NOT EXISTS "Pārkāpējs" (\
# 	"Id"	INTEGER NOT NULL UNIQUE,\
# 	"Vecums"	INTEGER,\
# 	"Vārds"	TEXT NOT NULL,\
# 	"Uzvards"	TEXT NOT NULL,\
# 	"PersonasKods"	TEXT NOT NULL,\
# 	PRIMARY KEY("Id" AUTOINCREMENT)\
# );'
# cur.execute(query)
# query = 'CREATE TABLE "" (\
# 	"Id"	INTEGER,\
# 	"SodaPunkti"	INTEGER,\
# 	"Pants"	INTEGER NOT NULL UNIQUE,\
# 	"NaudasSods"	REAL NOT NULL,\
# 	"ApmaksasTermins"	TEXT NOT NULL,\
# 	"MasinasNr"	TEXT NOT NULL,\
# 	"Laiks"	TEXT NOT NULL,\
# 	"Vieta"	TEXT NOT NULL,\
# 	"ParkapejaId"	INTEGER NOT NULL,\
# 	PRIMARY KEY("Pants" AUTOINCREMENT),\
# 	FOREIGN KEY("ParkapejaId") REFERENCES "Parkapejs"("Id")\
# );'
# cur.execute(query)

# 6. Uzdevums
# Izvadīt dziesmas nosaukumu no Tabulas "Track" un tā žanru (tabula "Genre", saistīts ar Track.GenreId).
query = 'SELECT a.name, b.name FROM Track a INNER JOIN Genre b ON a.GenreId == b.GenreId'
cur.execute(query)
result = cur.fetchall()
print(result)

cur.close()
db.commit()
db.close()