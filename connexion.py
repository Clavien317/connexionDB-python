import mysql
import mysql.connector



conn = mysql.connector.connect(
    host="localhost",
    user="root",
    database="mydb",
    password=""
)

if(conn):
    print("CONNECTED !")
else:
    print("No connected....")

matricule = input("Saisissez votre matricule :")
nom = input("Entrez votre nom :")
prenom = input("Entrez votre prenom :")
niveau = input("Entrez votre niveau Maintenant :")
parcours = input("Entrez votre parcours :")

lien = conn.cursor()
ajout = ("INSERT INTO etudiant (matricule,nom,prenom,niveau,parcours) VALUES (%s,%s,%s,%s,%s)")
value =[matricule,nom,prenom,niveau,parcours]
lien.execute(ajout,value)
print("---------OK-------\n\n")
print("1 Etudiant ajouter avec succees")
print("---------OK-------\n\n")
conn.commit()


req = ("SELECT * FROM etudiant")
lien.execute(req)

row = lien.fetchall()

for i in row:
    print(i)


lien.close()
conn.close()


