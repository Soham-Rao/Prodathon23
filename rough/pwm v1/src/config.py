#IMPORT
import sys
import string
import random
import hashlib
from getpass import getpass
from utils.dbconfig import dbconfig
from rich import print as printc #customise console text for better view
from rich.console import Console

console = Console()


def generateDeviceSecret(length = 10):
    return ''.join(random.choices((string.ascii_uppercase + string.digits), k = length))


def config():
    db = dbconfig()
    cursor = db.cursor()

    printc("[green][+] Creating new config [/green]")

    
    #CREATE DB
    try:
        cursor.execute("CREATE DATABASE Password_Manager")
    except Exception as e:
        printc("[red][!] An error has occoured while creating the database.")
        console.print_exception(show_locales = True)
        sys.exit(0)

    printc("[green][+][/green] Database 'Password_Manager' has been created")

    
    #CREATE TABLES
    query = '''CREATE TABLE Password_Manager.secrets(masterkey_hash TEXT NOT NULL, device_secret TEXT NOT NULL);'''
    res = cursor.execute(query)
    db.commit()
    printc("[green][+][/green] Table 'secrets' has been created")

    query = '''CREATE TABLE Password_Manager.entries(sitename TEXT NOT NULL, siteurl TEXT NOT NULL, email TEXT, username TEXT, password TEXT NOT NULL);'''
    res = cursor.execute(query)
    db.commit()
    printc("[green][+][/green] Table 'entries' has been created")


    #CREAITING MASTERPASSWORD
    while 1:
        mp = getpass("Choose a MASTER PASSWORD: ")
        if mp == getpass("Re-Type Your Password: ") and mp != '':
            break
        printc("[yellow][-] Please try again [/yellow]")


    #HASH THE MASTERPASSWORD
    hashed_mp = hashlib.sha256(mp.encode()).hexdigest()
    printc("[green][+][/green] Generated the Hash of the MASTER PASSWORD")

    #GENERATE A DEVICE SECRET
    ds = generateDeviceSecret()


    #ADD BOTH TO TABLE
    query = '''INSERT INTO Password_Manager.secrets(masterkey_hash, device_secret) VALUES(%s, %s)'''
    values = (hashed_mp, ds)
    cursor.execute(query, values)
    db.commit()

    printc("[green][+][/green] Added to the database")
    printc("[green][+] Configuration Done! [/green]")

    db.close()


config()








