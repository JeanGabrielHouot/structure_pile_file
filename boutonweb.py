# On utilise le module tkinter pour faire les fenêtres.
# On importe le module de Pile

from MaPile import *
from tkinter import *

# On crée ici une instance de fenetre avec tkinter
fenetre = Tk()


monsite = "Mon site pr�f�r�"

# Je garde en mémoire la taille de ma fenêtre
w = 250
h = 200

# On crée une pile historique et une pile temporaire 
# La pile temporaire garde en mémoire les sites
# Je donne une taille de 50 

hist = Pile(50)
tmp_hist = Pile(50)


# je crée les fonctions associées aux boutons
# ajouter: ajoute un site dans la pile hist
# avancer: renvoie vers le site suivant
# reculer: envoie vers le site précédent

def ajouter(site):
    monSite.delete("all")
    monSite.create_text(w/2,h/2, text=site, font="Arial 24", fill="blue")
    monSite.pack(side=TOP, padx=10, pady=10)
    hist.empiler(site)
    return
    
def avancer():
    elem = tmp_hist.depiler()
    hist.empiler(elem)

def reculer():
    elem = hist.depiler()
    tmp_hist.empiler(elem)
    
# Je rentre a liste de sites
mesSiteWeb = ["Google", "Mozilla", "Youtube","Wikip�dia","Amazon","Sncf"]


# Je crée ma fenêtre graphique avec la commande Canavas
monSite = Canvas(fenetre, width=w, height=h, bg='white')

# J'affiche un texte dans le canvas
monSite.create_text(w/2,h/2, text=monsite, font="Arial 24", fill="blue")
monSite.pack(side=TOP, padx=10, pady=10)

# Je crée les boutons avancer et reculer 
# On assice les fonctions via command

Bouton_reculer = Button(fenetre, text ='Reculer',command = reculer)
Bouton_reculer.pack(side=LEFT, padx=5, pady=5)

Bouton_avancer = Button(fenetre, text ='Avancer',command = avancer)
Bouton_avancer.pack(side=RIGHT, padx=5, pady=5)

# Je crée les autres boutons

for site in mesSiteWeb:
    Bouton_site = Button(fenetre, text=site, borderwidth=2,command = ajouter(site))
    Bouton_site.pack(side=LEFT, padx =5,pady=5)

# On affiche la fenêtre ici
fenetre.mainloop()


# Le bug semble provenir au niveau de la fonction ajouter ou de Bouton_site


