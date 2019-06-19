                            

**MAC-GYVER: THE ESCAPE GAME**


**Introduction :**
This project is a 2D labyrinth game realised with Python3.6 and le Pygame module in his version 1.9.

In this game, you are [MacGyver](https://en.wikipedia.org/wiki/MacGyver) (the tv-show hero). Your trapped in a labyrinth, and your mission (if you accept it) is to escape 
after collecting all the items present on the mapp.
You'll have to find and collect :

    > - bottle
    > - plastic tube
    > - syringe
    > - needle

Once you have all of these items (green logo on the top of the labyrinth), go and see the guard. You win!!! 
Watch out! If you forget a item on the mapp, the gard will not let you out!

This have been made with python 3.6 and pygame 1.9.6


**Installation:**

**Open your terminal and follow me:**

    1) To download the project run :
    
        git clone https://github.com/athd33/MacGyver-Openclassroom.git

    2) Then, open the project with :

        cd MacGyver-Openclassroom

    3) Now, run the command line to build the executable :

        python3 ./setup.py build

    4) Once its build, move in the created folders by typing :

        cd build/exe.linux-x86_64-3.6/

    5) Great! To launch the game, enter :

        ./main

    6) Have fun !



**Code composition:**

    main.py : main programm file. 
    constants.py: files containing all the constant variables (images, sounds, dimensions...2)
    mapp.py: Classes created to render the mapp on screen
    player.py: Class used to set the new position of the player on each keyboard command
    items.py : Class created to set random positions for the objects on the mapp
    mapp.txt : A text document representing the labyrinth mapp
    folder /sounds : The wav files
    folder /images : The images of the game
    requirement.txt: The list of the dependencies needed to run
    

**Game steps:**

    1) Display of the menu screen, press ENTER to play or Q to quit.
    2) In game, display or the labyrinth. Objects have a random position each time you launch the game.
    3) The player goes arround the mapp and get all the items. The loader image changes at each element catched!
    4) The players exit the mapp when he gets to the guard:
        
        a) All objects are collected : Win page displayes , press Q to exit and go back to the main menu.
        b) The player didn't find all the objects, Game Over page is displayed. Press Q to quit and go back to menu.

**Expected:**

    Code droppend on Github
    Use virtualenv to code
    Respect PEP8
    Use english
