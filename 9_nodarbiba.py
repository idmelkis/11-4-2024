import json
# vardnica = {
#     "key": "value",
#     "True": True,
#     23: 32,
#     False: True
# }

# print(vardnica)
# vardnica_str = json.dumps(vardnica)
# print(vardnica_str)

# json_str = "{\"123\":true,\"312\":\"World\"}"
# json_var = json.loads(json_str)
# print(json_var)
#print(type(json_var))

# fails = open("nosaukums", "w")
# print("asd")
# fails.close()

#
import os
faila_mape = os.path.dirname(__file__)
# 1. Faila nosaukums - relatīvs PALAIŠANAS ceļam
# 2. Atvēršanas režīms
# r - read - Lasīšanas režīms
# w - write - Rakstīšanas režīms (Faila saturs tiek pārrakstīts)
# a - append - Galā rakstīšanas režīms (Faila saturs netiek pārrakstīts)
# w+ - write + read
# r+ - read + append
# Vairāk informācija: https://docs.python.org/3/tutorial/inputoutput.html#reading-and-writing-files
# 3. kodējums - izmantojam UTF-8 (unicode)
#with open(f"{faila_mape}\\nosaukums", "r", encoding="UTF-8") as file:
    # Rakstīšana:
    #f.write("ā")
    #f.writelines(["asd\n", "das\n", "asd\n"])
    # Lasīšana
    # for line in file:
    #     print(line.strip())
    #print(file.read(2))
    # file.seek(0)
    # print(file.read(2))
    #print(file.readlines())

#print("dsa")
vardnica = {
    "key": "value",
    "True": True,
    23: 32,
    False: True
}
# with open(f"{faila_mape}\\nosaukums.json", "r", encoding="UTF-8") as fails:
#     #fails.write(json.dumps(vardnica))
#     #json.dump(vardnica, fails)
#     # vardnica = json.loads(fails.read())
#     # print(vardnica)
#     vardnica = json.load(fails)
#     print(vardnica)

# Uzdevums: Uzrakstat programmu, 
# kurā lietotājs ievada vairāku cilvēku datus (vārds; uzvārds, vecums).
# Visiem laukiem jābūt atsevišķi (t.i. neapvienojat vārdu un uzvārdu).
# Individuālu cilvēka dati jāsaglabā vārdnīcā. 
# Vārdnīcas jāapvieno sarakstā.
# Saglabājat šos datus failā. 
# Uzsākot programmu izvadat šos datus ja fails eksistē.
import os
os.path.isfile(f"{faila_mape}\\nosaukums.json") # Izvada True vai False
# atkarībā no tā vai fails eksistē