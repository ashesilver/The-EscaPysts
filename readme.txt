Memo - classes à créer:
	*principale (menu et appel niveau) //done
	*niveau (génération)               //done
	*ennemis                           //done
	*joueur                            //done
	*objet (énigmes)		   		   //done
	*graphisme                         //done


split class files system.



classe Core -> possède les touches ainsi que la boucle principale  


système de grilles pour les niveaux (classe : level) //done
	systeme de pièces (sidescroll)  // bas les couilles
	


Graphics : initialise la fenetre //done
		   peut la tuer//done
	a faire : une méthode changant l'écran : graphic.sidescroll(NiveauEnCours, écranNuméroX)
	
Ennemis :
	attributs :
		- self.stun (booléen)  //done
		- self.pos (tuple : X,Y) //done
		- self.triggered (booléen)  //done
		- self.playerObject (pas sur)  //done
	- methodes :
		- walk()  //done
		- followPlayer() //done
		- search()  //done
		- checkPlayer()  //done
	- fichier : 
		- ennemiesPatern.py  //done
	
Player :
	méthodes :
		
		- hide()  //done
		
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
