#IMPORT
import mysql.connector as sql
from rich.console import Console #rich module helps make python mode readable

console = Console()

#CONNECT
def dbconfig():
    try:
        db = sql.connect(
            host = 'localhost',
            user = 'root',
            password = 'password'
        )  
    except Exception as e:
        console.print_exception(show_locals = True)

    return db
