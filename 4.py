def is_prime(number):
    if number <= 1:
        return False
    for i in range(2, int(number ** 0.5) + 1):
        if number % i == 0:
            return False
    return True

favorite_number = int(input("Enter your favorite number: "))
if is_prime(favorite_number):
    print(f"{favorite_number} is prime number.")
else:
    print(f"{favorite_number} is not prime number.")