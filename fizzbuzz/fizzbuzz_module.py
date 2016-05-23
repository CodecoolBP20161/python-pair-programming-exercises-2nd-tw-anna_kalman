def fizzbuzz(number):
    if number % 15 == 0:
        print ("FizzBuzz")
    elif number % 3 == 0:
        print ("fizz")
    elif number % 5 == 0:
        print ("buzz")
    else:
        print (number)
    return

def main():
    for i in range(1, 101):
        fizzbuzz(i)
    return

if __name__ == '__main__':
    main()
