import getpass

username = "David"
password = "Davidpogi"

u = input("Input USERNAME --->")
y = input("Input PASSWORD --->")

if u == username or y == password:
    print("username and password correct")
    
else:
    print("username doesn't exist")