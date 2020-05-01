

revenue = float(input("What is your Company revenue?\n"))
costs = float(input("What is your Company costs?\n"))
difference = revenue - costs
if difference>0:
    print(f"You have a profit {difference}")
    employee = int(input("How many employee do you have?\n"))
    print("Yor profit per one employee is {:.2f}".format(difference/employee))
else:
    print(f"You have a loses = {-difference}")

