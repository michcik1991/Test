# I create generator to return next fibannaci value


def fib():
    a, b = 0, 1
    while 1:
        yield a
        a, b = b, a + b

# Function which check if number is prime or not - return True or False
def primary_number_check(n):
    if n > 1:
        for i in range(2, int(n**0.5)+1):
            if (n % i) == 0:
                return False
        else:
            return True
    return False

# My main function which return list of n first provided prime number from fibanacci sequence
def number_of_first_primary_numer_from_fib(n):
     if (type(n) == int):
         if n >= 0:
             number = fib()
             count = 0
             list_fiba = []
             while count < n:
                fib_number = next(number)
                if primary_number_check(fib_number):
                    list_fiba.append(fib_number)
                    count +=1
             return list_fiba
         else:
             raise Exception("The number is lower than 0. Please provided number grather than 0")
     else:
         raise Exception("The number is not integer")

