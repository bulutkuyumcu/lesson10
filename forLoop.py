liste = [1,2,3,4,5,6,7,8,9,10]

for i in liste:
    if i == liste[7]:
        break # Döngüyü kırar ve çıkar
    if i == liste[2]:
        continue # Döngüyü başa alır ve diğer adımdan devam eder.
    print(i)
