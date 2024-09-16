#asa3 = [int, bool, float, str, chr, list] 
teksts = "Šodien ir "
datums = 16
#print(teksts + str(datums))
#print("Šodien ir " + str(datums) + " datums!")
#print(f"{teksts}{datums} datums!")

#print(f"Rinda1\nRinda2")
print("""Rinda1
Rinda2""")

# Komentārs
"""
Komentārs
Vairākās
Rindās
"""

# ievade = input("Ievade: ")
# int(ievade)
# ievade.isdecimal()

# if <expr>:
a = 10
b = a == 10
# > lielāks
# < mazāks
# <=
# >=
# !=, <> - nav vienāds
# not- negatīvs
# is, ==
#if not a == 10:
# if a is 10:
#     print("Taisnība")
if a >= 10:
    print("Taisnība")
if not "" is "1":
    print("Not is -- True")

#a = [ "123", "321", 10 ]
a = [ 'A', 'B', 'C' ]
# ==
b = "ABC"
print(b[1])
#b[1] = "E" # Nestrādās
c = ( a, b ) # Tuple
#c[1] = 10
print(c[1])

# Uzdevums: Kalkulators
# Ievade - Divi skaitļi un darbība
# Izvade - Rezultāts
a = float(input("1. Skaitlis: "))
b = float(input("2. Skaitlis: "))
c = input("Darbība: ")
if c is "+":
    print(a+b)
elif c == "-":
    print(a-b)
elif c == "/":
    if b != 0.0:
        print(a/b)
    else:
        print("Dalīšana ar 0!")
elif c == "*":
    print(a*b)

# match c:
#     case "+":
#         print(a+b)
#     case "-":
#         print(a-b)
#     #...