import sqlite3
conn = sqlite3.connect('try.db')
c = conn.cursor()


c.execute('CREATE TABLE IF NOT EXISTS name(name TEXT)')
c.execute('INSERT INTO name VALUES("Nesh")')

query = 'SELECT * FROM name WHERE name='
while True:
    nameINput = input("Enter your name:  ")
    nka = nameINput + query
    c.execute(nka)
    if c.rowcount == 1:
        print("Yaay")
    else:
        print("Sad life :'(")
