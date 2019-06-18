# MacGyver
TD Jeu - "Aidez MacGyver à s'échapper"  avec le module Pygame


Ce projet a été réalisé avec le langage Python (version 3.7) et le module Pygame depuis un environnement virtuel installé avec le gestionnaire de paquets PIP (package installer for python).

[Voir le code source...](https://github.com/athd33/MacGyver-Openclassroom)

A) Choix algorithmiques :

Le jeu se lance depuis le fichier main.py. Ce dernier contient l’initialisation du module Pygame ainsi que les boucles principales du jeu (affichage du menu, jeu en cours, menu de victoire et menu de défaite). 
Au lancement du jeu, Pygame est initié et les différents modules créés sont importés. La configuration de la surface de Pygame est définie et 3 classes sont instanciées :

a) La classe MappToDisplay :

Cette classe sert au rendu de la carte. Elle décompose le contenu du fichier mapp.txt et génère une liste de liste. L’indexation de chaque élément de la carte est réalisé, ils sont accessibles avec des index X et Y. 

b) La classe Player :

Cette classe prend en paramètre la classe MappToDisplay précédemment instanciée. Avec sa méthode init(), la classe Player récupère la position du joueur avec ses coordonnées X et Y. Sa méthode moveMac() prend en paramètre la touche directionnelle utilisée par le joueur. En fonction de la direction donnée, elle modifie la position du joueur et renvoie à la classe MappToDisplay les nouvelles coordonnées du personnage que cette dernière sera chargée de rendre à l’écran grâce à Pygame.

c) La classe ObjectsItems :

Cette classe, à l’instar de la classe Player, prend en paramètre la classe MappToDisplay précédemment instanciée. Avec sa méthode getFreeCases() , elle créé une liste qui contient l’ensemble des positions libres sur la carte (non occupées par un mur ou personnage). Le module Random et sa méthode choice() sont utilisés pour générer depuis cette liste , une position aléatoire. 
Enfin, sa méthode displayObject() attribue à chaque item du jeu, une position aléatoire qui sera retournée à la classe MappToDisplay pour l’affichage.

Nota : La classe ObjectsItems sert à placer de façon aléatoire, les item du jeu à chaque nouvelle partie.

Une fois ces classes instanciées, le menu se lance. Pygame affiche une image et les commandes disponibles (quitter, lancer le jeu, activer et désactiver le son). 

Si je joueur appui sur la touche ENTRÉE, le menu se ferme, le jeu se lance et la carte s’affiche. La classe Loader est instanciée, elle affiche l’image d’un loader en haut de la carte. Quand le joueur récupère un item sur la carte, la classe Player indique à la classe Loader que le joueur a marqué 1 point supplémentaire. Il change alors d’image à afficher.

Une fois que le joueur a récupéré l’ensemble des items (4 points), les conditions sont réunies pour qu’il sorte vainqueur. Au contact du gardien, le jeu s’arrête et la page de fin de jeu s’affiche. Le joueur peut quitter le programme avec la touche Q ou recommencer avec la touche ENTRÉE.

Si le joueur n’a pas ses 4 points au contact du gardien, le jeu s’arrête. La fenêtre affiche le message de fin de partie (perdue),  Le joueur peut quitter le programme avec la touche Q ou recommencer avec la touche ENTRÉE.