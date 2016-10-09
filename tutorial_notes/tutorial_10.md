# Tutorial 10: Vigenere Ciphers, Modular Arithmetic

## Q1

Using a online tool to guess the key length yields 7 with a probability of around 13%.

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

```
a1 = 5 mod 7 = 5
a2 = 25 mod 7 = 4
a3 = 125 mod 7 = 6
a4 = 625 mod 7 = 2
a5 = 3125 mod 7 = 3
a6 = 78125 mod 7 = 5
```

b)

`log5(4) mod 7 = 2`
`log5(6) mod 7 = 3`
