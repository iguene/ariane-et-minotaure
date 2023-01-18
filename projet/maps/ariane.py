from upemtk import*
from time import*
def f(moussa):
	fic=open(moussa,"r")
	texte= fic.read()
	liste=texte.split("\n")
	ligne=[]
	for i in range(len( liste)-2):
		ligne.append(list(liste[i]))
	return (ligne)

#print(f("labyrinthe1.txt"))

	
	

def dessine_labyrinthe(a):
	
	
	for i in range (len( a)):
		
		for j in range (len(a[i])):
			
			if a[i][j]=="-":
				
				ligne((j-1)*40,i*40,(j+1)*40,i*40)
				
			elif a[i][j]=="|":
				
				ligne(j*40,(i-1)*40,j*40,(i+1)*40)
				
			elif a[i][j]=="P":
				
				porte(j*40,i*40,40)
				
			elif a[i][j]=="H":
				
				minH(j*40,i*40,40)
				
				
			elif a[i][j]=="V":
				
				minV(j*40,i*40,40)
				
			elif a[i][j]=="A":
				
				arian(j*40,i*40,40)

			elif a[i][j]=="T":
				
				thesee(j*40,i*40,40)
			
			elif a[i][j]=="D":
				arian(j*40,i*40,40)
				thesee(j*40,i*40,40)
			
			elif a[i][j]=="F":
				porte(j*40,i*40,40)
				arian(j*40,i*40,40)
				thesee(j*40,i*40,40)
			
			elif a[i][j]=="PH":
				minoH_attrape(j*40,i*40,40)
			
			elif a[i][j]=="PV":
				minoV_attrape(j*40,i*40,40)
			elif a[i][j]=="VA":
				minoVar(j*40,i*40,40)
			elif a[i][j]=="HA":
				minoHar(j*40,i*40,40)

def position_ariane(a):
	
	lst=[]
	for i in range (len( a)):
		
		for j in range (len(a[i])):
			if a[i][j]=="A":
				px,py=j,i
				lst.append((px,py))

	return lst

def position_thesee(a):
	
	lst=[]
	for i in range (len( a)):
		
		for j in range (len(a)):
			if a[i][j]=="T":
				px,py=j,i
				lst.append((px,py))

	return lst


def mino(a):
	mino=[]
	for i in range (len(a)):
		for j in range (len(a)):
				if a[i][j]=="V"or a[i][j]=="H":
					px,py=j,i
					mino.append((px,py))
	return mino

def position_minoV(a):
	lst_m=[]
	for i in range (len( a)):
		
		for j in range (len(a)):
			if a[i][j]=="V" : 
				px,py=j,i
				lst_m.append((px,py))

	return lst_m	

def position_minoH(a):
	lst_m=[]
	for i in range (len( a)):
		
		for j in range (len(a)):
			if a[i][j]=="H" : 
				px,py=j,i
				lst_m.append((px,py))

	return lst_m	

				
def minH(x, y, cote):
	image(x,y,"media/minoH.png","center")
def minV(x, y, cote):
	image(x,y,"media/minoV.png","center")
def arian(x,y,cote):
	image(x,y,"media/ariane.png","center")
def porte(x,y,cote):
	image(x,y,"media/porte.png","center")
def thesee(x,y,cote):
	image(x,y,"media/thesee.png","center")
def minoH_attrape(x,y,cote):
	image(x,y,"media/ariane.png","center")
	image(x,y,"media/thesee.png","center")
	image(x,y,"media/minoH.png","center")
def minoV_attrape(x,y,cote):
	image(x,y,"media/ariane.png","center")
	image(x,y,"media/thesee.png","center")
	image(x,y,"media/minoV.png","center")
def minoHar(x,y, cote):
	image(x,y,"media/ariane.png","center")
	image(x,y,"media/minoH.png","center")
def minoVar(x,y,cote):
	image(x,y,"media/ariane.png","center")
	image(x,y,"media/minoV.png","center")
def position_porte(a):
	lst_p=[]
	for i in range (len( a)):
		
		for j in range (len(a)):
			if a[i][j]=="P" : 
				px,py=j,i
				lst_p.append((px,py))

	return lst_p	

def murs(a):
	lst_m=[]
	for i in range (len( a)):
		
		for j in range (len(a)):
			if a[i][j]==" " : 
				px,py=j,i
				lst_m.append((px,py))

	return lst_m	
def perdu ():
	 texte (450,450 ,"vous avez perdu", couleur = "red", ancrage="center")
def gagne():
		texte (450,450 ,"vous avez gagné", couleur = "red", ancrage="center")
