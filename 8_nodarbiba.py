vardnica = {
    "1": 1,
    "2": 2,
    "3": 3
}

del vardnica["1"] # Izdzēst vārdnīca[atslēga]
#vardnica.pop("1")

# Uzdevums: (Dots) Tiek ģenerēts saraksts ar 20 vērtībām
# Ar ciklu izdzēst katru otro vērtību
# Vārdnīcas garums: len(vardnica)
import random
vardnica = {}
for iii in range(0, 20):
    vardnica[iii] = random.randint(1, 10)
print(vardnica)

for iii in range(0, 20, 2):
    del vardnica[iii]
print(vardnica)

#for key in vardnica.keys():
    #del vardnica[key]


# Izveidot vārdnīcu, kurā atrodas atslēgas un vērtības no dict1, 
# tām atslēgām kurām vērtības ir > 500, un izprintēt to.
# Piem, ja
# dict1 = {
#   1: 100,
#   2: 600,
#   3: 200,
#   4: 800
# }, tad
# dict2 = {
#   2: 600,
#   4: 800
# }
# Dots:
import random
dict1 = {}
for i in range(0, 20):
    dict1[i] = random.randint(0, 1000)
print(dict1)
dict2 = {}
for key, value in dict1.items():
    if value > 500:
        dict2[key] = value
print(dict2)

# Uzdevums
# Izveidot vārdnīcu no sarakstiem keys un values, kur keys ir atslēgas, un values ir vērtības
# Ir garantēts, ka keys un values sarakstu garumi ir vienādi.
import random
keys = [ 1, 2, "10", 3, random.randint(0, 100) ]
values = [ "viens", 4, False, [1,3,4], random.randint(0, 100) ]
rezultats = {}
for iii in range(0, len(keys)):
    rezultats[keys[iii]] = values[iii]
print(rezultats)

# i/ni uzdevums: Ir dota sekojoša vārdnīca
vardn = {
    'V': 10,
    'VI': 10,
    'VII': 40,
    'VIII': 20,
    'IX': 70,
    'X': 80,
    'XI': 40,
    'XII': 20
}
# Izveidot programmu, kura ar ciklu izveido vārdnīcu, kura satur skaitu
# tam, cik reizes atkārtojas vērtības vārdnīcā. (piem. 10 atkārtojas 2x,
# 20 atkārtojas 2x utt.). Izvadīt rezultātu. 
# Piezīme - Lai pārbaudītu vai vērtība ir vārdnīcā var izmantot if <vērtība> in <vārdnīca>