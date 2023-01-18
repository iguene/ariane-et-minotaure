from upemtk import *


def image_1(x, y, cote):
    image(x,y,"media/minoV.png","center")


cree_fenetre(900, 900)

# dessin initial du carré
cx, cy, taille = 0, 0, 10
image_1(cx, cy, taille)

# déplacement en pixels à chaque flèche pressée
dep = 90

while True:
    
    ev = donne_evenement()
    tev = type_evenement(ev)

    # déplacement du carré
    dx = 0
    dy = 0
    if tev == 'Quitte':
        break
    if tev == 'Touche':
        nom_touche = touche(ev)
        if nom_touche == 'Left':
            dx = max(-dep, -cx)
            print('left')
        elif nom_touche == 'Right':
            dx = min(dep, 899 - cx - taille)
            print('right')
        elif nom_touche == 'Down':
            dy = min(dep, 899 - cy - taille)
            print('Down')
        elif nom_touche == 'Up':
            dy = max(-dep, -cy)
            print('Up')
        if dx != 0 or dy != 0:
            efface_tout()
            cx = cx + dx
            cy = cy + dy
            image_1(cx, cy, taille)
    
    mise_a_jour()
ferme_fenetre()
