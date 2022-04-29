import turtle
import string
import urllib.request
import json
f = ("Arial", 12)
t = turtle
s = t.Screen()
d = urllib.request.urlopen('file://localhost/C:/Users/minal/OneDrive/Documents/Netflux/database.json')
datas = json.load(d)
print(datas['Client','Film'])
rectangles =  []
s.setup(0.999,0.999,0,0)
t.title("-- NETFLUX --")
t.bgcolor("black")
t.color("light gray")
t.speed(1000)
t.penup()
t.hideturtle()
class Personne():
    "Definition d'une personne"
    def __init__(self, prenom, nom, sexe):
        self._prenom = prenom
        self._nom = nom
        self._sexe = sexe
    def getPrenom(self):
        return self._prenom
    def setPrenom(self, prenom):
        self._prenom = prenom
    def getNom(self):
        return self._nom
    def setNom(self, nom):
        self._nom = nom
    def getSexe(self):
        return self._sexe
    def setSexe(self, sexe):
        self._sexe = sexe
    def __str__(self):
        return 'Cette personne sappelle {} et mon nom est {} et je suis {} '.format(self._prenom, self._nom, self._sexe)

class Client(Personne):
    "Definition d'un client"
    def __init__(self, prenom, nom, sexe, dateInscription, courriel, password):
        Personne.__init__(self, prenom, nom, sexe)
        self._dateInscription = dateInscription
        self._courriel = courriel
        self._password = password
    def getDateInscription(self):
        return self._dateInscription
    def setDateInscription(self, dateInscription):
        self._dateInscription = dateInscription
    def getCourriel(self):
        return self._courriel
    def setCourriel(self, courriel):
        self._courriel = courriel
    def getPassword(self):
        return self._password
    def setPassword(self, password):
        self._password = password
    def __str__(self):
        return 'Le prenom du client est {} son nom est {} et est {} et client depuis {}  ecrivez moi a {} mon mot de passe est {}'.format(self._prenom, self._nom, self._sexe, self._dateInscription, self._courriel, self._password)

class Employe(Personne):
    "Definition d'un employé"
    def __init__(self, prenom, nom, sexe, dateEmbauche, codeUtilisateur, password, typeAcces):
        Personne.__init__(self, prenom, nom, sexe)
        self._dateEmbauche = dateEmbauche
        self._codeUtilisateur = codeUtilisateur
        self._password = password
        self._typeAcces = typeAcces
    def getDateEmbauche(self):
        return self._dateEmbauche
    def setDateEmbauche(self, dateEmbauche):
        self._dateEmbauche = dateEmbauche
    def getcodeUtilisateur(self):
        return self._codeUtilisateur
    def setCodeUtilisateur(self, codeUtilisateur):
        self._codeUtilisateur = codeUtilisateur
    def getPassword(self):
        return self._password
    def setPassword(self, password):
        self._password = password
    def getTypeAcces(self):
        return self._typeAccces
    def setTypeAcces(self, typeAcces):
        self._typeAcces = typeAcces
    def __str__(self):
        return 'Le prenom de cet employe est {} son nom de famille est {} et cest  {} et travaille depuis {}  son usager c est  {} son mot de passe est {}'.format(self._prenom, self._nom, self._sexe, self._dateEmbauche, self._codeUtilisateur, self._password, self._typeAcces)

class Acteur(Personne):
    "Definition d'un acteur"
    def __init__(self, prenom, nom, sexe, nomPersonnage, dateDebut, dateFin, cachet):
        Personne.__init__(self, prenom, nom, sexe)
        self._nomPersonnage = nomPersonnage
        self._dateDebut = dateDebut
        self._dateFin = dateFin
        self._cachet = cachet
    def getNomPersonnage(self):
        return self._nomPersonnage
    def setNomPersonnage(self, nomPersonnage):
        self._nomPersonnage = nomPersonnage
    def getDateDebut(self):
        return self._dateDebut
    def setDateDebut(self, dateDebut):
        self._dateDebut = dateDebut
    def getDateFin(self):
        return self._dateFin
    def setDateFin(self, dateFin):
        self._dateFin = dateFin
    def getCachet(self):
        return self._cachet
    def setCachet(self, cachet):
        self._cachet = cachet
    def __str__(self):
        return 'cet acteur {} ,  {} et cest  {} joue le role de {} depuis {} jusqua {} et est payé {}'.format(self._prenom, self._nom, self._sexe, self._nomPersonnage, self._dateDebut, self._dateFin, self._cachet)
