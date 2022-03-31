def print_prime_numbers():
    maximum_range = 1000
    primes = []

    for num in range(1, maximum_range + 1):
        for j in range(2, int(num ** 0.5) + 1):
            if num % j == 0:
                break
        else:
            primes.append(num)

    return primes


if __name__ == "__main__":
    print(print_prime_numbers())
