# Tutorial 8: Symmetric Cryptography

## Question 1

a) The encrypted message will be K XOR M1:

```
M1: 11011001
K:  01011000
------------
C1: 10000001
```

b) There is no way to find the original message with just the ciphertext. However if Eve does know the key or knows other messages encrypted with the same key, she could decrypt the message.

c)

Eve can XOR M1 and C1 to get the key (K) and use the key to decrypt M2

```
M1: 11011001
C1: 10000001
------------
K:  01011000
C2: 10111110
------------
M2: 11100110
```

Thus the message can be easily found.

## Question 2

```
Plaintext: TRANSPOSITION

TRAN
SPOS
ITIO
N

Encrypted: TSIN RPT AOI NSO
```
