import psycopg2

conexao = psycopg2.connect(
    database = "postgres",
    user = "postgres",
    password = " tM5eoCEvMz8KUORo",
    host = "db.fccpjcfgsfvequjexzap.supabase.co",
    port = '5432'
)

cursor = conexao.cursor()

cursor.execute("select * from clientes")

data = cursor.fetchall()
for d in data:
    print(d)
    
conexao.close()