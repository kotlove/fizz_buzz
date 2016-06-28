import sys
x = 1
if len(sys.argv) <= 1:
    while True:
        try:
            n = int(input("Enter a number: "))
            break
        except ValueError:
            print("Enter an integer please!")
else:
    try:
        n = int(sys.argv[1])
    except ValueError:
        while True:
            try:
                print("Enter an integer please!")
                n = int(input("Enter a number: "))
                break
            except ValueError:
                pass
counting = True
while counting:
    if x <= n:
        if x % 3 == 0 and x % 5 == 0:
            print("FizzBuzz")
        elif x % 3 == 0 and x % 5 != 0:
            print("Fizz")
        elif x % 3 != 0 and x % 5 == 0:
            print("Buzz")
        else:
            print(x)
        x += 1
    else:
        counting = False