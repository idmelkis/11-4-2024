# Uzdevums:
# Uzrakstīt ciklu, kas iet pāri skaitļiem no 1 līdz 100, UN
# Ja skaitlis dalās ar 3, izvada vārdu "Fizz"
# Ja skaitlis dalās ar 5, izvada vārdu "Buzz"
# Attiecīgi, ja skaitlis dalās ar 3 un 5, izvada FizzBuzz
# Ja skaitlis nedalās ar nevienu no šiem skaitļiem, izvadat to
# Dalīšanas atlikuma pārbaudei izmatot - % - modulus operators
# Piem.
# 4 % 2 == 0
# 5 % 2 == 1
# Iepriekšējo stundu materiāli: https://github.com/idmelkis/11-4-2024
for iii in range(1,101):
    #print(f"Skaitlis: {iii}, Dalot ar 3: {iii % 3}")
    if iii % 3 == 0 and iii % 5 == 0:
        print("FizzBuzz")
    elif iii % 3 == 0:
        print("Fizz")
    elif iii % 5 == 0:
        print("Buzz")
    else:
        print(iii)

# Uzdevums:
# Uzrakstīt ciklu, kas 
# * ļauj lietotājam ievadīt vērtību un programma saglabā to
# * izvada visu ievadīto skaitļu vidējo vērtību (pēc ievades)
# * programma beidz darbu, kad lietotājs ievada kādu burtu
#piemērs  -
# Iterācija 1: ievada 2, izvada 2
# Iterācija 2: ievada 4, izvada 3 (2, 4)
# Iterācija 3: ievada 10, izvada 5.3 (2, 4, 10)

skaitli = []
while True:
    skaitlis = input("Skaitlis: ")
    if skaitlis.isnumeric():
        skaitli.append(int(skaitlis))
        print(f"Vidējais: {sum(skaitli)/len(skaitli)}, Skaitli: {skaitli}")
        # summa = 0
        # for iii in skaitli:
        #     summa += iii
        # print(summa/len(skaitli))
    else:
        break

# Spēle: Uzmini skaitli
# Uzdevums: Spēle "Uzmini skaitli"
# Spēle uzģenerē nejaušu skaitli izmantojot sekojošo kodu:
import random
skaitlis = random.randint(0, 100)
# Jāuzraksta cikls, kurā lietotājs ievada skaitli (input).
# Programma pārbauda vai skaitlis ir uzminēts,
# ja nav, izvada, vai ievadītais skaitlis ir lielāks, 
#  vai mazāks par nejaušo skaitli.
# Visas lietotāja ievades (minējumus) jāsaglabā sarakstā
# Kad lietotājs ir uzminējis skaitli - 
# Izvadīt 'Uzvara', minējumu skaitu (len(...)) un visus lietotāja minējumus