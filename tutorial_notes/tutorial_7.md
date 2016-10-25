# Tutorial 7: Information Theory and Symmetric Cryptography

## Q1

The entropy is log to base 2 of the number of possible outcomes. Thus in this case `log2(5) = 2.32`.

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

There are `2^16` different possible outcomes from coin tosses. Thus the entropy will be `log2(2^16) = log2(65536) = 16`.

## Q4

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

## Q5:

The decrypted message is `yougotitright`
