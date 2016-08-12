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

desired = "7"

def hash(inp):
    global desired
    m = hashlib.md5(str.encode(inp)).hexdigest()[0]
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

md5(17) = 7
```

It took 17 guesses to find a matching hash.

Since the output size is 4 bits, the probablity is 0.5^4, or 1/16. So it is estimated to take 16 attempts to find a solution

## Question 4

Using the same program from above, but attempting to find 'e' yields:

```bash
$ python3 md5_hash.py

md5(3) = e
```

It took three guesses to find the outcome. The expected probability will be the same as the above answer, 1/16

## Question 5

Using the same function in Q3, but changing the input to append my student number yields:
```bash
$ python3 md5_hash.py

md5(43560846 0) = e
```

The program found a match with the first attempt

## Question 6

Question 5 should be easier to compute, since we are looking for any two strings that match.

Thus we can store a table of previously found hashes and compare against that, which is much easier than attempting to find a specific value such as in question 4.

## Question 7

Removing the secure authentication protocols will force the server to fall back to basic authenication, in which the password is transmitted in plain text which the attacker could easily intercept and get the plaintext password.

## Question 8

An attacker could set up a fake server and trick the user to authenticate with it. The fake server then collects the hashed password. The attacker can then authentice with the real server using the collected hashed password.
