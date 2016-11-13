# Tutorial 7: Information Theory and Symmetric Cryptography

## Q1: Consider a random variable with the following equally likely outcomes: A, B, C, D, E.

### a) What is the Entropy?

The entropy is log to base 2 of the number of possible outcomes. Thus in this case `log2(5) = 2.32`.

### b) Find an encoding scheme that uses the smallest possible number of bits per outcome.

The smallest encoding scheme would be 2.4 bits. Such as:

```
A: 11
B: 01
C: 10
D: 001
E: 000

{11, 01, 10, 001, 000}
```

## Q2

For a random variable X with two outcomes x1 and x2 with probabilities p1 and p2, we get maximum Entropy if p1 = p2. Can you prove this?

```
H(x) = -sum(p_i * log2 p_i)
h(x) = -p_1 log(p_1) - p_2 log(p_2)
h(p_1) = -p_1 log(p_1) - (1 - p_1) log(1 - p_1)
h'(p_1) = log(p_1) + log(p_1 - 1) = 0

p_2 = 1 - p_1 = 0.5
p_2 = 0.5
p_1 = 0.5
```

## Q3

Alice and Bob want to communicate via an insecure channel and decide to use a
secret key encryption algorithm with a 128 bit key. They decide on the following method to
determine their secret key: They toss a coin 16 times. If the result is ‘heads’ they write
down a ‘1’ if the result is ‘tails’, they write a ‘0’. Then, they compute the MD5 hash of this
16 bit number, which results in a 128 bit output.
What’s the entropy of their 128 bit secret key?

__There are `2^16` different possible outcomes from coin tosses. Thus the entropy will be `log2(2^16) = log2(65536) = 16`.__

## Q4

Encrypt the following text with a Caesar cipher with a key ‘E’, i.e. with a shift of 4, which means the letter A in the plaintext will be mapped to the letter E in the ciphertext. 
HELLOWORLD

The output is `lippsasvph`

```javascript
function caesar(message) {
    var out = "";
    var shift = 4;

    message = message.toLowerCase();

    for (var i = 0; i < message.length; i++) {
        var charCode = message.charCodeAt(i);
        charCode += shift;

        if (charCode > 122) {
            charCode -= 26;
        }

        out += String.fromCharCode(charCode);
    }

    return out;
}

console.log(caesar("helloworld"));
```

## Q5: Vigenere Example

### Encryption

To encrypt, pick a letter in the plaintext and its corresponding letter in the keyword, use the keyword letter and the plaintext letter as the row index and column index, respectively, and the entry at the row-column intersection is the letter in the ciphertext. For example, the first letter in the plaintext is M and its corresponding keyword letter is H. This means that the row of H and the column of M are used, and the entry T at the intersection is the encrypted result.

### Decryption

To decrypt, pick a letter in the ciphertext and its corresponding letter in the keyword, use the keyword letter to find the corresponding row, and the letter heading of the column that contains the ciphertext letter is the needed plaintext letter. For example, to decrypt the first letter T in the ciphertext, we find the corresponding letter H in the keyword. Then, the row of H is used to find the corresponding letter T and the column that contains T provides the plaintext letter M (see the above figures). Consider the fifth letter P in the ciphertext. This letter corresponds to the keyword letter H and row H is used to find P. Since P is on column I, the corresponding plaintext letter is I. 

The decrypted message is `yougotitright`
