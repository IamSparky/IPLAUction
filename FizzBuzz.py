'''FizzBuzz HACKERRANK CODING CHALLENGE'''
def fizzbuzz1(x):
    if x % 3 == 0 and x % 5 == 0:
        return "FizzBuzz"
    elif x % 3 == 0:
        if x % 5 != 0:
            return "Fizz"
    elif x % 5 == 0:
        if x % 3 != 0:
            return "Buzz"
    else:
        return x


def fizzBuzz(n):
    # Write your code here
    for i in range(1, n + 1):
        print(fizzbuzz1(i))


if __name__ == '__main__':
    n = int(input('Enter your no.'))
    fizzBuzz(n)