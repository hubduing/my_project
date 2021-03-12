from simplecrypt import encrypt, decrypt, EncryptionException, DecryptionException
with open("encrypted.bin", "rb") as inp, open("passwords.txt") as pas: # open("encrypted.txt", 'w') as enc,
    lst = [i.strip() for i in pas] # password
    encrypted = inp.read()
    for line in lst:
        #print(line)
        try:
            plaintext = decrypt(line, encrypted).decode('utf8')
            print(plaintext)
        except DecryptionException:
            continue
            print(plaintext)
        #enc.write(plaintext)
    inp.close()
    pas.close()
    #enc.close()