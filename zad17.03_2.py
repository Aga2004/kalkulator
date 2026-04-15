#1
user_role = "admin"
is_logged = True

if user_role == "admin" and is_logged == True:
    print("WItaj w panelu admina")
elif user_role == "moderator" and is_logged == True:
    print("WItaj w panelu moderatora")
elif is_logged == True:
    print("WItaj w panelu uzytkwnika")
else:
    print("blad logowania")

#2

user_country = "Polska"
if user_country == "Polska" or user_country == "Niemcy" or user_country == "Czechy":
    print("dostawa mozliwa")
else:
    print("dostawa towaru niemozliwa:(")

#3

godz = input("ktora godzina? ")
godz = int(godz)

if godz >= 6 and godz <= 12:
    print("good morning")
elif godz > 12 and godz <= 18:
    print("good afternoon")
else:
    print("good evening")
