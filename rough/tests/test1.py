#IRREVERSIBLE

import hashlib #import hashing library

#MULTILINE
sha512 = hashlib.sha3_512() #define hashing algo

pw = input("enter: ") #input
pw1 = pw.encode() #convert to bytestream

sha512.update(pw1) #hash

print('{} : {}'.format(pw1.decode() ,sha512.hexdigest())) #print original + hash in hexadecimal

#SINGLELINE

print(hashlib.sha3_256(pw.encode()).hexdigest())








