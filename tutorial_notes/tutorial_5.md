# Tutorial 5: Biometrics and Access Control

## Q1: Explain what a false accept and false reject is

- __False Accept__

An attacker successfully authenticates as somebody else and is granted access to the system.

- __False Reject__

A valid user is rejected by the system

## Q2: Compare Biometrics

- __Hair Colour__
    - Universality

    Low: Some people don't have hair

    - Distinctiveness

    Low: Many people share the same hair colour

    - Permanence

    Low: People can change their hair colour

    - Performance

    High: Its easy for a company to detect a colour

    - Acceptability

    High: Not invasive

    - Circumvention

    High: Its easy to fake a hair colour

- __Fingerprint__

    - Universality

    Medium: Everyone has a fingerprint

    - Distictiveness

    High: Fingerprint are unique

    - Permanence

    Medium: Fingerprints can be damaged with cuts, etc.

    - Performance
    
    High: Fast and accurate

    - Acceptability

    High: Easy to do and non invasive

    - Circumvention

    Medium: Hard to fake a fingerprint

## Q3: Biometric Attacks

![block diagram](resources/tut_5_block_diagram.png "Block Diagram")

Two potential replay attacks are:

1. Stealing the user's biometrics (Fingerprint, etc) and using it to authenticate with the server as usual

2. Setting up a fake server, intercepting a valid transaction then setting up a fake server to mirror the responses.

## Q4: A biometric device can be used in identification mode or verification mode. In which situation will we have a higher False Match Rate?

### a) Explain your answer using an intuitive argument.

Identification has the highest false match rate, this is because the device is searching through a database to find the highest match against many different users. Whereas verification is checking against a single user, thus less chance of a false match.

### b)
Use a simple mathematical argument. For this you can make the following assumptions: 

We can model both identification and verification as random processes. Let P 1 be the probability of a False Match (false accept) in a verification trial, where we have a 1-to-1 
match problem. We now want to find PN, the probability of a False Match in an 
identification trial, searching through a database of size N. The identification process (1-to-N match) can be modeled as N independent verification processes (1-to-
1 matches)

```
P1: Probability of a False Match in verification mode
PN: Probability of a False Match in identification mode

PN = Probability of a single false match * number of matches
PN = P1 * N
```

## Question 5

![PDF Function](resources/t5_pdf.jpg)
\ 

### a) For a threshold of t = 5.5, what are the parameters FAR (FMR) and FRR (FNMR)?

```
FMR: a * 0.5 = 0.125
FNMR: b * 0.5 = 0.25

a: 1/(6 - 2) = 0.25
b: 1/(7 - 5) = 0.5
```

### b) You are asked to adjust the system so that FNMR=2.5%. Where do you need to set the threshold t to achieve this? What is the resulting FMR?

The t value will need to be closer to 5 to achieve a smaller FNMR. However this will increase the FMR.

Thus the exact answer will be:

```
0.025 = b * t
0.025 = 0.5 * t
0.05 = t
act = 5 + t
act = 5.05

FMR: 0.2375
```

### c) What is the Equal error rate?

```
(6 - t) * 0.25 = (t - 5) * 0.5
= 5.33
```
