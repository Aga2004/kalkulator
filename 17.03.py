#typ prosty: bool / boolean

zalogowano = True
eu = False

tytul = "567"

sprawdz = tytul.isnumeric()

#operatory liczbowe > < >= <= ==

#if else elif
x = 5
if x>5:
    print("x jest wieksze niz 5")
else:
    print("x nie jest wieksze niz 5")

typ_konta = "mo"

if typ_konta == "admin":
    print("eitj w panelu admina")
elif typ_konta == "moder":
    print("eitj w panelu modera")
else:
    print("nie wiadomo")

#and or
jezyk = "python"
wersja = 3.01

if jezyk == "python" and wersja > 3.10:
    print("start szkolenia")
else:
    print("zla wersja")

