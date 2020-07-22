"""Every twin prime pair except (3, 5) is of the form (6n – 1, 6n + 1) for some natural number n; that is,
  the number between the two primes is a multiple of 6.

  we will be using Wilsons method to identify a prime no.
"""

# welcome to the world of Primes - the Prime twins

def factorial(num):
    num_fact = 1
    for i in range(num):
        num_fact = num_fact * (i + 1)
    return num_fact


def wilson_check(p):
    """Wilson’s theorem states that a natural number p > 1 is a prime number if and only if
        (p - 1) ! ≡  -1   mod p
    OR  (p - 1) ! ≡  (p-1) mod p
    """
    if factorial(p - 1) % p == p - 1:
        return True
    else:
        return False


twins = []
dd = int(input("Enter no. of decimal digits: "))  # dd = decimal digit

to = range(10 ** (dd - 1), 10 ** dd)  # to = tenth order(b/w)

if dd == 1:
    twins.append((3, 5))
    twins.append((5, 7))
else:
    for num in to:
        if num % 6 == 0 and wilson_check(num - 1) and wilson_check(num + 1):
            twins.append((num - 1, num + 1))

# print(twins)

#if you pull this code and run just change "Shashank Gupta"

file = open(r"C:\Users\Shashank Gupta\Documents\git_test\myFirstFile", "w+")
# file.write(twins)

for pair in twins:
    file.write(str(pair) + "\n")

file.close()

# please uncomment this code in order to read file

# file = open(r"C:\Users\Shashank Gupta\Documents\git_test\myFirstFile", "r")
# print(file.readlines())

# file.close()
