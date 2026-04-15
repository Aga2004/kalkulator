import requests

odpowiedz = requests.get("https://restcountries.com/v3.1/name/poland")
dane = odpowiedz.json()[0]

kraj = ", ".join(dane.get("altSpellings"))

#print(kraj)

waluta = dane.get("currencies").get("PLN").get("name")
#waluta1 = dane.get("currencies").get("PLN").get("symbol")

#print(waluta + " " +waluta1)

stolica = dane.get("capital")[0]

#print(stolica)

sasiedzi =", ".join(dane.get("borders"))
#print(sasiedzi)

flaga=dane.get("flags").get("png")
#print(flaga)


def polska(
        kraj = dane.get("altSpellings"),
        stolica = dane.get("capital")[0],
        waluta =  dane.get("currencies").get("PLN").get("name"),
        sasiedzi = ", ".join(dane.get("borders")),
        flaga=dane.get("flags").get("png"),
):

    return f"{kraj},  {waluta},  {stolica},  {sasiedzi},  {flaga}"

pol = polska(kraj, stolica, waluta, sasiedzi, flaga)
print(pol)

