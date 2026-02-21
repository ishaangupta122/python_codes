# Method 1: Euclidean Algorithm
def gcd_euclidean(a, b):
    while b != 0:
        a, b = b, a % b
    return a


# Method 2: Naive approach
def gcd_naive(a, b):
    gcd = 1
    # Start from the smaller number and go downwards
    for i in range(min(a, b), 0, -1):
        if a % i == 0 and b % i == 0:
            gcd = i
            break
    return gcd


# Example usage
num1 = 48
num2 = 18

print("GCD using Euclidean Algorithm:", gcd_euclidean(num1, num2))
print("GCD using naive method:", gcd_naive(num1, num2))
 
print(48 % 3)