# liste = [55, 77, 999, 10, 0, True, "hello"]
#
# liste.append("apple")
# liste.append(76)
# liste.insert(3, "cat")
# liste.insert(0, 99)
# hello_indeksi = liste.index("hello")
# adet_76 = liste.count(76)
# liste.remove(76)
# true_indeksi = liste.index(True)
# liste.pop(true_indeksi)
#
#
# def sum_of_squares(xs):
#     toplam = 0
#     for x in xs:
#         toplam += x ** 2
#     return toplam
#
#
#
# def cift_sayilar_toplami(sayilar):
#     toplam = 0
#     for sayi in sayilar:
#         if sayi % 2 == 0:
#             toplam += sayi
#     return toplam
#
#
#
# def bes_harfli_kelime_sayisi(kelimeler):
#     sayac = 0
#     for kelime in kelimeler:
#         if len(kelime) == 5:
#             sayac += 1
#     return sayac
#
#
# def ilk_cift_sayiya_kadar_toplam(sayilar):
#     toplam = 0
#     for sayi in sayilar:
#         if sayi % 2 == 0:
#             break
#         toplam += sayi
#     return toplam
#
#
#
# def sam_dahil_kelime_sayisi(kelimeler):
#     sayac = 0
#     for kelime in kelimeler:
#         sayac += 1
#         if kelime == "sam":
#             break
#     return sayac
#
#
#
# def replace(s, old, new):
#     pieces = s.split(old)
#     return new.join(pieces)
#
#
# def test(actual, expected):
#     if actual == expected:
#         print("PASSED")
#     else:
#         print("FAULT")
#
#
#
# test(replace("mississippi", "i","I"),"mIssIssIppI")
#
#
# def max(list):
#     x = 0
#     y = 1
#
#     for d in list:
#         if y >= len(list):
#             break
#         if list[x] > list[y]:
#             y += 1
#             continue
#         else:
#             x = y
#             y += 1
#
#     return print(list[x])
#
#
# max([1,2,3,4,5,6,7,8,9])


