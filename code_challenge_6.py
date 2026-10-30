size = int(input("Enter Size --->"))

for x in range(0, size):
  for y in range(0, size):
    if x+y == size-1 or x == y:
      print("*", end = " ")
    else:
      print(" ", end = " ")
  print()