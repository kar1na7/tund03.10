"""Iseseisev praktiline töö"""

# Kirjuta kood mis:
# 1) küsib kasutajalt ainult täisarve a ja b
# 2) tagastab kasutajale a ja b summa, korrutise ja ruutude summa
# all on sulle vastuse näide koos andmetüübiga f-sõne, proovi jutumärkide sisse panna loogsulud {}

a = int(input("Sisesta oma a "))
b = int(input("Sisesta oma b "))
print(f"SUMMA:", int(a) + int(b))
print(f"KORRUTIS:",int(a) * int(b) )
print(f"RUUTUDE SUMMA:",a*a + b*b)
