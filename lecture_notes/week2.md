# Week 2: Authentication

## Trust and Trustworthiness

- __Trust__: Confidence, strong belief, in the goodness, strength reliability of something or somebody
- We can trust somebody or something if it/he/she behaves as expected

- Bob's boss trusts him to handle large amounts of company money, _Bob is trusted_.
- If Bob embezzles the money, he is still trusted by his boss, but he is definitely _not trustworthly_.

## Direct and Indirect Trust
- Trust can be based on direct experience
    - Bob has conducted business with Alice for several years, therefore he trusts her.
    - What is Alice and Bob want to do business but have never met or communicated before? How can they establish a level of trust?
        - Via indirect experience or recommendation
        - Trent tells Bob that Alice is trustworthy. If Bob trusts Trent, this trust is transferable to Alice. (Trent acts as a so-called __Trusted Third Party__)

## Information Security
- Information Security is about protecting information assets
- Information assets need to be protected to provide (5 aspects of Information Security)
    - __Confidentiality__
    - __Integrity__
    - __Availability__
    - Authenticity (Integrity of provenance)
    - Non-repudiation (Integrity of action/timeline)

## Access Control
- Lack of Access control can lead to __Confidentiality__, __Integrity__ and __Availability__ (CIA) being compromised
- We need to control who can read, write and modify data.

- Access control is typically based on __Identity__
- Two separate functions:
    - Establish Identity (Identification and Authentication)
        - __Identification__: Determine Identity
        - __Authentication__: Verify Identity
    - Authorisation
        - Once the identity of a person is known, a decision can be made about granting or denying access

## Authentication
- "The processing of verifying a claimed identity"
    - Authentication provides proof of identity
- Methods of providing proof
    - Something you __know__:
        - Pins, password
    - Something you __have__:
        - Token, smart card
    - Something you are __are (or do)__:
        - Fingerprints, voice

## Passwords
- Most common method for Authentication
- Problems with passwords:
    - Users forget passwords
    - Users choose same password for multiple systems
    - Users choose weak or guessable passwords

## Attacks Against Passwords
- Password Guessing
    - Brute force (offline, online)
- Social Engineering
- Eavesdropping
- Shoulder surfing
- Fake Interface
- Keyloggers
- Attacks by Audit Trails
- Attacks against Password Storage

## One Way Hash Functions
- Also known as __digest functions__ and __digital fingerprints__
- __Collision Resistance__: It is computationally infeasible to find any two distinct inputs that hash to the same value
    - __Strong Collision Resistance__: It is computationally infeasible to find any two distinct values that hash to the same output
    - __Weak Collision Resistance__: It is computationally infeasible given a hash, to find a value that hashes to the given hash
- __One Way Property (Pre Image Resistance)__: It is computationally infeasible to find the original text from a hashed message

## Random Oracle Model
A __random oracle__ is a black box that responds to every _unique query_ with a truly random response chosen uniformly from its output domain. If a query is repeated it responds the same way every time the query is submitted.

## Pre Image Attack (Weak Collision Resistance)
- 'Work factor' to find a pre-image, for a n-bit function (random oracle model)
- On average, we can expect to find a pre-image after trying `2^n` different inputs (Work Factor)

## Collision Attack (Strong Collision Resistance)
- Find a collision between any two inputs
- Much easier that pre image attack
- Work factor: `2^(n/2)`
