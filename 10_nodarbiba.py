# Uzdevums: Uzrakstat programmu, 
# kurā lietotājs ievada vairāku cilvēku datus (vārds; uzvārds, vecums).
# Visiem laukiem jābūt atsevišķi (t.i. neapvienojat vārdu un uzvārdu).
# Individuālu cilvēka dati jāsaglabā vārdnīcā. 
# Vārdnīcas jāapvieno sarakstā. Saglabājat šos datus failā. 
# Uzsākot programmu izvadat šos datus ja fails eksistē.
#os.path.isfile(f"{faila_mape}\\nosaukums.json") # Izvada True vai False
# atkarībā no tā vai fails eksistē
# import os
# import json
# faila_mape = os.path.dirname(__file__)

# if os.path.isfile(f"{faila_mape}\\dati.json"):
#     with open(f"{faila_mape}/dati.json", "r", encoding="utf-8") as f:
#         cilveki = json.load(f)
#         print(cilveki)
# else:
#     print("Fails neeksistē!")

# cilveki = []
# while True:
#     vards = input('Vārds: ')
#     uzvards = input('Uzvārds: ')
#     vecums = int(input('Vecums: '))

#     cilveks = {
#         'vards': vards,
#         'uzvards': uzvards,
#         'vecums': vecums,
#     }
#     cilveki.append(cilveks)

#     if input("Beigt ievadi? (jā/nē)") == "jā":
#         break

# with open(f"{faila_mape}/dati.json", "w", encoding="utf-8") as f:
#     json.dump(cilveki, f)

#import os
# Pārbauda vai fails eksistē
#os.path.isfile("nosaukums")
# Pārbauda vai mape eksistē
#os.path.isdir("nosaukums")
# Pārbauda vai fails VAI mape eksistē
#os.path.exists("ceļš/uz/failu/vai/mapi")

# Iegūst ceļu (mapi) kurā atrodas fails
#os.path.dirname(__file__)

# Programmas argumenti
# [0] - Programmas atrašanās vieta (relatīva mapei kurā palaižat)
# import sys
# print(sys.argv[0])
# print(sys.argv[1])
# print(sys.argv[2])

# Absolūtie failu ceļi
# Piem. C:\Users\idmelkis\Desktop\11-4-2024\fails.json
# Relatīvie failu ceļi
# Piem. ja gribam nokļūt C:\Users\idmelkis\Desktop\11-6-2024\
# no. C:\Users\idmelkis\Desktop\11-4-2024\
# Relatīvais ceļš būs: ..\11-4-2024
# . - tekošā mape kurā esat, piem. .\10_nodarbiba.py - atver failu 10_nodarbiba.py šajā mapē
# .. - Mape vienu līmeni augstāk, piem C:\Users\idmelkis\Desktop\.. == C:\Users\idmelkis
# ../.. - Divus līmeņus augstāk
# ../../.. - Trīs, utt... -- C:\Users\idmelkis\Desktop\..\..\.. = C:\

# Var miksēt
#with open("C:\\Users\\idmelkis\\Desktop\\11-6-2024\\..\\11-4-2024\\10_nodarbiba.py", "r", encoding="utf-8") as f:
#    print(f.read())
# atver failu C:\Users\idmelkis\Desktop\11-4-2024\10_nodarbiba.py

# import pathlib
# p = pathlib.Path("ceļš/uz/failu")
# p.parents[0] # ceļš/uz
# p.parents[1] # ceļš

#import os
# with open("nosaukums", "w") as f:
#     pass
# # Izdzēš failu
# os.remove("nosaukums") # rm komanda konsole

# if not os.path.isdir("nosaukums"):
#     os.mkdir("nosaukums") # Izveido mapi
#     os.makedirs("nosaukums/mape1/mape2") # ļauj izveidot vairākas mapes

# Dzēst mapi - neļaus, ja mapē kaut kas ir
#os.rmdir("nosaukums")

# Lai izdzēstu mapi ar failiem.
# 1. var - izdzēšam visus failus
#cur_dir = os.path.dirname(__file__)
# for file in os.listdir("nosaukums"):
#     #os.remove(f"{cur_dir}\\nosaukums\\{file}") # absolūts ceļš
#     os.remove(f".\\nosaukums\\{file}") # relatīvais ceļš
# os.rmdir("nosaukums")

# 2. var - izmantot shell utils (shutils)
#import shutil
#shutil.rmtree("nosaukums")

# Uzdevums: Uzrakstat programmu kura izveido mapi "mape"
# Mapē izveidojat failus ar nosaukumiem no 1 līdz 100
import os
cur_dir = os.path.dirname(__file__)
if not os.path.isdir(f"{cur_dir}\\mape"):
    os.mkdir("mape")
for iii in range(1,101):
    with open(f"{cur_dir}\\mape\\{iii}", "w") as f:
        pass
import shutil
shutil.rmtree(f"{cur_dir}\\mape")