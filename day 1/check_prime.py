# prime number or not

def check_prime(num):
    if num <= 1:
        return False
    for i in range(2, num):
        if num % i == 0:
            return False
    return True


num = int(input("enter number: "))

if check_prime(num):
     print(f"{num} is a prime number.")
else:
    print(f"{num} is not a prime number.")