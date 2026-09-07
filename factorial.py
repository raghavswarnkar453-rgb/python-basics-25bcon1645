# Input: Get integer from the user
num = int(input("Enter a number: "))

factorial = 1

# Check if the number is negative, zero, or positive
if num < 0:
    print("Factorial is not defined for negative numbers.")
elif num == 0:
    print("The factorial of 0 is 1.")
else:
    # Loop from 1 to num (inclusive)
    for i in range(1, num + 1):
        factorial *= i
    print(f"The factorial of {num} is {factorial}")
