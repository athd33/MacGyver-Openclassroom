import os
import time
from carte import Carte_Online

class Robot:
    """
    Classe définissant le robot et ses déplacements dans la carte. L'initialistation permet de récupérer les position
    de tous les éléments de la carte instanciée avec la classe CarteOnline
    """
    def __init__(self, labyrinthe_Online ):     #classe instanciée avec la classe carte en paramètre
        self.labyrinthe_Online = labyrinthe_Online

    def __repr__(self):
        """
        Méthode d'affichage de la carte
        """    
        self.grilleToList = []
        grille = self.grille

        for i in grille:   # pour tous les elements de self.grille
            self.grilleToList.append(''.join(i)) # remplissage de mappToDisplay avec les elements sans espace    
        self.mappToDisplay = "\n".join(self.grilleToList)
        
        return f"{self.mappToDisplay}"

    def deplacer(self, direction):   # méthode pour les déplacements du robot
        """
        Méthode qui récupère le choix de direction de l'utilisateur et modifie en fonction, les éléments de la grille
        """
        self.grille = self.labyrinthe_Online.grille
        robot = self.labyrinthe_Online.robot
        Rx = robot[0]
        Ry = robot[1]

        if direction == "O":
            nextCase = self.grille[Rx][Ry -1]
        elif direction == "E":
            nextCase = self.grille[Rx][Ry +1]
        elif direction == "S":
            nextCase = self.grille[Rx +1][Ry]
        elif direction == "N":
            nextCase = self.grille[Rx -1][Ry]

        if nextCase == "U":
            print('BRAVO, vous avez trouvé la sortie!')
            print("FIN DE PARTIE")
            exit()
        
        else:
            if direction == "O":
                if nextCase == "O":
                    pass
                else:
                    self.grille[Rx][Ry] = " "
                    self.grille[Rx][Ry -1] = "X" 
                    robot[1] -= 1

            if direction == "E":
                if self.grille[Rx][Ry +1] == "O":
                    pass
                else:
                    self.grille[Rx][Ry] = " "
                    self.grille[Rx][Ry +1] = "X" 
                    robot[1] += 1

            elif direction == "N":
                if self.grille[Rx -1][Ry] == "O":
                    pass
                else:
                    self.grille[Rx][Ry] = " "
                    self.grille[Rx -1][Ry] = "X" 
                    robot[0] -= 1

            elif direction == "S":
                if self.grille[Rx +1][Ry] == "O":
                    pass
                else:
                    self.grille[Rx][Ry] = " "
                    self.grille[Rx +1][Ry] = "X" 
                    robot[0] += 1
