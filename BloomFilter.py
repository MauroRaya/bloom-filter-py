from BloomFilterReturn import BloomFilterReturn
from typing import Callable

class BloomFilter():
    def __init__(
        self,
        bitset_length: int,
        hash_functions: list[Callable[[int], int]]
    ):
        self.bitset = [0] * bitset_length
        self.hash_functions = hash_functions

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
