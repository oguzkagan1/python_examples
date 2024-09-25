"""Calculate the number of steps required to reach 1 following the Collatz Conjecture."""

def steps(n):
    count = 0
    if n > 0:
        while n != 1:
            if n % 2 == 0:
                n //= 2
            else:
                n = 3 * n + 1
            count += 1
    else:
        raise ValueError("Only positive integers are allowed")
    return count

n = int(input("Enter the Number: "))
print(steps(n))
