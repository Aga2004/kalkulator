# 1.
# Napisz 3 zmienne zawierające imię, nazwisko i miasto użytkownika.
# Następnie napisz zmienną wynik w której za pomocą konkatenacji połączysz powyższe zmienne i inne słowa w zdanie:
# "To jest Jan Kowalski. Jego miejsce urodzenia to Poznań"

imie = "Kasia"
nazwisko = "Kowalska"
miasto = "Krakow"

wynik = f"To jest {imie} {nazwisko}. Jej miejsce urodzenia to {miasto}"
#print (wynik)

# 2.
# W twoim programie znajduje się zmienna:
# result = "to jest krótkie zdanie na temat Jana"
# Za pomocą odpowiedniej metody zastąp wszystkie spacje " ", myślnikami "-". Wynik zapisz w nowej zmiennej i wyświetl ją w konsoli

result = "to jest krótkie zdanie na temat Jana"
wynik= result.replace(" ","-")
#print (wynik)

# 3.
# W twoim programie znajduje się zmienna:
# greeting = "hello world"
#
# a) W nowej zmiennej za pomocą odpowiedniej metody policz długość stringa z powyższej zmiennej
# b) W kolejnej zmiennej dźwignij wszystkie litery zmiennej do dużej litery
# c) W jeszcze jednej zmiennej dźwignij do dużej litery tylko pierwszą literę

greeting = "hello world"
dlugosc = len(greeting)
#print (dlugosc)
duze = greeting.upper()
#print(duze)
pierwsza=greeting.capitalize()
#print(pierwsza)

# 4.
# W twoim programie znajduje się zmienna:
# movie = "lord of the rings"
#
# Za pomocą odpowiedniej metody dźwignij pierwszą literę każdego wyrazu do dużej litery

movie = "lord of the rings"
duze=movie.title()
# print(duze)

# 5.
# W twoim programie znajduje się zmienna:
# movie = "dzisiaj jest sobota"
#
# Za pomocą odpowiedniej metody sprawdź jaka litera znajduję się na 5 miejscu w stringu

movie = "dzisiaj jest sobota"
jaka=movie[4]
# print(jaka)

# a:int = int(input("Podaj a: "))
# b:int = int(input("Podaj b: "))
# wyn=a+b
# print(wyn)

pot = 2**4
#print(pot)

