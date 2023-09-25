import hashlib
import random
import statistics
from typing import Set

BINARY_LENGTH = 130


def generate_string_set(min_number: int, max_number: str) -> set:
    """Create a set of strings based on range(min_number, max_number)"""
    # TODO: Using random values to test comvergence
    return {str(x + random.randint(0, 100000)) for x in range(min_number, max_number)}


def binary_hash(string_value: str):
    """create binary reporesention for hash of string_value"""
    hashcode=hashlib.md5(string_value.encode(encoding = 'UTF-8')).hexdigest()
    return bin(int(hashcode,16))


def generate_binary_set(string_set: set) -> set:
    """Create set of binary hash representations of a set of strings""" 
    return {binary_hash(s) for s in string_set}


def leading_zeros(binary_set: set):
    return [BINARY_LENGTH - len(b) for b in binary_set]


def estimate_cardinality(leading_zeros: list):
    max_zeros = max([zeros for zeros in leading_zeros])
    return 2**max_zeros


def estimate_mean_cardinality(string_set_size: int, n: int):
    estimates = [estimate_cardinality(leading_zeros(generate_binary_set(generate_string_set(0, string_set_size )))) for index in range(n)]
    return statistics.mean(estimates)
