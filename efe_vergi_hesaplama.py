# Information

kdvOran1 = 8
kdvOran2 = 18
# gideri alıyorum
gider = int(input("Bu ay ne kadar fatura girişi oldu ? : "))
# geliri alıyorum
gelir = int(input("Bu ay ne kadar fatura kestiniz ? : "))

# kdvsiz gideri hesaplıyorum
# (gelir-gider) * 0.3
kar = gelir-gider
gelirVergisi = kar * 0.3

# kdv hesaplama
kdv_8 = gelir * kdvOran1 / 100
kdv_18 = (gelir * kdvOran2) / 100

# kdvler çıktıktan sonraki kazanc
# kdv %18 ise net kazanç
netKazanc18 = (gelir - gelirVergisi) - kdv_18
# kdv %8 ise net kazanç
netKazanc8 = (gelir - gelirVergisi) - kdv_8

""" aylık %18 e gmre """


"""if netKazanc18 <= 14.800:
    GelirVergisi = (AylikKazanc * 15) // 100
    netKazanac = AylikKazanc - GelirVergisi
    print("bu ayki kazncınız {} tl'dir".format(netKazanac))
elif netKazanc18 > 14.800 and netKazanc18 < 35.000:
    GelirVergisi = (AylikKazanc * 20) // 100
    netKazanc = AylikKazanc - GelirVergisi
    print("bu ayki kazncınız {} tl'dir".format(netKazanc))
else:
    AylikKazanc > 35.000
   GelirVergisi = (AylikKazanc * 30) // 100
    netKazanc = AylikKazanc - GelirVergisi
    print("bu ayki kazancınız {} tl'dir".format(netKazanc))"""