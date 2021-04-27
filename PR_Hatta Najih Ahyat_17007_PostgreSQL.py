import psycopg2

con = psycopg2.connect(
    host="localhost", 
    port = 5432, 
    database = "test",
    user = "postgres",
    password = "Daanmogot260700!")

cur = con.cursor()


print("     Program Demo Operasi CRUD PostgresSQL Database     ")
print("                     Hatta Najih Ahyat                  ")
print("                    19/447313/SV/17007                  ")
print("                           ARM 1                        ")
print("======================================================\n")
print("Menu Operasi Database")
print("1. Create Database dan Tabel")
print("2. Insert Data")
print("3. Select/Search Data")
print("4. Update Data")
print("5. Delete Data")
menu=input("Silahkan pilih operasi ( 1 / 2 / 3 / 4 / 5 ) ? ")
print("Anda memilih : " + menu)

if menu=='1' :
    print("Create database dan tabel")
    # create a database
    con = psycopg2.connect(
    host="localhost", 
    user = "postgres",
    database = "test",
    port = 5432,
    password = "Daanmogot260700!")
    cur = con.cursor()
    # create a table
    cur = con.cursor()
    cur.execute("CREATE TABLE penilaian (name VARCHAR(100) NOT NULL, nilai INTEGER NOT NULL)")
    con.commit()

elif menu=='2' :
    print("Insert Data")
    #insert
    con = psycopg2.connect(
    host="localhost", 
    port = 5432, 
    database = "test",
    user = "postgres",
    password = "Daanmogot260700!")
    cur = con.cursor()
    cur.execute('''INSERT INTO manageuser (name, pass, stok) VALUES ('Tono', 'bonjovi', 'member');''')  
    con.commit()

elif menu=='3' :
    print("Select/Search Data")
    #search data
    con = psycopg2.connect(
    host="localhost", 
    port = 5432, 
    database = "test",
    user = "postgres",
    password = "Daanmogot260700!")
    cur = con.cursor()
    cur.execute("""SELECT * FROM sparepart""")
    query_res = cur.fetchall()
    print(query_res)

elif menu=='4' :
    print("Update data")
    #update data
    con = psycopg2.connect(
    host="localhost", 
    port = 5432, 
    database = "test",
    user = "postgres",
    password = "Daanmogot260700!")
    cur = con.cursor()
    sql1 = "UPDATE sparepart SET name = 'aki' WHERE id = 4"
    cur.execute(sql1)
    con.commit() 
    print(sql1)

elif menu=='5' :
    print("Delete data")
    #delete data
    con = psycopg2.connect(
    host="localhost", 
    port = 5432, 
    database = "test",
    user = "postgres",
    password = "Daanmogot260700!")
    cur = con.cursor()
    sql2 = "DELETE FROM sparepart WHERE id = 4"
    cur.execute(sql2)
    con.commit()
    print(sql2)
cur.close()
con.close()