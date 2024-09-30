# Uzdevums:
# Uzrakstat while ciklu, kas izvada skaitļus no 0 līdz 10, izlaižot skaitļus
# 4 un 6.
# x = 0
# while x <= 10:
#     x += 1
#     if x != 4 and x != 6:
#         print(x)

# Uzdevums: 
# Kalkulators kas ļauj ievadīt neierobežotu skaitu skaitļus 
# un darbības starp skaitļiem
# 
# Jāpārvieto darbības ievade uz ievades ciklu
# Jāpārslēdzas starp ievadēm (vienā iterācijā notiek skaitļa, otrā - darbības ievade)
# (Var izmantot modulus - %, operatoru)
skaitli = []
while True:
    if len(skaitli) % 2 == 0:
        skaitlis = input("Skaitlis: ")
        if skaitlis.isnumeric():
            skaitli.append(float(skaitlis))
        else:
            break
    else:
        darbiba = input("Darbība: ")
        if darbiba == "+" or darbiba == "-" or darbiba == "/" or darbiba == "*":
            skaitli.append(darbiba)
        else:
            break

# aprēķina ciklā jāņem vērā to, ka katra otrā vērtība ir darbība
rezultats = 0
darbiba = ""
for skaitlis in skaitli:
    # Hint: Glabājat darbību mainīgajā ārpus cikla
    if skaitlis == "+" or skaitlis == "-" or skaitlis == "/" or skaitlis == "*":
        darbiba = skaitlis
    else:
        if darbiba == "+":
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
        elif darbiba == "":
            rezultats = skaitlis
print(rezultats) # == 4

# Uzdevums: Pārveidot ievadi tā, lai var veikt vairākus darbību tipus
