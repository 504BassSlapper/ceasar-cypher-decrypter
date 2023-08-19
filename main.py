from alphabet import alphabet_dict

ciphered = list("cdiiddwpgswtgt")


def rot_all():
    for i in range(0, 26):
        decrypted = rot(i)
        print(decrypted)


def rot(i):
    decrypted = ""
    for letter in ciphered:
        value = [i for i in alphabet_dict if alphabet_dict[i] == letter]
        new_index = (value[0] + i) % 26
        letter = alphabet_dict[new_index]
        decrypted += letter
    return decrypted


rot_all()
