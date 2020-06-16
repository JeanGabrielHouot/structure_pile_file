# Function qui teste le bon parenthésage des symboles dans une expression

from MaPile import *

# On improte la classe Pile avec le fichier MaPile


def bonneParenthese(monTexte):
    mesSymboles = Pile(len(monTexte))

    for symbole in monTexte:
        if symbole in "([{":
            mesSymboles.empiler(symbole)
        if symbole in ")]}": 
            if mesSymboles.estVide(): 
                return False
            elif mesSymboles.dessus() == '(' and symbole == ')':
                mesSymboles.depiler()
            elif mesSymboles.dessus() == '[' and symbole == ']':
                mesSymboles.depiler()
            elif mesSymboles.dessus() == '{' and symbole == '}':
                mesSymboles.depiler()
            else:
                return False
    return mesSymboles.estVide()


txt1 = "((voici) un bon) [parenthésage]"
rep1 = bonneParenthese(txt1)
print(rep1)


txt2 = "((voici) un mauvais{) [}parenthésage]"
rep2 = bonneParenthese(txt2)
print(rep2)


