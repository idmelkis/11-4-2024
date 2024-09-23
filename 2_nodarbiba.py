#sar = [ "123", "das" ]
#newval = "!!!"
#sar.append(newval)
#print(sar)
#print(sar[0:2]) # sar[<sākums>:<beigas>]
#print("Teksts"[3:])
#print(",".join(sar))

# Tukši cikli/if/funkcijas ar pass:
# while True:
#     pass
# if a == 1:
#     pass
# elif a == 2:
#     pass

# for i in range(0, 10):
#     print(i)

# a = 0
# while a <= 3:
#     a += 1
#     if a == 2:
#         continue
#     print(f"Cikls {a}")
#     if a == 3:
#         break
# else:
#     print("Beidzās!")

# for i in range(0, 4):
# ...

# Uzdevums: Pārveidot for ciklu while ciklā
sar = ["21", "312", "2", "312", "aaa"]

for s in sar[0::2]:
    print(s)

print("====")

a = 0
while a < len(sar):
    print(sar[a])
    a += 2


# Uzdevums: 
# Kalkulators kas ļauj ievadīt neierobežotu skaitu skaitļus
# Visiem skaitļiem viena darbība

darbiba = input("Darbība: ")
skaitli = []
# sk = int(input("Darbību skaits: "))
# a = 0
# while a <= sk:
while True:
    skaitlis = input("Skaitlis: ")
    if skaitlis.isnumeric():
        skaitli.append(float(skaitlis))
    else:
        break

rezultats = 0
for skaitlis in skaitli:
    if darbiba is "+":
        rezultats = rezultats+skaitlis
    elif darbiba == "-":
        rezultats = rezultats-skaitlis
    elif darbiba == "/":
        if skaitlis != 0.0:
            rezultats = rezultats/skaitlis
        else:
            print("Dalīšana ar 0!")
    elif darbiba == "*":
        rezultats = rezultats*skaitlis
print(skaitli)
print(rezultats)

# Uzdevums: Pārveidot ievadi tā, lai var veikt vairākus darbību tipus
