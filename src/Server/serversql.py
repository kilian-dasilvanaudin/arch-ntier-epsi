import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="",
  database="db_gag"
)

mycursor = mydb.cursor()

mycursor.execute("SELECT * FROM cmd")

myresult = mycursor.fetchall()

for x in myresult:
  print(x)

mycursor.execute("SELECT DISTINCT(client.nom) FROM cmd JOIN client on cmd.nomCli=client.nom JOIN prod ON cmd.nProd = prod.design WHERE prod.couleur = 'rouge'")

myresult = mycursor.fetchall()
for x in myresult:
    print(x)