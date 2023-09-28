#IRREVERSIBLE

import hashlib

one = hashlib.sha256()
two = hashlib.sha512()

password = "password"

pw = password.encode()

#hashing pw
one.update(pw)

hashed = one.hexdigest()

#hashing hash
hh = hashed.encode()

two.update(hh)

print('{} : {}'.format("1", one.hexdigest()))
print('{} : {}'.format("2", two.hexdigest()))
#more secure

print(one.digest_size, two.digest_size)


