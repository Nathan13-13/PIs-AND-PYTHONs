def collatz(n):
    # Creates a function called collatz that takes a number (n).
    if n == 1:
        return 0
    #This is the base case. When the number reaches 1, the function stops and returns 0.
    elif n % 2 == 0:
        return 1 + collatz(n // 2)
    # % 2 == 0 means the number is even.   // 2 divides the number by 2.    1 + counts the current step.
    else:
        return 1 + collatz(3 * n + 1)
    # Multiply it by 3.   Add 1.   Call the function again.   Add 1 to count the step.

print(collatz(42))


#If the Collatz Conjecture was false and a number never reached 1, the program would keep calling itself forever