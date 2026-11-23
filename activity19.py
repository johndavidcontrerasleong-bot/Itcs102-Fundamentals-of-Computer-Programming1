import getpass
attempts = 0
username = "David"
password = "Smogath32"

while True:
    user = input("Enter Your Username: ---> ")
    pas = input("Enter Your Password: ---> ")

    if user == username and pas == password:
        print("Successfull Log In")
        print("Login Attempts: ", attempts)
        break
    else:
        print('Failed to log in')
        attempts = attempts + 1