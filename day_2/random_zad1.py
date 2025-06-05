import random

# operacje na liczbach (pseudo)losowych

# """Return random integer in range [a, b], including both end points."""
print(random.randint(1, 100)) # int  od 1 do 100

print(random.randrange(1, 100)) # int od 1 do 99
print(random.randrange(5)) # int od 0 do 4

print(random.random()) # float 0.10920553978758085, od 0 do 0.99999999
print(random.random() * 8) # float 6.881740583579205, od 0 do 7.99999999