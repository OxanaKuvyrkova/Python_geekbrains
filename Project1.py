
name = input("Hello, User, what is your name?\n")
age = int(input(f"Hi, {name}, How old are you?\n"))
question = input(f"{name}, don't you think we can be a friends?\n")
print(f"I've predicted your '{question}' answer\n")
friends = int(input(f"How many friends do you have in your {age} years old?\n"))
print(f"Well, now you can replace your number of friends with {friends + 1}, my congradulations!!!\n")