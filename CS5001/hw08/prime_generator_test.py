from prime_generator import PrimeGenerator


def test_primes_to_max():
        primes_list = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29,
                       31, 37, 41, 43, 47]
        pg = PrimeGenerator()
        generated_list = pg.primes_to_max(50)
        assert all(elem in primes_list for elem in generated_list)
