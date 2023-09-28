#IRREVERSIBLE

import hashlib

iterations = 500000

key = hashlib.pbkdf2_hmac('sha3_512', b"password", b"salt"*2, iterations)
#password based key derivation function 2 - hash based message authentication code


print(hashlib.sha3_512(b"password").hexdigest()) #hashed once with no salt
print(key.hex()) #hashed 500k times w salt

#hashlib.pbkdf2_hmac(hash_name, password, salt, iterations, dklen=None)  SYNTAX