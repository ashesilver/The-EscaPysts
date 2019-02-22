Memo - classes à créer:
	*principale (menu et appel niveau) //done
	*niveau (génération)               //done
	*ennemis                           //done
	*joueur                            //done
	*objet (énigmes)		   //done
	*graphisme                         //done



classe Core -> possède les touches ainsi que la boucle principale


système de grilles pour les niveaux (classe : level)
	systeme de pièces (sidescroll)
	


Graphics : initialise la fenetre
		   peut la tuer
	a faire : une méthode changant l'écran : graphic.sidescroll(NiveauEnCours, écranNuméroX)
	
Ennemis :
	attributs :
		- self.stun (booléen)
		- self.pos (tuple : X,Y)
		- self.triggered (booléen)
		- self.playerObject (pas sur)
	- methodes :
		- walk()
		- followPlayer()
		- search()
		- checkPlayer()
	- fichier : 
		- ennemiesPatern.py
	
Player :
	méthodes :
		
		- hide()
		
	attributs :
		
Activatable :
	fichiers :
		- gridElements.py :
			format des variables : dict
			- "canHide"
			- "type"
			- "gate"   //sortir des pièces
			
			
	methodes :
		- links(self, other)
		- activateObj()
