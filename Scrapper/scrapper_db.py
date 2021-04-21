import sqlite3

db = sqlite3.connect('favorites.db')
db.row_factory = lambda cursor, row: row[0]
cursor = db.cursor()
# cursor.execute("CREATE TABLE product_list (loja text,serial text,name text, price text, date date)")


def gera_lista(loja):
    search = loja
    cursor.execute("SELECT serial FROM product_list WHERE loja LIKE (?)",('%'+search+'%',))
    result = cursor.fetchall()
    result = list(set(result))
    print(result)


def salvar_banco():
    cursor.execute("INSERT INTO product_list VALUES ('"+loja+"',"+serial+",'"+name+"','"+price+"',"+data_atual+")")