# Tutorial 7: Information Theory and Symmetric Cryptography

## Q1

The entropy is log to base 2 of the number of possible outcomes. Thus in this case `log2(5) = 2.32`.

The smallest encoding scheme would be 3 bits. Such as:

```
A: 000
B: 001
C: 010
D: 011
E: 100
```

## Q2
![Calculation](resources/wk7_calc.png "Calculation")
\ 

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
