series = []
answer = input("Do you watch series? (yes/no) --> ").lower()

while True:
    if answer == "yes":
        title = input("What is the title of the series? --> ")
        series.append(title)
        ans = input("Is there anything else? (yes/no) --> ").lower()
    else:
        print(series)
        break