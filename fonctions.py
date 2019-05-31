
from mapp import MappToDisplay

def initMapp():
    with open("mapp.txt", "r") as f:
        content = f.read()                
    return content