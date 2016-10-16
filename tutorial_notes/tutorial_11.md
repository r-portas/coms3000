# Tutorial 11: RSA

## Q1

```
Alice sends Bob: 3^4 mod 29 = 23
Bob sends Alice: 3^7 mod 29 = 12
Alice computes:  12^4 mod 29 = 1
Bob computes:    23^7 mod 29 = 1
Alice and Bob share the secret key (1)
```

## Q2

Trudy could act as a proxy for Alice and Bob, so Alice would exchanges keys with Trudy, thinking it was Bob. Bob would also exchange keys with Trudy, thinking it was Alice.

When Trudy recieves a message from Alice, she just decrypts it, reads it, encrypts it again and sends it to Bob. This also works the other way.

Diffie Hellman does not provide authentication

## Q3

```
p = 11
q = 3

n = p * q
  = 11 * 3
  = 33

Calculate Euler's Totient function
z = (p-1) * (q-1)
  = 10 * 2
  = 20

Choose e such that gcd(e, z) = 1
gcd(1337, 20) = 1
e = 1337

```

## Q4

### a

```
p = 7
q = 11
n = p * q = 77
z = (p-1)(q-1) = 60
e = 7

e * d * mod z = 1
d * 7 * mod 60 = 1

Do trial and error...
43 * 7 * mod 60 = 1

d = 43
```

### b

```
c = m^e mod n
c = m^7 mod 77

39 = 18(R)^7 mod 77
68 = 19(S)^7 mod 77
1  = 1(A)^7 mod 77
```

## Q5

Digital signatures with RSA involve using your private key to create a signature, the message and signature are sent together.

The reciever uses the public key on the signature to verify if its from the intended sender.


## Q6

Factoring number is hard to do via brute force, since p and q is not known to the attacker, they would have to brute force a solution, which is extremely difficult when large prime numbers are used.

## Q7

Generally the message should be hashed first, because RSA encryption and decryption is slow, then the hash of the message should be encrypted with the private key and sent with the message.

This is because hashes are significantly smaller in size then the original message.

When verifying the signature, the public key will be used to decrypt the hash and check against the computed hash. If the hashes match, the message is verified from the owner.

The hash also provides integrity, as if the message is changed the hash will not match the message. Thus when the receiver hashes the message to check against the hash, it will not match.
