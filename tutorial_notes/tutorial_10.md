# Tutorial 10: Vigenere Ciphers, Modular Arithmetic

## Q1

To guess the keylength of the cipher, we can shift across the cipher text and see how many characters line up. The number of times we shift will be the keylength

```
# Guess the key length of a vigenere cipher

ciphertext = "nianmgwssl eg ghbjmnavg lc ekwej ds rds irg ml pvv wkfja qfubiqlc egsre pc kko ocu tzqnmlc hyh zsqehzrx sd pvv fstfafkhhx jahkhb ml pvzv bsu wbu wril qgzqq xfa qfoeqlo zreop yo hyh zpyebkhhx"

def check_offset(str1, offset):
    matches = 0
    for i in range(len(str1) - offset):
        if str1[i] == str1[i + offset]:
            matches += 1
    return matches


for i in range(0, 40):
    matches = check_offset(ciphertext, i)
    print("Offset: {}, Matches: {}".format(i, matches))

```

The output of the program is:
```
Offset: 1, Matches: 7
Offset: 2, Matches: 7
Offset: 3, Matches: 12
Offset: 4, Matches: 22
Offset: 5, Matches: 11
Offset: 6, Matches: 8
Offset: 7, Matches: 12
Offset: 8, Matches: 14
Offset: 9, Matches: 15
Offset: 10, Matches: 10
Offset: 11, Matches: 9
Offset: 12, Matches: 7
Offset: 13, Matches: 11
Offset: 14, Matches: 6
...
```

From the output, we can guess that the keylength is 4, as it has the highest number of matches


## Q2: Prime Numbers

| Number   | Prime? |
| -------- | ------ |
| 7        | Yes    |
| 13       | Yes    |
| 19       | Yes    |
| 43       | Yes    |
| 32437685 | No     |

## Q3: Prime factors

`21: 3 * 7`
`24: 2 * 2 * 2 * 3`
`96: 2 * 2 * 2 * 2 * 2 * 3`

## Q4: Modulo Arithmetic

a) 5
b) 2
c) 1

## Q5: Modulo Arithmetic

a) 9
b) 4

## Q6

a)

It is a generator if `gcd(a, n-1) = 1`
Thus `gcd(5, 6) = 1`, therefore it is a generator

b)

`log5(4) mod 7 = 0.861`
`log5(6) mod 7 = 1.113`
