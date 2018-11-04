from prime_generator import PrimeGenerator


def main():
    max = int(input("Enter the limit: "))
    pg = PrimeGenerator()
    prime_list = pg.primes_to_max(max)
    print(prime_list)


main()
