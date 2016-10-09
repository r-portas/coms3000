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
