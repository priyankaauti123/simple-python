


def check_prime(no):
    for i in range(2,no//2):
        if no%i==0:
            return 0
    return 1

def print_prime(no1,no2):
    for i in range(no1,no2):
        if check_prime(i)==1:
            print i


print_prime(input(),input())


