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
        if len(self.pile) !=self.tailleMax:
            self.pile.append(elem)
            print(str(elem) + " a été empiler sur la pile.")
        else:
            print("la pile est pleine")

    def depiler(self):
        if len(self.pile) !=0:
            print(str(self.pile[-1])+ " a été retirer de la pile ")
            return self.pile.pop()
        else:
            print("La pile est vide")

    def estVide(self):
        return len(self.pile)==0

    def dessus(self):
        if self.estVide():
            print("La pile est vide.")
        else:
            return self.pile[-1]


