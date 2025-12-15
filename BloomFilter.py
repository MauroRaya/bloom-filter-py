from BloomFilterReturn import BloomFilterReturn

class BloomFilter():
    def __init__(self):
        self.bitset = [0 for _ in range(10)]
        self.hash_functions = [
            lambda x : x % len(self.bitset),
            lambda x : (2 * x) % len(self.bitset),
            lambda x : (x * x) % len(self.bitset),
        ]

    def insert(self, value: int):
        for hash_function in self.hash_functions:
            index = hash_function(value)
            self.bitset[index] = 1

    def contains(self, value: int) -> BloomFilterReturn:
        for hash_function in self.hash_functions:
            index = hash_function(value)

            if self.bitset[index] == 0:
                return BloomFilterReturn.DEFINITELY_NO

        return BloomFilterReturn.PROBABLY_YES
