

def factorial(n):
    if n<0:
        print("Can't calculate factorial for negative number")
    elif n==0:
        return 1
    else:
        result = 1
        for i in range(1,n+1):
            result *=i
        return result
num = 6
print(f"Factorial of num is",factorial(num))            