if __name__ == "__main__":
	
	
	c =int(input("choisissez votre numero de labyrinthe(taper1,2,3,4ou5):"))
	if c==1:
		fichier="labyrinthe1.txt"
	if c==2:
		fichier="labyrinthe2.txt"
	if c==3:
		fichier="labyrinthe3.txt"
	if c==4:
		fichier="labyrinthe4.txt"
	if c==5:
		fichier="labyrinthe5.txt"
	
	framerate =5

	ariane=(40,40)

	cree_fenetre(900,
				   900)
	f(fichier)

	laby=f(fichier)

	dessine_labyrinthe(laby)

	i=position_ariane(laby)[0][1]

	j=position_ariane(laby)[0][0]

	tx=position_thesee(laby)[0][0]

	ty=position_thesee(laby)[0][1]

	px=position_porte(laby)[0][0]

	py=position_porte(laby)[0][1]

	hx=position_minoH(laby)[0][0]

	hy=position_minoH(laby)[0][1]

	vx=position_minoV(laby)[0][0]

	vy=position_minoV(laby)[0][1]

	print(position_ariane(laby))

	print(mino(laby))

	print("px=",px)
	while True:

		ev = donne_evenement()

		tev = type_evenement(ev)

		if tev == 'Quitte':

			break

		if tev == 'Touche':

			nom_touche = touche(ev)

			print(nom_touche)

			x=0

			if (nom_touche == 'Left') and (j-1,i) in murs(laby) and (j-2,i)not in mino(laby) and (j-2,i)not in position_porte(laby):
				
				laby[i][j-2],laby[i][j]=laby[i][j],laby[i][j-2]

				j=j-2

				print(j,i)

			elif (nom_touche == 'Right')and (j+1,i)in murs(laby) and (j+2,i) not  in mino(laby) and (j+2,i) not  in position_porte(laby):

				ar=laby[1][1]

				laby[i][j+2],laby[i][j]=laby[i][j],laby[i][j+2]

				j=j+2

				print(j,i)

			elif (nom_touche == 'Down') and (j,i+1) in murs(laby) and (j,i+2)not in mino(laby) and (j,i+2)not in position_porte(laby):

				ar=laby[1][1]

				laby[i+2][j],laby[i][j]=laby[i][j],laby[i+2][j]

				i=i+2

				print(j,i)

			elif nom_touche == 'Up' and (j,i-1) in murs(laby) and (j,i-2) not in mino (laby) and (j,i-2) not in mino (laby):

				ar=laby[1][1]

				laby[i-2][j],laby[i][j]=laby[i][j],laby[i-2][j]

				i=i-2

				print(j,i)
			

			else :

				print ("déplacement impossible")
				
			if ((j,i)==(tx+2,ty)and (j-1,i) in murs(laby)) or ((j,i)==(tx-2,ty) and (j+1,i) in murs(laby)) or ((j,i)==(tx,ty+2) and (j,i-1) in murs(laby)) or ((j,i)==(tx,ty-2)and (j,i+1) in murs(laby)):

				laby[ty][tx]=" "

				laby[i][j]="D"
			
			if (j,i)==((px+2,py)and (j-1,i) in murs(laby)) or ((j,i)==(px-2,py)and (j+1,i) in murs(laby)) or ((j,i)==(px,py+2)and (j,i-1) in murs(laby)) or( (j,i)==(px,py-2)and (j,i+1) in murs(laby)):

				laby[i][j]=" "

				laby[py][px]="F"

				print("gagné")
				v= "gané"
				break
			
			
			if i<vy and (vx,vy-1)  in murs(laby) and (vx,vy-2) not in position_minoV(laby) and (vx,vy-2) not in position_ariane(laby)  and (vx,vy-2) not in position_thesee(laby) and (vx,vy-2) not in position_porte(laby) and (vx,vy-2)!=(hx,hy) :

				laby[vy-2][vx],laby[vy][vx]=laby[vy][vx],laby[vy-2][vx]
				position_minoV(laby).remove((position_minoV(laby)[0][0],position_minoV(laby)[0][1]))
				vy= vy-2
				position_minoV(laby).append((vx,vy))
				
			elif i>vy and(vx,vy+1)  in murs(laby) and (vx,vy+2) not in position_minoV(laby) and (vx,vy+2) not in position_ariane(laby)  and (vx,vy+2) not in position_thesee(laby) and (vx,vy+2) not in position_porte(laby) and (vx,vy+2)!=(hx,hy) :

				laby[vy+2][vx],laby[vy][vx]=laby[vy][vx],laby[vy+2][vx]
				position_minoV(laby).remove((position_minoV(laby)[0][0],position_minoV(laby)[0][1]))

				vy=vy+2
				position_minoV(laby).append((vx,vy))
				
			elif i==vy and j<vx and (vx-1,vy)  in murs(laby)and (vx-2,vy) not in position_minoV(laby) and (vx-2,vy) not in position_ariane(laby)  and (vx-2,vy) not in position_thesee(laby) and (vx-2,vy) not in position_porte(laby) and (vx-2,vy)!=(hx,hy)  :
				while vx>j+2 and (vx-1,vy) in murs(laby):
					laby[vy][vx-2],laby[vy][vx]=laby[vy][vx],laby[vy][vx-2]
					position_minoV(laby).remove((position_minoV(laby)[0][0],position_minoV(laby)[0][1]))
					vx=vx-2
					position_minoV(laby).append((vx,vy))

			elif i==vy and j>vx and (vx+1,vy)  in murs(laby)and (vx+2,vy) not in position_minoV(laby) and (vx+2,vy) not in position_ariane(laby)  and (vx+2,vy) not in position_thesee(laby) and (vx+2,vy) not in position_porte(laby) and (vx+2,vy)!=(hx,hy) :
				while vx<j-2 and (vx+1,vy)in murs(laby):
					laby[vy][vx+2],laby[vy][vx]=laby[vy][vx],laby[vy][vx+2]
					position_minoV(laby).remove((position_minoV(laby)[0][0],position_minoV(laby)[0][1]))

					vx=vx+2
					position_minoV(laby).append((vx,vy))
			
			
			if j<hx and (hx-1,hy)  in murs(laby)and (hx-2,hy) not in position_minoV(laby) and (hx-2,hy) not in position_ariane(laby)  and (hx-2,hy) not in position_thesee(laby) and (hx-2,hy) not in position_porte(laby) and (hx-2,hy)!=(vx,vy) :
				
				laby[hy][hx-2],laby[hy][hx]=laby[hy][hx],laby[hy][hx-2]

				hx= hx-2
				
			elif j>hx and(hx+1,hy)  in murs(laby) and (hx+2,hy) not in position_minoV(laby) and (hx+2,hy) not in position_ariane(laby)  and (hx+2,hy) not in position_thesee(laby) and (hx+2,hy) not in position_porte(laby)and (hx+2,hy)!=(vx,vy)  :
				laby[hy][hx+2],laby[hy][hx]=laby[hy][hx],laby[hy][hx+2]

				hx=hx+2
				
			elif j==hx and i<hy and (hx,hy-1)  in murs(laby) and (hx,hy-2) not in position_minoV(laby) and (hx,hy-2) not in position_ariane(laby)  and (hx,hy-2) not in position_thesee(laby) and (hx,hy-2) not in position_porte(laby)and (hx,hy-2)!=(vx,vy)  :

				while hy>i+2 and (hx,hy-1) in murs(laby):
					laby[hy-2][hx],laby[hy][hx]=laby[hy][hx],laby[hy-2][hx]

					hy=hy-2
				
			elif j==hx and i>hy and (hx,hy+1)  in murs(laby) and (hx,hy+2) not in position_minoV(laby) and (hx,hy+2) not in position_ariane(laby)  and (hx,hy+2) not in position_thesee(laby) and (hx,hy+2) not in position_porte(laby) and (hx,hy+2)!=(vx,vy) :
				while hy<i-2 and (hx,hy+1) in murs (laby):
					laby[hy+2][hx],laby[hy][hx]=laby[hy][hx],laby[hy+2][hx]
					
					hy=hy+2
			if laby[i][j]=="D":	
				if ((j,i)==(vx,vy+2)and (vx,vy+1)  in murs(laby) ) or ((j,i)==(vx,vy-2)and(vx,vy-1)  in murs(laby))  :
					laby[vy][vx]=" "
					laby[i][j]="PV"
					v="perdu"
					break
				if ((j,i)==(hx+2,hy) and (hx+1,hy)  in murs(laby) )  or ((j,i)==(hx-2,hy) and (hx-1,hy)  in murs(laby)) :
					laby[hy][hx]=" "
					laby[i][j]="PH"
					v="perdu"
					break
			if laby[i][j]=="A":
				if ((j,i)==(vx,vy+2)and (vx,vy+1)  in murs(laby) ) or ((j,i)==(vx,vy-2)and(vx,vy-1)  in murs(laby))or((j,i)==(vx+2,vy) and (vx+1,vy)  in murs(laby) )  or ((j,i)==(vx-2,vy) and (vx-1,vy)  in murs(laby)):
					laby[vy][vx]=" "
					laby[i][j]="VA"
					v="perdu"
					break
				if ((j,i)==(hx+2,hy) and (hx+1,hy)  in murs(laby) )  or ((j,i)==(hx-2,hy) and (hx-1,hy)  in murs(laby)) or ((j,i)==(hx,hy+2)and (hx,hy+1)  in murs(laby) ) or ((j,i)==(hx,hy-2)and(hx,hy-1)  in murs(laby)) :
					laby[hy][hx]=" "
					laby[i][j]="HA"
					v="perdu"
					break
		efface_tout()	
		dessine_labyrinthe(laby)
		mise_a_jour()
	efface_tout()
	dessine_labyrinthe(laby)
	if v=="perdu":
		perdu()
	else:
		gagne()
	mise_a_jour()
	sleep(4)
	
	
