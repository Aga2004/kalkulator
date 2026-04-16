def dodawanie (b,c):
    return(b+c)
def odejmowanie (b,c):
    return(b-c)
def mnozenie (b,c):
    return(b*c)
def dzielenie (b,c):
    return(b/c) if c!=0 else "Gluptasku! nie mozna dzielic przez 0!"
def potega (b,c):
    return (b**c)

while True:
    try:
        a: int = int(input(" 1. Dodawanie \n 2. Odejmowanie \n 3. Mnożenie \n 4. Dzielenie \n 5. Potegowanie \n 6. Zakonczenie \n  Wybierz operacje "))
    except ValueError:
        print("Nie podales liczby")
        continue

    if   a == 6:
        print("Papa")
        break

    if a in [1,2,3,4,5]:
        try:
            b: int = int(input("Pierwsza liczba: "))
            c: int = int(input("Druga liczba: "))
        except ValueError:
            print("Nie podales liczby")
            continue

    if a == 1:
        print(dodawanie (b, c))
    elif a == 2:
        print(odejmowanie (b, c))
    elif a == 3:
        print(mnozenie(b,c))
    elif a == 4:
        print(dzielenie (b,c))
    elif a == 5:
        print(potega (b,c))
    else:
        print("Nie ma takiej operacji. Wybierz inna")

