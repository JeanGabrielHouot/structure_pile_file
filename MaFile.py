'''
Création de la classe File

Elles s'appuient sur la structure de liste en Python.
Lors de leur construction, on impose une taille maximale.

'''


class File:
    def __init__(self,tailleMax):
        self.file = []
        self.tailleMax = tailleMax

    def ajouter(self,elem):
        self.file.append(elem)
        print(str(elem) + " a été ajouter à la file.")

    def retirer(self):
        if len(self.file) !=0:
            print("On a retire de la file"+str(self.file[-1]))
            return self.file.pop()
        return print("La file est vide")

    def estVide(self):
        return len(self.file)==0

    def avant(self):
        if self.estVide():
            return print("La file est vide.")
        return self.file[0]

    def arriere(self):
        if self.estVide():
            return print("La file est vide.")
        return self.file[-1]
