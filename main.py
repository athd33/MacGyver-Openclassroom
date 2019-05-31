from fonctions import initMapp
from mapp import *
from player import *


mappOnline = MappToDisplay(initMapp()) # instanciation of object mappOnline witch is a MappToDisplay class object

print(mappOnline)

macGyver = Player(mappOnline)


print(macGyver.mapp.robot)
