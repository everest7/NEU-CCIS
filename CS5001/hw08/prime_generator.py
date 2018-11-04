class PrimeGenerator():
    def __init__(self):
        pass

    def primes_to_max(self, max):
        """Generate a list of primes under the limit: max

        Args:
            max: the limit of primes generated

        Returns:
            A list of primes
        """
        nonprimes = (max + 1) * [False]
        nonprimes[0] = nonprimes[1] = True
        res = []
        for i in range(2, max + 1):
            for j in range(2 * i, max + 1, i):
                nonprimes[j] = True
        for flag in range(2, max + 1):
            if not nonprimes[flag]:
                res.append(flag)
        return res
