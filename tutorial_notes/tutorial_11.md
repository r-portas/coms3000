# Tutorial 11: RSA

## Q1

### Question

The Diffie-Hellman Key exchange protocol relies on the fact that it is easy to do
modular exponentiation, but it is hard to do the inverse, i.e. to compute the “Discrete
Logarithm.”
Let’s assume Alice and Bob want to establish a shared secret key using the Diffie-Hellman
protocol.
They agree on a value n = p = 29 (prime number) and a generator a = g = 3. (The fact that
gcd(3,p-1=28)=1 guarantees that 3 is a generator.)
These values do not have to be secret and can remain constant over a long period of time.
According to the protocol, Alice chooses a random number x (modulo 29), let’s say x = 4.
Bob also chooses a random number y = 7.
Execute step by step the Diffie-Hellman protocol and calculate the shared secret key.
What can you say about the security of this protocol?

### Answer

```
Alice sends Bob: 3^4 mod 29 = 23
Bob sends Alice: 3^7 mod 29 = 12
Alice computes:  12^4 mod 29 = 1
Bob computes:    23^7 mod 29 = 1
Alice and Bob share the secret key (1)
```

Security is heavily dependant on the difficulty of computing discrete logarithms for finding the secret x and y

## Q2

_Describe how Trudy could use a Man-in-the-middle-attack to attack the Diffie-Hellman session establishment protocol between Alice and Bob._

Trudy could act as a proxy for Alice and Bob, so Alice would exchanges keys with Trudy, thinking it was Bob. Bob would also exchange keys with Trudy, thinking it was Alice.

When Trudy recieves a message from Alice, she just decrypts it, reads it, encrypts it again and sends it to Bob. This also works the other way.

Diffie Hellman does not provide authentication

## Q3

_Consider an RSA system with p=11 and q=3. Find the parameters n and z and also find a valid parameter e._

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

Consider an RSA system with the following parameters:
```
p=7, q=11
n = p * q = 77
z = (p-1)(q-1) = 6 * 10 = 60
e=7
```

### a) Find the secret key d.

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

### b) Use this system to encrypt the following message: “RSA”

```
c = m^e mod n
c = m^7 mod 77

39 = 18(R)^7 mod 77
68 = 19(S)^7 mod 77
1  = 1(A)^7 mod 77

{39, 68, 1}
```

## Q5) Explain how RSA can be used for digital signatures.

Digital signatures with RSA involve using your private key to create a signature, the message and signature are sent together.

The reciever uses the public key on the signature to verify if its from the intended sender.


## Q6) Explain why in a real RSA system an attacker cannot find the secret key d.

Factoring number is hard to do via brute force, since p and q is not known to the attacker, they would have to brute force a solution, which is extremely difficult when large prime numbers are used.

## Q7

### Question

Encrypting or signing large files with RSA is computationally very expensive due to
the large number of modular exponentiations with very large integers that are involved.
Explain how cryptographic one-way hash functions can be used to increase the efficiency
of digital signatures using RSA.
Explain why this mechanism also provides integrity.

### Answer

Generally the message should be hashed first, because RSA encryption and decryption is slow, then the hash of the message should be encrypted with the private key and sent with the message.

This is because hashes are significantly smaller in size then the original message.

When verifying the signature, the public key will be used to decrypt the hash and check against the computed hash. If the hashes match, the message is verified from the owner.

The hash also provides integrity, as if the message is changed the hash will not match the message. Thus when the receiver hashes the message to check against the hash, it will not match.
