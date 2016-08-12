# Tutorial 4: Hash functions, Authentication protocols and Biometrics

## Question 1

The challenge is reused, so a attacker could intercept the challenge response from the server and store it. When Alice transmits the hash of her passsword, the attacker can intercept and store that against the given challenge. If Alive logs into the server once again, the attacker can lookup the challenge and response with the stored hash and the attacker can do a replay attack.

## Question 2

The first 4 bytes are `E807`. Changing one bit of the input drastically changes the output of the hash, with all four bits different.

The MD5 fits the random oracle model, based off these two facts:
1. Hashing the same input twice yields the same hash
2. Similar but not identical input files most likely result in a completely different hash

## Question 3

The nature of a hashing algorithm makes it hard to find a specific value, as there is no way to move 'closer' to the desired outcome. MD5 is called a one way hash for this reason.

However we can brute force it with a quick python script:

```python
import hashlib

desired = "0111"

def hash(inp):
    global desired
    m = hashlib.md5(str.encode(inp)).hexdigest()[0:4]
    if m == desired:
        print("md5(" + inp + ") = " + desired)
        exit()

def main():
    i = 0
    while True:
        if (i % 1000) == 0:
            print("Hashed " + str(i) + " values")
        hash(str(i))
        i += 1

main()
```

Running this yields:
```bash
$ python3 md5_hash.py
Hashed 0 values
Hashed 1000 values
Hashed 2000 values
Hashed 3000 values
Hashed 4000 values
Hashed 5000 values
Hashed 6000 values
Hashed 7000 values
Hashed 8000 values
Hashed 9000 values
Hashed 10000 values
Hashed 11000 values
Hashed 12000 values
Hashed 13000 values
Hashed 14000 values
Hashed 15000 values
Hashed 16000 values
Hashed 17000 values
Hashed 18000 values
Hashed 19000 values
Hashed 20000 values
Hashed 21000 values
Hashed 22000 values
Hashed 23000 values
Hashed 24000 values
Hashed 25000 values
Hashed 26000 values
Hashed 27000 values
Hashed 28000 values
Hashed 29000 values

md5(29504) = 0111
```

It took 29504 guesses to find a matching hash

## Question 4


