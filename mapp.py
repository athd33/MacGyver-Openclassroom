

class MappToDisplay():
    """
    Class used to build a indexation of all elements on the mapp
    """
    def __init__(self, content):
        self.content = content
        self.grid = []          #self.grid is a list of of the elements on the mapp
        self.lines = self.content.split('\n')
        self.robot = None

        for line in self.lines:             # creating grid for indexation of each element of the game lab
            self.grid.append([c for c in line])


    def __repr__(self):
        self.mappRebuilded = [] #empty list        
        for i in self.grid: # joining elements in lines
            self.mappRebuilded.append("".join(i))
        
        self.mappToDisplay = "\n".join(self.mappRebuilded) # joining lines in list

        return f"{self.mappToDisplay}"

