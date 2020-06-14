'''
Création de la classe Pile

Elles s'appuient sur la structure de liste en Python.
Lors de leur construction, on impose une taille maximale.

'''

class Pile:
    def __init__(self,tailleMax):
        self.pile = []
        self.tailleMax = tailleMax

    def empiler(self,elem):
        self.pile.append(elem)
        print(str(elem) + " a été empiler sur la pile.")

    def depiler(self):
        if len(self.pile) !=0:
            print("On a retire de la pile "+str(self.pile[-1]))
            return self.pile.pop()
        return print("La pile est vide")

    def estVide(self):
        return len(self.pile)==0

    def dessus(self):
        if self.estVide():
            return print("La pile est vide.")
        return self.pile[-1]


