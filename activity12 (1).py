name = input("Please input your name --->")
age = int(input("Please input your age --->"))

if age <=5 : 
    print("This age is considered as Infant")

elif age <= 18 :
    print("This age is considered as Minor")

elif age <= 20 :
    print("This age is considered as Teen")
    
elif age <=59:
    print("This age is considered as Adult")

elif age >=60:
    print("This age is considered as Senior")

else:
    print("age invalid")