from mapp import MappToDisplay




def initMapp():
    with open("mapp.txt", "r") as f:
        content = f.read()                
    return content

def displayHelp():
    with open("README.md", "r") as f:
        text = f.read()
    return text
