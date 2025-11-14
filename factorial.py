def recursive_factorial(num):
    if num == 0 or num ==1 :
        return 1
    else: 
        return num * recursive_factorial(num -1)

def looping_factorial(num):
    if num == 0 or num ==1:
        return 1
    else:
        fact = 1
        for i in range(1, num + 1):
            fact *= i
        return fact
        

factorialNum = int(input("Enter the number to find factorial: "))
print (f"Factorial of {factorialNum} is using recursion: {recursive_factorial(factorialNum)}")
print (f"Factorial of {factorialNum} is using loop: {looping_factorial(factorialNum)}")
