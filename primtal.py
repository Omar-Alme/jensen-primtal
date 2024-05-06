def is_prime(n):
    """
    Check if a number is prime.

    a prime number is a natural number greater than 1 
    that is not a product of two smaller natural numbers.

    Args:
        n: An integer.

    Returns:
        A boolean value, True if the number is prime, False otherwise.
    """
    if n < 2:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True



def find_primes(n):
    """
    Find all prime numbers up to n.

    Args:
        n: An integer.

    Returns:
        A list of prime numbers.
    """
    primes = []
    for i in range(2, n+1):
        if is_prime(i):
            primes.append(i)
    return primes


def main():
    try:
        n = int(input("Enter a whole number: "))	
        if n < 2:
            print("The number must be greater than 1.")
        else:
            print(f"Prime numbers up to {n}:")
            prime_numbers = find_primes(n)
            for prime in prime_numbers:
                print(prime, end=" ")
    except ValueError:
        print("You must enter a whole number.")

if __name__ == "__main__":
    main()


