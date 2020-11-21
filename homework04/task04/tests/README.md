# How to use doctests

1. Install Python 3.8 (https://www.python.org/downloads/)
2. Clone the repository https://github.com/kiayria/epam-python-hw
3. Open terminal and change directory \
`cd /path/to/repo/epam-python-hw/homework04/task04/fizzbuzz` \
Run: \
`python3 -m doctest -v fizzbuzz.py` \
To run with pytest: \
`cd /path/to/repo/epam-python-hw/homework04/task04/` \
`pytest --doctest-modules tests/test_fizz_buzz.py fizzbuzz/fizzbuzz.py`