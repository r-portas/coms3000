# Tutorial 5: Biometrics and Access Control

## Question 1

- __False Accept__

An attacker successfully authenticates as somebody else and is granted access to the system.

- __False Reject__

A valid user is rejected by the system

## Question 2

- __Hair Colour__
    - Universality

    Low: Some people don't have hair

    - Distinctiveness

    Low: Many people share the same hair colour

    - Permanence

    Medium: People can change their hair colour

    - Performance

    High: Its easy for a company to detect a colour

    - Acceptability

    High: Not invasive

    - Circumvention

    Low: Its easy to fake a hair colour

- __Fingerprint__

    - Universality

    High: Everyone has a fingerprint

    - Distictiveness

    High: Fingerprint are unique

    - Permanence

    Medium: Fingerprints can be damaged with cuts, etc.

    - Acceptability

    High: Easy to do and non invasive

    - Circumvention

    High: Hard to fake a fingerprint

## Question 3

![block diagram](resources/tut_5_block_diagram.png "Block Diagram")

Two potential replay attacks are:

1. Stealing the user's biometrics (Fingerprint, etc) and using it to authenticate with the server as usual

2. Setting up a fake server, intercepting a valid transaction then setting up a fake server to mirror the responses.

## Question 4

a) Identification has the highest false match rate, this is because the device is searching through a database to find the highest match against many different users. Whereas verification is checking against a single user, thus less chance of a false match.

b) 

```
P1: Probability of a False Match in verification mode
PN: Probability of a False Match in identification mode

PN = Probability of a single false match * number of matches
PN = P1 * N
```

## Question 5

a) 

```
FMR: a * 0.5 = 0.125
FNMR: b * 0.5 = 0.25

a: 1/(6 - 2) = 0.25
b: 1/(7 - 5) = 0.5
```

b) The t value will need to be closer to 5 to achieve a smaller FNMR. However this will increase the FMR.

Thus the exact answer will be:

```
0.025 = b * t
0.025 = 0.5 * t
0.05 = t
act = 5 + t
act = 5.05

FMR: 0.2375
```

c) Equal error rate

```
(6 - t) * 0.25 = (t - 5) * 0.5
= 5.33
```
