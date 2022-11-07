# Information

# Database #
dbUsername = "Ege"
dbPass = "22335"

print("-----------Login pls----------------")
inputUsername = input("Enter username: ")
if inputUsername == dbUsername:
    inputPassword = input("Enter password: ")
    if inputPassword == dbPass:
        print("You have logged in")
    else:
        print("Check your password")
else:
    print("Account not found")

print("-------------------------------")
