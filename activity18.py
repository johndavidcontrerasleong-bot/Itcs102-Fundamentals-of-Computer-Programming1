is_active  = True

while is_active == True:
    ask = input("Do you want to continue --> ")

    if ask.lower() == "Yes":
        print("You chose to continue...")
        continue
    else:
        print("You chose to STOP")
        break