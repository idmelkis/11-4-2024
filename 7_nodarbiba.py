#saraksts = []
#kortezs = ()

# Atslēga <=> Vērtība
vards = "Jānis"
vardnica = {
    "vards": "Janis",
    "uzvards": "Eglitis",
    "atslega": "vertiba",
    vards: vards,
    1: "Viens",
    2: "Divi",
    5: "Trīs"
}
print(vardnica)

print(vardnica[vards])
#print(vardnica[4])

# Uzdevums: Izmantot vārdnīcas lai pārveidotu tekstā burtus āēīū formā bez
# garumzīmes, t.i. aeiu
burti = {
    "ā": "a",
    "ē": "e",
    "ī": "i",
    "ū": "u",
}
def changeLetter(text):
    result = ""
    for letter in text:
        if letter in burti:
            result += burti[letter]
        else:
            result += letter
    return result
print(changeLetter("Māja"))
print(changeLetter("Vējš"))
print(changeLetter("Vētra"))

#print(burti.keys())
#print(burti.values())
# print(burti.items())
# for j,k in burti.items():
#     print(f"Atslēga {j}, Vērtība {k}")

burti["ķ"] = "k"
burti["ō"] = "o"
print(burti)

burti.update({"ž": "z", "č": "c", "ļ": "l"})
print(burti)

# Uzdevums
# Uzrakstīt programmu, kas izveido vārdnīcu, kurā atslēgas 
# ir skaitļi no 1 līdz n (lietotāja ievadīts skaitlis) 
# un vērtības ir šis skaitlis kvadrātā.
# piem.
# 1: 1
# 2: 4
# 3: 9
# 4: 16
skaitli = {}
n = int(input("Ievadat skaitli"))
for iii in range(1, n+1):
    skaitli[iii] = iii*iii
    #skaitli.update({iii: iii*iii})
print(skaitli)

#print(burti.keys())
#print(burti.values())
# print(burti.items())
# for j,k in burti.items():
#     print(f"Atslēga {j}, Vērtība {k}")

# Uzdevums: Pacelt vērtības iekš vārdnīcas kvadrātā
vardnica = {
    1: 1,
    "a": 2,
    3: 3
}
# Piem. 
# vardnica = {
#     1: 1,
#     "a": 4,
#     3: 9
# }
for j,k in vardnica.items():
    #print(f"Atslēga {j}, Vērtība {k}")
    vardnica[j] = vardnica[j] * vardnica[j]
print(vardnica)

# Uzdevums:
# Apvienot vārdnīcas iekš mainīgā dict3
dict1 = {
    1: 10,
    2: 20,
    3: 30
}
dict2 = {
    4: 40,
    5: 50,
    6: 60
}
dict3 = { 
    # ...
}

# for j,k in dict1.items():
#     dict3[j] = dict1[j]
# for j,k in dict2.items():
#     dict3[j] = dict2[j]
# print(dict3)

for i in (dict1, dict2): 
    dict3.update(i) # dict3.update({1: 10, 2: 20, 3: 30}, {4: 40, 5: 50, 6: 60})