# Lasāmviela

Joinu tipi:
![Grafiks](https://miro.medium.com/v2/0*Nrjozs1i0XIiACKd.png)

* [Join sintakse](https://www.sqlite.org/syntax/join-operator.html)

# Vaicājumi

Unions -- Apvieno vairākus vaicājumus izvadot to rezultātu kopā. Abiem vaicājumiem jāatgriež vienāds kolonu skaits.

```sql
SELECT vards, alga FROM Darbinieks -- 1. Vaicājums
UNION
SELECT id, nosaukums FROM Projekts -- 2. Vaicājums
```

JOINS -- Atgriež datus no vairākām tabulām.
```sql
SELECT * FROM "Darbinieks" CROSS JOIN "Projekts"; -- CROSS JOIN - Apvieno tabulu rezultātus, katrai rindai no tabulas 1 izvadot visas rindas no tabulas 2.  
SELECT * FROM "Darbinieks" A FULL OUTER JOIN "Projekts" B ON A."id" == B."id" -- FULL OUTER JOIN - Izvada visus tabulas 1 rezultātus, un ja apvienotajā kolonā ir atbilstoša vērtība, izvada vērtības no tabulas 2. Ja nav - izvada NULL šajos tabulas 2 laukos. Apvienots RIGHT un LEFT joins.
SELECT * FROM "Darbinieks" A RIGHT JOIN "Projekts" B ON A."id" == B."id"; -- RIGHT (OUTER) JOIN - Izvada visus tabulas 2 rezultātus, kuriem ir atbilstoša vērtība norādītajā tabulas 1 kolonā. Ja nav - izvada NULL tabulas 1. laukos.
SELECT * FROM "Darbinieks" A LEFT JOIN "Projekts" B ON A."id" == B."id"; -- LEFT (OUTER) JOIN - Izvada visus tabulas 1 rezultātus, kuriem ir atbilstoša vērtība norādītajā tabulas 2 kolonā. Ja nav - izvada NULL tabulas 2. laukos.
SELECT * FROM "Darbinieks" A INNER JOIN "Projekts" B ON A."id" == B."id"; -- INNER JOIN - Izvada TIKAI tos tabulu rezultātus kuriem tabulā 1 ir atbilstoša vērtība tabulā 2.
```

# Uzdevumi

* Piemēra datu bāze "Chinook": https://s.ayy.lv/chinook

1. Uzdevums - Uzrakstīt vaicājumu, kas izvada albumus ar to mākslinieku nosaukiem (tabula Album + Tabula Artist).

```sql
SELECT A.Title, B.Name
FROM Album A 
INNER JOIN Artist B -- Strādās arī vienkārši "JOIN Artist B", INNER JOIN ir standarta joins.
ON A.ArtistId == B.ArtistId;
```

2. Uzdevums - Izveidot kopiju tabulai `Genre`, un pārkopēt visus datus no Tabulas `Genre` iekš izveidotās kopijas. (šī ir darbība, kas var būt noderīga gadījumā, ja jums ir [jāmaina tabulas definīcija](https://www.sqlite.org/lang_altertable.html)).

```sql
CREATE TABLE IF NOT EXISTS "Genre_2" (
	"GenreId"	INTEGER NOT NULL,
	"Name"	NVARCHAR(120),
	CONSTRAINT "PK_Genre" PRIMARY KEY("GenreId")
);

INSERT INTO "Genre_2" SELECT GenreId, Name FROM "Genre";
```

3. Uzdevums - Izvadīt visus rēķinus (tabula `Invoice`) klientiem (tabula `Customer`) no Brazīlijas (kolona `Country` tabulā `Customer`).

```sql
SELECT b.FirstName, b.LastName, b.Address, a.InvoiceId FROM "Customer" b
INNER JOIN "Invoice" a
ON a.CustomerId == b.CustomerId
WHERE b.Country == "Brazil";
```