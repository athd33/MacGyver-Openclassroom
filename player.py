import mapp

class Player():
    """
    Class used for the players moves on the mapp
    """
    def __init__(self, mapp):
        self.mapp = mapp
        self.mapp.robot = self
        grid = self.mapp.grid

        for index_x, x in enumerate(grid):
            for index_y, y in enumerate(x):
                if y == "X":
                    self.mapp.robot = [index_x, index_y]
  

    def moveMac(self, direction):
        """
        Method witch checks and defines the next position of Macgyver on the mapp
        """
        
        Rx = self.mapp.robot[0]
        Ry = self.mapp.robot[1]
        robot = self.mapp.robot
        grid = self.mapp.grid
        nextCase = None
        
        if direction == "O":
            nextCase = grid[Rx][Ry -1]
        elif direction == "E":
            nextCase = grid[Rx][Ry +1]
        elif direction == "S":
            nextCase = grid[Rx +1][Ry]
        elif direction == "N":
            nextCase = grid[Rx -1][Ry]

        if nextCase == "O":
            pass
        elif nextCase == "U":
            print('BRAVO, vous avez trouvé la sortie!!!')
            exit(0)
        else:
            if direction == "N":
                self.mapp.grid[Rx -1][Ry] = "X"
                self.mapp.grid[Rx][Ry] = " "
                robot[0] -= 1
            if direction == "S":
                self.mapp.grid[Rx +1][Ry] = "X"
                self.mapp.grid[Rx][Ry] = " "
                robot[0] += 1
            if direction == "E":
                self.mapp.grid[Rx][Ry +1] = "X"
                self.mapp.grid[Rx][Ry] = " "
                robot[1] += 1
            if direction == "O":
                self.mapp.grid[Rx][Ry -1] = "X"
                self.mapp.grid[Rx][Ry] = " "
                robot[1] -= 1
            