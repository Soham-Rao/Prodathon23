#Random Password Generator

import random 

upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
lower = upper.lower()
digit = "0123456789"
symbols = "!@#$%^&*()}{|][:;'.,/?><-=+_`~"

up, low, num, sym = True, True, True, True

all  = ''

if up == True:
    all += upper
if low == True:
    all += lower
if num == True:
    all += digit
if sym == True:
    all += symbols

length = 20
amount = 1


for i in range(amount):
    password = ''.join(random.sample(all, length)) 

    print(password)

