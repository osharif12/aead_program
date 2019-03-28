# Practice aead encryption

from aead import AEAD
import sys

file = sys.argv[1]
print('Name of the file you want to encrypt is ', file)

flag = True
cryptor = AEAD(AEAD.generate_key())

while(flag):
    response = input('Enter 1 to encrypt file, 2 to decrypt file, and 3 to exit program: ')

    if response == "1":
        with open('spring.txt', 'r') as myfile:
            data = myfile.read()
        myfile.close()

        bytesData = data.encode()
        encrypted = cryptor.encrypt(bytesData, b"AuthenticatedData")
        print('encrypted: ', encrypted)

        with open('spring.txt', 'w') as the_file:
            the_file.write(encrypted.decode("utf-8"))
        the_file.close()

    elif response == "2":
        with open('spring.txt', 'r') as myfile:
            data = myfile.read()
        myfile.close()

        bytesData = data.encode()
        print(bytesData)
        decrypted = cryptor.decrypt(bytesData, b"AuthenticatedData")

        with open('spring.txt', 'w') as the_file:
            the_file.write(decrypted.decode("utf-8"))
        the_file.close()

    elif response == "3":
        flag = False
        print('\nExiting Program!!!\n')
        break



'''
#print(data)
bytesData = data.encode()

cryptor = AEAD(AEAD.generate_key())

ct = cryptor.encrypt(bytesData, b"PrivateKey")

print('The encrypted file is: \n', ct)

dt = cryptor.decrypt(ct, b"PrivateKey")

print('Hello world decrypted is ', dt)
'''