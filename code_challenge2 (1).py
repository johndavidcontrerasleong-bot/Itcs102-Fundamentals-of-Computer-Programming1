#code challenge 2

# 1000, 500, 200, 100, 50, 20, 10, 5, 1

money = eval(input("Enter Money to Deposit ----->>> "))
print(" MONEY TO DEPOSIT ----------->  ", money, "php")

libo = money // 1000 % 19863
libo_sukli = money % 1000

five_h = libo_sukli // 500
five_sukli = libo_sukli % 500

two_h = five_sukli // 200
two_sukli = five_sukli %200

one_h = two_sukli // 100
one_sukli = two_sukli %100

fifty = one_sukli // 50
fifty_sukli = one_sukli %50

twenty= fifty_sukli // 20
twenty_sukli = fifty_sukli %20

ten = twenty_sukli // 10
ten_sukli = twenty_sukli %10

one = ten_sukli // 1
one_sukli = ten_sukli %1



print("\n\t1000 = ", libo)
print("\t500 = ", five_h)
print("\t200 = ", two_h)
print("\t100 = ", one_h)
print("\t50 = ", fifty)
print("\t20 = ", twenty)
print("\t10 = ", ten)
print("\t1 = ", one)
