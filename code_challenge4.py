import getpass

username = input("Enter your username: ")
password = getpass.getpass("Enter your password: ")
if username == "user" and password == "pogi321":
 print("Access granted.")
else:
 print("Access denied. Invalid username or password.")
 exit()

age = int(input("Enter Age: "))
is_employed = bool(input("Are you Currently Employed? "))
credit_score = eval(input("Credit Score History: "))
annual_income = eval(input("How much is your annual income? "))
has_collateral = bool(input("Do you have a collateral? "))
amount_to_loan = float(input("Enter amount to loan: "))

if age >= 21 and is_employed == True:
    print("Passed baseline eligibility")
    if credit_score >= 750:
        if annual_income >= 100000:
           base_rate = 4.5 // amount_to_loan
           print("Final interest rate is : 4.5%", base_rate)
        else:        
            base_rate = 5.0 // amount_to_loan
            print("Final interest rate is : 5.0%", base_rate)
    elif credit_score >= 600 and credit_score <= 749:
        if has_collateral == True:
            base_rate = 7.0 // amount_to_loan
            print("Final interest rate is : 7.0%", base_rate)
        elif annual_income < 40000:
            base_rate = 9.5 // amount_to_loan
            print("Final interest is : 9.5%", base_rate)S
        else: 
            base_rate = 8.0 // amount_to_loan
            print("Final interest is : 8.0%", base_rate)
    elif credit_score < 600:
        print("Too low credit")
    else:
        print ("Pwede na")
        
