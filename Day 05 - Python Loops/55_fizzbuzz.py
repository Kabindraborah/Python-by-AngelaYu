#from 1 to 100 if there is a no divisible by - 3 it should print fizz, 5 it should print buzz, 3x5 it should print fizzbuzz

for number in range(1,101):
    if number % 3 == 0 and number % 5 ==0:
        print("FizzBuzz")
    elif number % 3 == 0:
        print("Fizz")
    elif number % 5 == 0:
            print("Buzz")
    else:
        print(number)