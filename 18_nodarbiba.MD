# SQL Vaicājumi

* '*' = wildcard character - izvēlas visu

LIMIT

```sql
SELECT * FROM T1 WHERE T1_ID > 4 LIMIT 2;
```

GROUP BY

```sql
-- GROUP BY apvieno vienādās vērtības
-- Agregātfunkcijas ļauj strādāt ar apvienotajiem laukiem/kolonām.
-- Visas agregātfunkcijas: https://www.sqlite.org/lang_aggfunc.html#sumunc
SELECT "Lauks", count("Lauks") FROM T1 GROUP BY "Lauks";
```

DELETE

```sql
DELETE FROM "T1" WHERE "T1_ID" == 6;
```

DROP TABLE - dzēst tabulu
```sql
DROP TABLE IF EXISTS "Darbinieks"
```

# Uzdevumi

Uzdevums: uzrakstīt SQL vaicājumus, lai
* izveidotu sekojošo klasi kā tabulu, 
* un uzrakstīt vaicājumus lai ievietotu tabulā apakšā esošos datus.

```py
class Darbinieks:
    id :int
    vards :str
    alga :float
    amats :str
    nostradats :int

janis = Darbinieks(1, "Jānis", 1000, "Slotas operators", 24)
eriks = Darbinieks(2, "Ēriks", 2000, "Tirgotājs",	30)
anna = Darbinieks(3, "Anna",  500,  "Laborante",	2)
karlis = Darbinieks(4, "Kārlis", 9001, "Direktors", 36)
```

Risinājums:
```sql
CREATE TABLE IF NOT EXISTS "Darbinieks" (
	"id" INTEGER UNIQUE,
	"vards" TEXT,
	"alga" REAL,
	"amats" TEXT,
	"nostradats" INTEGER,
	PRIMARY KEY ("id" AUTOINCREMENT)
);
INSERT INTO "Darbinieks" ("vards", "alga", "amats", "nostradats") VALUES
("Jānis", 1000, "Slotas operators", 24), ("Ēriks", 2000, "Tirgotājs", 30),
("Anna",  500,  "Laborante", 2), ("Kārlis", 9001, "Direktors", 36);
```

Uzdevums (turpinājums): 
* Izveidot tabulu projekts, kurš satur informāciju par projekta nosaukumu un identifikatoru.
* Realizēt darbinieku saistību ar vairākiem projektiem.

Risinājums:

```sql
CREATE TABLE IF NOT EXISTS "Projekts" (
	"id" INTEGER UNIQUE,
	"nosaukums" TEXT,
	PRIMARY KEY ("id" AUTOINCREMENT)
);

CREATE TABLE IF NOT EXISTS "DarbiniekuProjekti" (
	"id_darbinieks" INTEGER,
	"id_projekts" INTEGER,
    CONSTRAINT "Darbinieks" FOREIGN KEY("id_darbinieks") REFERENCES "Darbinieks"("id") ON DELETE CASCADE,
    CONSTRAINT "Projekts" FOREIGN KEY("id_projekts") REFERENCES "Projekts"("id") ON DELETE CASCADE
);

-- Paātrinātu pieeju datiem "DarbiniekuProjekti" tabulā, ja mēs mēģinātu iegūt tos ar SELECT
CREATE INDEX "idxProj" ON "DarbiniekuProjekti" (
	"id_darbinieks"	ASC,
	"id_projekts"	ASC
);
```

Nākošajā stundā -- Joins, Unions