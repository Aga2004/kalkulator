import requests
import pandas as pd
pd.set_option('display.max_columns', None)
#
# def wszystkie_kraje():
#     url = "https://restcountries.com/v3.1/all?fields=name,flags,population,subregion,independent"
#     odpowiedz = requests.get(url)
#     dane = odpowiedz.json()
#
#     kraje = []
#     for x in dane:
#         nowy = {
#             "nazwa": x.get("name").get("common"),
#             "oficjalna_nazwa": x.get("name").get("official"),
#             "flaga": x.get("flags").get("png"),
#             "populacja": x.get("population"),
#             "niepodleglosc": x.get("independent"),
#             "region": x.get("subregion"),
#
#         }
#         kraje.append(nowy)
#
#     return kraje
#
# result = wszystkie_kraje()
#
# df = pd.DataFrame(result)
#
# df.to_excel("kraje.xlsx")
#
# print(df)



#import pandas as pd
#
# # numbers = [ 4,7,4,9,10]
# #
# # s=pd.Series(numbers)
# #
# # print(s)
#
# # Szereg - jednowymiarowa struktura
# s = pd.Series([10, 20, 30], index=['a', 'b', 'c'])
# # print(s["a"])
#
# # DataFrame - wielowymiarowa struktura
#
# # data = [
# #     {
# #         "miasto":"Warszawa",
# #         "temperatura": 20
# #     },
# #     {
# #         "miasto":"Kraków",
# #         "temperatura": 18
# #     }
# # ]
#
# data = {
#     "miasto": ["Warszawa","Kraków","Gdańsk"],
#     "temperatura": [10,20,30],
# }
#
# df = pd.DataFrame(data)
# a=df.iloc[0]
# f=df.iloc[0,1]
#
#
# print(f)
#
# df.to_excel("test.xlsx")

df = pd.read_excel("kraje.xlsx")

a = df.head()
b = df.tail(2)
c=df.describe()

d=df.columns

e=df.sort_values(by=['populacja'])

print(e)

