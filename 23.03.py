#ilość znaków
len("abc123d")

#zmieniamy parametry w nawiasie
def powitanie(imie):
    print(f"cześć {imie}")

#powitanie("Błażej")
#powitanie("Aga")

def dzielenie(x, y):
    if y==0:
        return "nie dzielimy przez 0"
    print(x/y)

#dzielenie(1,0)

#1

def obliczenia(x, y, z):
    return x * y * z
wynik=obliczenia(1, 2, 3)
#print(wynik)

#2

def witaj(imie, miasto):
    return f"witaj {imie} z {miasto}"
czesc=witaj("Kasia", "Kraków")
#print(czesc)

#3

def stopnie(kelwin):
     cels = kelwin - 273
     return cels

temp = stopnie(350)
#print(temp)

#4

def pole(a, b):
    return a * b * 0.5

troj=pole(5,3)
#print(troj)

#lambda
l_odejmowanie = lambda m,n: m-n

wynik2 = l_odejmowanie(20,3)

#print(wynik2)

#1

l_obliczenia1 = lambda x, y, z: x*y*z

wynik_1 = l_obliczenia1(1, 2, 3)
#print(wynik_1)


#2

l_witaj1 = lambda imie, miasto: f"witaj {imie} z {miasto}"

czesc_1 = l_witaj1("Kasia", "Kraków")
#print(czesc_1)

#3

l_stopnie1 = lambda kelwin: kelwin - 273

temp_1=stopnie(300)
#print(temp_1)

#4

l_pole = lambda a, b: a * b * 0.5

troj_1=pole(5,3)
#print(troj_1)

