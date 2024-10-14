# Spēle: Uzmini skaitli
# Uzdevums: Spēle "Uzmini skaitli"
# Spēle uzģenerē nejaušu skaitli izmantojot sekojošo kodu:
# import random
# skaitlis = random.randint(0, 100)

# Jāuzraksta cikls, kurā lietotājs ievada skaitli (input).
# Programma pārbauda vai skaitlis ir uzminēts,
# ja nav, izvada, vai ievadītais skaitlis ir lielāks, 
#  vai mazāks par nejaušo skaitli.
# Visas lietotāja ievades (minējumus) jāsaglabā sarakstā
# Kad lietotājs ir uzminējis skaitli - 
# Izvadīt 'Uzvara', minējumu skaitu (len(...)) un visus lietotāja minējumus
# skaitli = []
# x = 0
# while True: #x != skaitlis:
#     x = int(input("Ievade:"))
#     skaitli.append(x)
#     if x > skaitlis:
#         print("Ievade ir lielāka")
#     elif x < skaitlis:
#         print("Ievade ir mazāka")
#     else:
#         print("Uzvara")
#         print(f"Spēle beidzās pēc {len(skaitli)} minējumiem. Minējumi:")
#         print(skaitli)
#         break
#     # ...
    
# Funkcijas
# Nosaukumi:
# vardsVards
# vards_vards
def nosaukums():
    pass
def sum(param1 :int, param2 :int = 2) -> int:
    """Komentārs"""
    return param1 + param2;
print(sum(1))

x = 1
x = 2

def printSomething(ievade :str):
    print(ievade)
printSomething("kautkas")
print("")
def printSomething(ievade :str):
    print("*"*10)
    print(ievade)
    print("*"*10)
printSomething("kautkas")

def bezgaligaIevade(pirmaisSkaitlis :int, *mainigie, kautkasCits):
    print(mainigie)
    print(f"pirmais: {pirmaisSkaitlis}, kautkasCits: {kautkasCits}")
bezgaligaIevade(1,2,3,4,5,kautkasCits=6)


# Uzdevums
# Lietotājs ievada vairākus skaitļus:
# def skaitluIevade():
#     skaitli = []
#     while True:
#         ievade = input("Skaitlis:")
#         if ievade.isdigit():
#             skaitli.append(int(ievade))
#         else:
#             break
#     return skaitli
# # Jāuzraksta funkcija, kas saskaita šo skaitļu summu
# def summa(skaitli: 'list[int]'):
#     summa = 0
#     for skaitlis in skaitli:
#         summa += skaitlis
#     return summa
# print(summa(skaitluIevade()))
# print(summa(skaitluIevade()))
# print(summa(skaitluIevade()))
# print(summa(skaitluIevade()))

# def recurse(param1):
#     print(param1)
#     if param1 > 0:
#         return recurse(param1-1)
#     else:
#         return
# print(recurse(2000))

# x = 2000
# while x > 0:
#     print(x)
#     x -= 1


def factorial(n):
   if n == 1:
        return 1
   else:
        return n * factorial(n-1)
print(factorial(5)) # 4! = 4 * 3 * 2 * 1 (24)

n = 5
rezultats = 1
while n > 0:
    rezultats *= n
    n -= 1
print(rezultats)


# Uzdevums - Factoriālis kā while cikls


# Uzdevums: Apmainat vietām mainīgo a un b vērtības
a = 5
b = 11
def swap():
    global a, b
    # ????
print(a, b) # === 11, 5
