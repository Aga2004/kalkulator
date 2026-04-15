# #1
# imiona = ["Kasia", "Jan", "Basia"]
#
# for imie in imiona:
#     print(f" To jest {imie}")
#
# #2
# tekst = "w29iwwnas292i2929"
# for lit in tekst:
#     if lit.isnumeric():
#         continue
#     print(lit)
#
# #3
# suma = 0
# for i in range (1, 51):
#     if i % 3 == 0:
#         suma += i
# print(suma)
#
#
# #4
#
# for l in range (1,102):
#     if l % 3 == 0 and l % 5 == 0:
#        print("fizzbuzz")
#     elif l % 5 == 0:
#         print("buzz")
#     elif l % 3 == 0:
#         print("fizz")
#     else:
#        print(l)
#
# #1
# lista = [ ]
#
# lista.append(5)
# lista.append(13)
# print(lista)
#
# #2
# list1 = [1, 2, 3]
# list2 = [4, 5, 6]
#
# list1.extend(list2)
# print(list1)
#
# #3
#
# my_list = [1, 2, 3, 4, 2]
# my_list.pop(1)
# print(my_list)
#
# #4
# my_list1 = [10, 20, 40, 30, 20]
# ilość = my_list1.index(40)
# print(ilość)
#
# #5
# my_list2 = [1, 2, 2, 3, 2, 4, 2]
#
# suma = my_list2.count(2)
# print(suma)

# #1
# nums = [1, 2, 3, 4, 5]
# po2 = [num*2 for num in nums]
# print(po2)
#
# #2
# nums1 = [1, 2, 3, 4, 5, 6]
# parzyste = list(filter(lambda i: i % 2 == 0, nums1))
#
# print(parzyste)
# #3
# words = ["kot", "pies", "ryba"]
# wielkie = list(map(lambda word: word.upper(), words))
# print (wielkie)
# #4
#
# nums4 = [1, 2, 3, 4, 5]
# liczby = [x * x for x in nums4 if x > 3]
#
# print(liczby)
# #5
# words5 = ["ala", "kot", "samochód", "dom", "rower"]
# lista5 = list(filter(lambda l: len(l)>3, words5))
# print(lista5)

