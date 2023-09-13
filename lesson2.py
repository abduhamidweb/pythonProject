import math

# # Kvadratning tomonini a deb o'rnating
# a = float(input("Kvadrat tomonini kiriting: "))
#
# # Perimetrni hisoblash
# P = 4 * a
#
# # Perimetrga chiqaring
# print("Kvadratning perimetri:", P)





# # Kvadratning tomonini a deb o'rnating
# a = float(input("Kvadrat tomonini kiriting: "))
#
# # Yuzani hisoblash
# S = a**2
#
# # Yuzani chiqaring
# print("Kvadratning yuzasi:", S)





# # To'g'ri to'rtburchakning tomonlarini a va b deb o'rnating
# a = float(input("To'g'ri to'rtburchakning birinchi tomonini kiriting: "))
# b = float(input("To'g'ri to'rtburchakning ikkinchi tomonini kiriting: "))
#
# # Yuzani hisoblash
# S = a * b
#
# # Perimetrga chiqaring
# P = 2 * (a + b)
#
# # Yuzani va perimetrga chiqaring
# print("To'g'ri to'rtburchakning yuzasi:", S)
# print("To'g'ri to'rtburchakning perimetri:", P)



# # Aylananing diametri d ni kiriting
# d = float(input("Aylananing diametrini kiriting: "))
#
# # Aylananing uzunligini hisoblash
# L = 3.14 * d
#
# # Aylananing uzunligini chiqaring
# print("Aylananing uzunligi:", L)



# # Kubning yon tomonini a ni kiriting
# a = float(input("Kubning yon tomonini kiriting: "))
#
# # Kubning hajmini hisoblash
# V = a ** 3
#
# # Kubning to'la sirtini hisoblash
# S = 6 * a ** 2
#
# # Hajmini va to'la sirtini chiqaring
# print("Kubning hajmi:", V)
# print("Kubning to'la sirti:", S)


# # Paralelepepidning tomonlarini a, b, c ni kiriting
# a = float(input("a ni kiriting: "))
# b = float(input("b ni kiriting: "))
# c = float(input("c ni kiriting: "))
#
# # Paralelepepidning hajmini hisoblash
# V = a * b * c
#
# # Paralelepepidning to'la sirtini hisoblash
# S = 2 * (a * b + b * c + a * c)
#
# # Hajmini va to'la sirtini chiqaring
# print("Paralelepepidning hajmi:", V)
# print("Paralelepepidning to'la sirti:", S)




# # Doiraning radiusini R ni kiriting
# R = float(input("Doiraning radiusini kiriting: "))
#
# # Doiraning uzunligini hisoblash
# L = 2 * math.pi * R
#
# # Doiraning yuzasini hisoblash
# S = math.pi * R ** 2
#
# # Uzunligini va yuzasini chiqaring
# print("Doiraning uzunligi:", L)
# print("Doiraning yuzasi:", S)



# # Ikkita sonni a va b ni kiriting
# a = float(input("a ni kiriting: "))
# b = float(input("b ni kiriting: "))
#
# # Ikkita sonning o'rta arifmetigini hisoblash
# orta_arifmetik = (a + b) / 2
#
# # O'rta arifmetigini chiqaring
# print("Ikkita sonning o'rta arifmetigi:", orta_arifmetik)


# # Uzunlikni santimetrda kiriting
# L = int(input("Uzunlikni santimetrda kiriting: "))
#
# # Metrlar sonini hisoblash
# metrlar = L // 100
#
# # Metrlar sonini chiqaring
# print("Metrlar soni:", metrlar)


# # Og'irlikni kilogramda kiriting
# M = int(input("Og'irlikni kilogramda kiriting: "))
#
# # Tonnalar sonini hisoblash
# tonnalar = M // 1000
#
# # Tonnalar sonini chiqaring
# print("Tonnalar soni:", tonnalar)



# # Fayl hajmini baytlarda kiriting
# baytlar = int(input("Fayl hajmini baytlarda kiriting: "))
#
# # Kilobaytlarda ifodalash
# kilobaytlar = baytlar // 1024
#
# # Kilobaytlarda ifodalashni chiqaring
# print("Fayl hajmi kilobaytlarda:", kilobaytlar)


# # A va B sonlarini kiriting
# A = int(input("A ni kiriting: "))
# B = int(input("B ni kiriting: "))
#
# # A kesmada B kesmani necha marta joylashtirish mumkinligini hisoblash
# marta = A // B
#
# # Natijani chiqaring
# print("A kesmada B kesmani joylashtirish mumkinligi:", marta)



# # A va B sonlarini kiriting
# A = int(input("A ni kiriting: "))
# B = int(input("B ni kiriting: "))
#
# # A kesmada B kesmani necha marta joylashtirish mumkinligini hisoblash
# qismiqolmagan = A % B
#
# # Natijani chiqaring
# print("A kesmada B kesmaning joylashmagan qismi:", qismiqolmagan)


# # Ikki xonali sonni kiriting
# son = int(input("Ikki xonali sonni kiriting: "))
#
# # O'nliklar xonasidagi raqamni aniqlash
# onliklar_xonasi = (son // 10) % 10
#
# # Natijani chiqaring
# print("O'nliklar xonasidagi raqam:", onliklar_xonasi)


# # Ikki xonali sonni kiriting
# son = int(input("Ikki xonali sonni kiriting: "))
#
# # Raqamlar yig'indisini hisoblash
# yigindi = (son // 10) + (son % 10)
#
# # Natijani chiqaring
# print("Raqamlar yig'indisi:", yigindi)



# # Uch xonali sonni kiriting
# son = int(input("Uch xonali sonni kiriting: "))
#
# # Yuzlar xonasidagi raqamni aniqlash
# yuzlar_xonasi = (son // 100) % 10
#
# # Natijani chiqaring
# print("Yuzlar xonasidagi raqam:", yuzlar_xonasi)




# # Uch xonali sonni kiriting
# son = int(input("Uch xonali sonni kiriting: "))
#
# # O'nliklar va birliklar xonasidagi raqamlarni aniqlash
# onliklar_xonasi = (son // 10) % 10
# birliklar_xonasi = son % 10
#
# # Natijani chiqaring
# print("O'nliklar xonasidagi raqam:", onliklar_xonasi)
# print("Birliklar xonasidagi raqam:", birliklar_xonasi)





# # Uch xonali sonni kiriting
# son = int(input("Uch xonali sonni kiriting: "))
#
# # Raqamlar yig'indisini hisoblash
# raqamlar_yigindisi = (son // 100) + ((son // 10) % 10) + (son % 10)
#
# # Natijani chiqaring
# print("Raqamlar yig'indisi:", raqamlar_yigindisi)




# # Uch xonali sonni kiriting
# son = int(input("Uch xonali sonni kiriting: "))
#
# # Raqamlarni teskari tartibda yozishdan hosil bo'lgan sonni hisoblash
# teskari_son = (son % 10) * 100 + ((son // 10) % 10) * 10 + (son // 100)
#
# # Natijani chiqaring
# print("Teskari tartibda yozilgan son:", teskari_son)





# # Uch xonali sonni kiriting
# son = int(input("Uch xonali sonni kiriting: "))
#
# # Raqamlarni ajratib olish
# birliklar = son % 10
# onliklar = (son // 10) % 10
# yuzliklar = son // 100
#
# # Natijani chiqaring
# print("Yuzliklar:", yuzliklar)
# print("O'nliklar:", onliklar)
# print("Birliklar:", birliklar)
