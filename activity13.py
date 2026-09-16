age = int(input("Enter Age: "))
is_employed = bool(input("Are you Currently Employed? "))
credit_score = eval(input("Credit Score History: "))
annual_income = eval(input("How much is your annual income? "))
has_collateral = bool(input("Do you have a collateral? "))

if age >= 21 and is_employed == True:
    print("Passed baseline eligibility")
    if credit_score >= 750:
        if annual_income >= 100000:
           print("Final interest rate is : 4.5%")
        else:        
            base_rate = 5.0
            print("Final interest rate is : 5.0%")
    elif credit_score >= 600 and credit_score <= 749:
        if has_collateral == True:
            base_rate = 7.0
            print("Final interest rate is : 7.0%")
        elif annual_income < 40000:
            base_rate = 9.5
            print("Final interest is : 9.5%")
        else: 
            base_rate = 8.0
            print("Final interest is : 8.0%")
    elif credit_score < 600:
        print("Too low credit")
    else:
        print ("Pwede na")
        