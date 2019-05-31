import mapp

class Player():
    """
    Class used for the players moves on the mapp
    """
    def __init__(self, mapp):
        self.mapp = mapp
        self.mapp.robot = self

    def getPosition(self):
        grid = self.mapp.grid

        for index_x, x in enumerate(grid):
            for index_y, y in enumerate(x):
                if y == "X":
                    self.mapp.robot = [index_x, index_y]
    
    def __repr__(self):
        return self.mapp.robot
        