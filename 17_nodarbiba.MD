# Lasāmviela:

* Foreign keys: https://www.sqlite.org/foreignkeys.html
* Transactions: https://www.sqlite.org/lang_transaction.html
* Indeksi: https://www.sqlitetutorial.net/sqlite-index/

# SQL Vaicājumi

Lai atrastu doc. - Google vai citā dzinī - vaicājuma tips + sqlite, piem INSERT Sqlite

* Tabulas izveide [ CREATE TABLE ]
* Datu ievietošana [ INSERT ]

Komentāri:
```SQL
-- Vienas rindas komentārs
/*
Vairāku rindu
komentārs
*/
```

Tabulas izveide:
```SQL
CREATE TABLE "T1" (
	"T1_ID"	INTEGER NOT NULL UNIQUE,
	"Lauks"	TEXT,
	PRIMARY KEY("T1_ID" AUTOINCREMENT)
);
```

Tabulas izveide ar foreign key:
```SQL
CREATE TABLE "T2" (
	"T2_ID"	INTEGER NOT NULL UNIQUE,
	"Lauks"	TEXT DEFAULT 'Standarta_vērt',
	"T1_ID"	INTEGER,
	PRIMARY KEY("T2_ID" AUTOINCREMENT),
	CONSTRAINT "T1_Saistība" FOREIGN KEY("T1_ID") REFERENCES "T1"("T1_ID") ON DELETE CASCADE
);
```

Insert:
```SQL
INSERT INTO "T1" ( "Lauks" ) VALUES ( "Kautkada_vert2" ), ( "Kautkada_vert3" )
```

Update:
```SQL
UPDATE "T1" SET "Lauks" = "Jauna vērtība" WHERE "T1_ID" == 6
```

Select:
```SQL
-- WHERE darbības: > < <= >= != == LIKE
SELECT * FROM "T1"; -- Izvēlamies visu
SELECT DISTINCT "Lauks" FROM "T1" WHERE "T1_ID" > 3; -- Unikālas kolonas "Lauks" vērtības, ar T1_ID > 3
SELECT "Lauks" FROM "T1" WHERE "T1_ID" < 5; -- Visas kolonas "Lauks" vērtības, kurām T1_ID < 5
SELECT * FROM "T1" WHERE LAUKS LIKE "%_vert"; -- Teksta pārbaude - pārbaudam vērtības "Lauks", kur teksts beidzas ar "_vert"
```

ORDER BY
```SQL
SELECT * FROM "T3" ORDER BY "Lauks2" ASC, "Lauks" ASC; -- Vairāki lauki
SELECT * FROM "T1" ORDER BY "Lauks" DESC; -- Dilstošā secībā
```

Nākošajā stundā -- LIMIT, GROUP BY, Joins, Unions