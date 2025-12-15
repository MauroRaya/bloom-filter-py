import unittest
from BloomFilterReturn import BloomFilterReturn
from BloomFilter import BloomFilter

class TestBloomFilter(unittest.TestCase):
    def setUp(self):
        self.bloom_filter = BloomFilter()

    def test_insert_10_contains_10_probably_yes(self):
        self.bloom_filter.insert(10)
        result = self.bloom_filter.contains(10)
        self.assertEqual(result, BloomFilterReturn.PROBABLY_YES)

    def test_insert_10_contains_9_definitely_no(self):
        self.bloom_filter.insert(10)
        result = self.bloom_filter.contains(9)
        self.assertEqual(result, BloomFilterReturn.DEFINITELY_NO)

    def test_insert_10_contains_0_probably_yes(self):
        self.bloom_filter.insert(10)
        result = self.bloom_filter.contains(0)
        self.assertEqual(result, BloomFilterReturn.PROBABLY_YES)
