number = int(input("Enter your number\n"))
start = number % 10
number_new = (number - start)/10
max_digit = start
while number_new>10:

    if start == 9:
        print(start)
        break
    next_digit = number_new%10
    number_new = (number_new - next_digit)/10

    if next_digit >= max_digit:
        max_digit = next_digit

    if number_new<10:
        if number_new > max_digit:
            print(int(number_new))
        else:
            print(int(max_digit))
        break