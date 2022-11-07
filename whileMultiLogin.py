# TAMAMLANMAMIŞ KOD 



accounts = [
    ["Berk Kesin","berkkeskin","berk123",True,0],
    ["Bulut Kuyumcu","bulutkuyumcu","bulut123",True,0],
    ["Efe Kurşun","Efe Kurşun","efe123",True,0],
    ["Cem Birinci","cembirinci","cem123",True,0],
    ["Ege Ugurbil","egeugurbil","ege123",True,0],
]

find_acc = False
account = None

while True:
    if find_acc == False:
        username = input("Enter your username: ")

    for i in accounts:
        if username == i[1]:
            account = i
            find_acc = True
            break

    if find_acc == False:
        continue

    password = input("Enter your password: ")
    if password == account[2]:
        if account[4] == 3:
            account[3] = False
            print("Your account is banned")
            break

        if account[3] == False:
            print("Your account is blocked.")
            break
        print("Login success")
        break
    else:
        print("Check your password")
        account[4] += 1


