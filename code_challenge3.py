name = input("Enter name: ")
weight = float(input("Enter package weight in pounds: "))
distance = float(input("Enter distance in km: "))
fragile = input("Is the package fragile? ")
is_express = input("Is the package express? ")
is_international = input("Is the package international? ")

Base_cost = (weight * 2.5) + (distance * 0.15)
if is_express == "no" and is_international == "no" and weight <= 2 and distance <= 100: 
 print("Free Shipping")
elif is_express == "yes" and is_international == "yes" : 
 Total_cost = (Base_cost * 1.4) + 50
 print("Express and International Shipping Cost: ", Total_cost)
elif is_express == "yes"  or is_international == "yes" and weight > 20 : 
 Total_cost = (Base_cost * 1.2) + 25
 print("Express or Heavy International Shipping Cost : ", Total_cost)
elif weight > 30 or distance > 1000:
 Total_cost = (Base_cost) + 30
 print("Heavy or Long Distance Shipping Cost: ", Total_cost)
else:  
 print("Shipping Cost: ", Base_cost)