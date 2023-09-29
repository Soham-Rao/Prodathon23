from getpass import getpass
from Cryptodome.Protocol.KDF import PBKDF2
from Cryptodome.Hash import SHA512
from Cryptodome.Random import get_random_bytes
from utils.dbconfig import dbconfig
from rich import print as printc
from rich.console import console

import utils.aesutil



def computeMasterKey(mp, ds):
    password = mp.encode()
    salt = ds.encode()
    key = PBKDF2(password, salt, 32, count = 1000000, hmac_hash_module = SHA512)
    return key


def addEntry(mp, ds, sitename, siteurl, email, username):
    #ENCRYPT PASSWORD
    password = getpass("Password: ")
    mk = computeMasterKey(mp, ds) 

    encrypted = utils.aesutil.encrypt(key = mk, source = password, keyType = "bytes")

    #ADD TO DATABASE

    db = dbconfig()
    cursor = db.cursor()
    query = '''INSERT INTO Password_Manager.entries (sitename, siteurl, email, username, password) VALUES (%s, %s, %s, %s, %s);'''
    values = (sitename, siteurl, email, username, encrypted)
    cursor.execute(query, values)
    db.commit()

    printc("[green][+][/green] Entry has been added")







