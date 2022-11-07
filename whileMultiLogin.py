# Hesaplar listesi olsun
# Hesapların içerisinde
# ad,soyad,kullanıcı adı,şifre,hesap durumu
# ve hesaba özel hatalı giriş sayısı bulunsun.
# Kullanıcı girişi yapılırken eğer hatalı giriş yapılırsa
# tekrar kullanıcı bilgisi sorulsun
# 3 hatalı girişte hesap kapatılsın
# Doğru giriş yapıldığında hatalı giriş sıfırlansın ve isim soyisim
# ile karşılama yapılsın

# name surname, username, password, status, attempLoginCount
accounts = [
    ["Berk Keskin","berkkeskin07","123123",True,0],
    ["Cem Birinci","cembirinci","234234",True,0],
    ["Efe Kurşun","efekursun","345345",True,0],
    ["Bulut Kuyumcu","bulutkuyumcu","567567",True,0],
    ["Ege Uğurbil","egeugurbil","678678",True,0],
]
find_acc = False
account = None

while True:
    # Kullanıcı adı girişi yapıldı mı?
    if find_acc == False:
        username = input("Enter your username: ")

    # Kullanıcı adına göre hesabı bul
    # Bulduğun hesabı account'a liste olarak ata
    for i in accounts:
        if username == i[1]:
            account = i
            find_acc = True
            break

    # Hesap bulamadıysan en başa dön ve tekrar kullanıcı adı al
    if find_acc == False:
        continue

    # Bulunan hesap için şifre sor
    password = input("Enter your password: ")

    # Hesaba 3. kez hatalı giriş var ise banla
    if account[4] == 3:
        account[3] = False  # Hesabı banla
        account[4] = 0  # Hatalı girişi sıfırla
        print("Your account is banned.")
        break
    # Hesap banlı mı?
    if account[3] == False:
        print("You account is blocked.")
        break

    # Şifre eşleşiyor ise giriş yap
    if password == account[2]:
        print("Login success")
        account[4] = 0 # Hatalı giriş sayısını sıfırla
        break
    else:
        print("Check your password")
        account[4] += 1 # Hatalı giriş sayısını 1 arttır.
        continue