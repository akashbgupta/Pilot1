
def primecheker(number):
    is_prime = True
    for i in range(2, number):
        if number % i == 0:
            is_prime = False
            break
    if is_prime:
        print("It is a Prime number")
    else:
        print("Fuck you")

n = int(input())
primecheker(number=n)


