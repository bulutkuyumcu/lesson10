for i in range(1,101):
    if i % 2 == 0:
        continue
    if i == 63:
        break
    print(i)


# Soru
"""Kullanıcıdan alınan 2 sayı arasındaki sayıların toplamayı veren algoritmayı yazınız.
Örneğin kullanıcıdan 1 ve 5 alınırsa 2+3+4= 9 sonucu gelsin"""


sayı1 = int(input("1. Sayıyı giriniz: "))
sayı2 = int(input("2. sayıyı giriniz: "))

toplam = 0

for i in range(sayı1+1,sayı2):
    toplam += i
print("{} sayısı ile {} sayısı arasındaki sayıların toplamı {}".format(sayı1,sayı2,toplam))