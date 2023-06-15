"""
sudo apt install python3-virtualenv
virtualenv ~/dev/learnpy/venv && source ~/dev/learnpy/venv/bin/activate
pip install psycopg2-binary
~/dev/learnpy/venv/bin/deactivate # disable virtualenv
"""
import psycopg2.extras
import psycopg2

conn = psycopg2.connect(database="habrdb",
                        host="localhost",
                        user="habrpguser",
                        password="pgpwd4habr",
                        port="5432")
cursor = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)
cursor.execute("SELECT * FROM document_template")
print(cursor.fetchone())
result = cursor.fetchmany(size=5)
for y in result:
    print("id:", y['id'], ", desc:", y['description'])

count = cursor.fetchall()
cursor.execute("INSERT INTO document_template (id, name, description) VALUES(%s, %s, %s)",
               (len(count) + 1, "Wolf", "Some wolf from Rock"))
conn.commit()

cursor.close()
conn.close()




