# Tutorial 3: Identification, Authenication, Cryptographic one-way hash functions

## Q1: What is the difference between identification and authenication
Identification is the process of presenting an identity to the system, done in the initial stages. Such as providing a username or giving your name.

Authentication is the process of validating that identity, such as checking if a password is correct for a given username.

## Q2: What are the key properties of a one way hash function
- Cannot find the original message from the hash (Pre-image)
- Quick to compute any message and compresses the message to a fixed length output
- A small change in the message should yield a large difference in the hash output, so an attacker cannot determine if two messages are similar
- Its unfeasible to find two different messages that hash to the same value (Collision resistance)

## Q3a: Evaluate this function against the key properties of a one way hashing function

If a single character is changed in the input, the hash will be the same. Thus the function does not create unique hashes for different messages, thus the collision resistance property is not held. In addition similar messages (strings of the same length, with one characters being different) will be identical, which is also not ideal.

The pre-image property will be held as it is nearly impossible to guess the original message.

## Q3b: What's the probability of  a collision in h() for two chosen inputs x1 and x2

The probability of a collision occurring is 1/2, as the output hash only has two states (all 0s or all 1s). Thus any message must hash to one of the two.

## Q3c: Whats the probability of a collision between two randomly chosen inputs x1 and x2 for an ideal one way hash function with 32 bit output

The probability is (1/2)^n, thus (1/2)^32
