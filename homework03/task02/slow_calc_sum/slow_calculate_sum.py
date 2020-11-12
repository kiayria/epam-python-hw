"""
Calculate total sum of slow_calculate() of all numbers starting from 0 to 500.
Calculation time should not take more than a minute. Use functional capabilities
of multiprocessing module. You are not allowed to modify slow_calculate function.
"""
import hashlib
import random
import struct
import time
from multiprocessing import Pool
from multiprocessing.dummy import Pool as ThreadPool


def slow_calculate(value):
    """Some weird voodoo magic calculations"""
    time.sleep(random.randint(1, 3))
    data = hashlib.md5(str(value).encode()).digest()
    return sum(struct.unpack("<" + "B" * len(data), data))


pool = ThreadPool(25)
start = time.time()
nums = pool.map(slow_calculate, range(0, 501))
res = sum(nums)
time_total = time.time() - start
print(res, time_total)
