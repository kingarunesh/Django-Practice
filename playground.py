import os

random_str = lambda: os.urandom(10).hex()

print(random_str())