class CarteCredit():
    "Definition d'une carte de credit"
    def __init__(self, numero, dateExpiration, codeSecret):
        self._numero = numero
        self._dateExpiration = dateExpiration
        self._codeSecret = codeSecret
    def getNumero(self):
        return self._numero
    def setNunero(self, numero):
        self._numero = numero
    def getDateExpiration(self):
        return self._dateExpiration
    def setDateExpiration(self, dateExpiration):
        self._dateExpiration = dateExpiration
    def getCodeSecret(self):
        return self._codeSecret
    def setCodeSecret(self, codeSecret):
        self._codeSecret = codeSecret
    def __str__(self):
        return 'Cette carte numero {} expire le {} et son code est  {} '.format(self._numero, self._dateExpiration, self._codeSecret)

class Film():
    "Definition d'un film"
    def __init__(self, nomFilm, duree, descriptionFilm):
        self._nomFilm = nomFilm
        self._duree = duree
        self._descriptionFilm = descriptionFilm
    def getNomFilm(self):
        return self._nomFilm
    def setNomFilm(self, nomFilm):
        self._nomFilm = nomFilm
    def getDuree(self):
        return self._duree
    def setDuree(self, duree):
        self._duree = duree
    def getDescriptionFilm(self):
        return self._descriptionFilm
    def setDescriptionFilm(self, descriptionFilm):
        self._descriptionFilm = descriptionFilm
    def __str__(self):
        return 'Le film {} dure  {} minute et parle de {} '.format(self._nomFilm, self._duree, self._descriptionFilm)

class Categorie():
    "Definition d'une categorie"
    def __init__(self, nomCategorie, descriptionCategorie):
        self._nomCategorie = nomCategorie
        self._descriptionCategorie = descriptionCategorie
    def getTitre(nomCategorie):
        return self._titre
    def setTitre(self, nomCategorie):
        self._nomCategorie = nomCategorie
    def getDescriptionCategorie(self):
        return self._descriptionCategorie
    def setDescriptionCategorie(self, descriptionCategorie):
        self._descriptionCategorie = descriptionCategorie
    def __str__(self):
        return 'Le style {} comprend  {}'.format(self._nomCategorie, self._descriptionCategorie)

a1 = Personne("Jamie", "Nice", "femme")
print(a1)

b = Client("James", "Bond", "homme", "2022-04-20","james007@gmail.com", "secret123")
print(b)

c = Employe ("Tom", "Smith", "homme", "2020-03-13", "tommyboy", "soleil456", "admin")
print(c)

d = Acteur("Keanu", "Reeves", "homme", "John Wick", "2013", "2021", "1 milion")
print(d)

e = CarteCredit("4540 3232 1111 2222", "05-2025", "124")
print(e)

e = Film("Parabellum", "120", "l histoire dun tueur a gages")
print(e)

f1 = Categorie("comedie", "film qui fait rire")
print(f1)



def printPicture(fileName,x,y):
    s.register_shape(fileName, None)
    s.addshape(fileName)
    t.shape(fileName)
    t.goto(x,y)
    t.stamp()

def drawInputRectangle(nomDuChamp,valeur,long,haut,x,y,secret):
    t.goto(x,y)
    t.write(nomDuChamp,font=f)
    t.goto(x+150,y)
    t.pendown()
    
    compte = 0
    while compte < 2:
        t.forward(long)
        t.left(90)
        t.forward(haut)
        t.left(90)
        compte = compte+1
    t.penup()
    textField = (valeur,x+150,x+150+long,y,y+haut)
    rectangles.append(textField)
    enteredText = []
    def copyTexte(key):
        t.forward(10)
        if secret==1:
            t.write("*",font=f)
        else:
            t.write(key, font=f)
        enteredText.append(key)
        userEntry=""
        for i in enteredText:
            userEntry=userEntry+i 
            print(valeur,"=",userEntry)   
    all_characters = string.ascii_letters + string.punctuation + string.whitespace
    for key in all_characters:
        s.onkeypress(lambda key=key: copyTexte(key), key)
        s.listen()


def testRectangle(clicX,clicY):
    for each in rectangles:
        topLeft = each[1]
        topRight = each[2]
        bottomLeft = each[3]
        bottomRight = each[4]
        if clicX>topLeft and clicY<bottomRight and clicX<topRight and clicY>bottomLeft:
         print(each[0])


printPicture("netfluxlogo.gif",0,300)
t.onscreenclick(testRectangle)

formulaire =  []

formField1 = {} 
formField1['nomDuChamps'] = "Nom d'utilisateur:"
formField1['valeur'] = "userName"
formField1['long'] = 200
formField1['haut'] = 20
formField1['x'] = -150
formField1['y'] = 150
formField1['secret'] = 0
formulaire.append(formField1)

formField2 = {}
formField2['nomDuChamps'] = "Mot de passe:"
formField2['valeur'] = "passWord"
formField2['long'] = 200
formField2['haut'] = 20
formField2['x'] = -150
formField2['y'] = 100
formField2['secret'] = 1
formulaire.append(formField2)
print(formulaire)
for item in formulaire:
    drawInputRectangle(item['nomDuChamps'],item['valeur'],item['long'],item['haut'],item['x'],item['y'],item['secret'])
t.done()


