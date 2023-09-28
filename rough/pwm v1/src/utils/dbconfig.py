import mysql.connector as sql
from rich import Console #rich module helps make python mode readable

console = Console()

def dbconfig():
    try:
        sql.connect(
            host = 'localhost',
            user = 'root',
            password = 'password',
            database = 'prodathon' 
        )  
    except Exception as e:
        console.print_exception(show_locals = True)

        