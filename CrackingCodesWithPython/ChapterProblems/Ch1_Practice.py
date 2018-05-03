from string import ascii_lowercase

lower_alpha = ascii_lowercase
i_letter = dict(enumerate(lower_alpha))
caesar = dict((v,k) for k,v in i_letter.items())

test_string = "AMBIDEXTROUS: Able to pick with equal skill a right hand pocket or a left."



def caesar_num(letter, key):
    x = caesar[letter] + key
    if x > 25:
        x = 26 - x
    return i_letter[x]

for a in test_string:
    if a.isalpha() and a.islower():
        print(caesar_num(a, 4))
    else:
        print(a)


def encrypt(input_str, key):
    encrypted_str = []
    for c in input_str:
        if c.isalpha():
            if c.isupper():
                encrypted_str.append(i_letter[caesar_num(c.lower,key)].upper())
            else:
                encrypted_str.append(i_letter[caesar_num(c,key)])
        else:
            encrypted_str.append(c)
    return encrypted_str

#test = encrypt(test_string,4)

#print(test)
