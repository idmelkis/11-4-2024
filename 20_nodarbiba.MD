# Lasāmviela

* Datumi - https://www.sqlite.org/lang_datefunc.html

# Uzdevumi

* Uzrakstat vaicājumu, kas izvada rēķinus (`Invoice`), kuru id ir 400 vai lielāki, un kopsumma (`Total`) ir virs 5.00.

```sql
SELECT * FROM "Invoice" WHERE InvoiceId >= 400 AND total > 5.00;
```

* Uzrakstat vaicājumu, kas izvada visus rēķinus (`Invoice`) no 2009. gada līdz 2011. gadam.

```sql
-- Vērtību diapazona salīdzinājums (piem. ar Total kolonu)
-- ... WHERE Total BETWEEN 5.00 AND 10.00
-- ... WHERE total >= 5.00 AND Total <= 10.00
-- Pārbaude ar datumiem
-- ... WHERE datetime(kolonas_nosaukums)...
SELECT * FROM "Invoice"
WHERE InvoiceDate BETWEEN datetime('2009-01-01 00:00:00') AND datetime('2011-01-01 00:00:00');
```

* Izmainat iepriekšējo vaicājumu, lai izvadītu šajā laika posmā izrakstīto rēķinu skaitu

```sql
SELECT count(*)
FROM "Invoice"
WHERE InvoiceDate BETWEEN datetime('2009-01-01 00:00:00') 
AND datetime('2011-01-01 00:00:00');
```

* Uzrakstat vaicājumu, kas izvada cik katrā atskaņošanas sarakstā ir dziesmas (tabula  `PlaylistTrack`). Pietiek, ka parāda playlistId - skaits. Hint - grupēt.

```sql
SELECT PlaylistId, count(TrackId) FROM PlaylistTrack GROUP BY PlaylistId
```

# i/ni darbs
Dotas 15min. 2 Vaicājumi - jāatbilst nosacījumiem!

1. Uzrakstat vaicājumu, kas izvada nosaukumu un garumu (sekundēs) visām dziesmām (`Track`), kuras ir garākas par 1min (kolona - `Miliseconds`). Piezīme - tabulā dati ir milisekundēs, izvadē jāpārveido uz sekundēm.
2. Uzrakstat vaicājumu, kas izvada cik daudz rēķini (`Invoice`) ir katrā valstī (`BillingCountry`). Rezultātam vajadzētu būt sakārtotam no lielākā uz mazāko.

Iesniegt e-klasē pie šīs stundas. Saglabājat vai nu kā teksta (.txt) vai sql (.sql) failu.