# Do not import any modules. If you do, the tester may reject your submission.

# Constants for the contents of the maze.

# The visual representation of a wall.
WALL = '#'

# The visual representation of a hallway.
HALL = '.'

# The visual representation of a brussels sprout.
SPROUT = '@'

# Constants for the directions. Use these to make Rats move.

# The left direction.
LEFT = -1

# The right direction.
RIGHT = 1

# No change in direction.
NO_CHANGE = 0

# The up direction.
UP = -1

# The down direction.
DOWN = 1

# The letters for rat_1 and rat_2 in the maze.
RAT_1_CHAR = 'J'
RAT_2_CHAR = 'P'


class Rat:
    """ A rat caught in a maze. """

    # Write your Rat methods here.
    def __init__(self, name, row, col):
        """(Rat, str, int, int) -> NoneType​

        Initialize a rat with a single character name, starting row, column, and set number of sprouts eaten to zero. 

        Example: Rat('P', 1, 4)
        """

        self.name = name
        self.row = row
        self.col = col
        self.num_sprouts_eaten = 0


    def set_location(self, row, col):
        """(Rat, int, int) -> NoneType

        Set the rat's row and col instance variables to the given row and column.
        """

        self.row = row
        self.col = col


    def eat_sprout(self):
        """(Rat) -> NoneType

        Increases num_sprouts_eaten by one.
        """

        self.num_sprouts_eaten += 1


    def __str__(self):
        """(Rat) -> str

        Return a string representation of of the rat in this format:
        symbol at (row, col) ate num_sprouts_eaten sprouts.

        >>> paul = Rat('P', 1, 2)
        >>> print(paul)
        P at (1, 2) ate 0 sprouts.
        """

        return '{0} at ({1}, {2}) ate {3} sprouts.'.format(self.name, self.row, self.col, self.num_sprouts_eaten)


class Maze:
    """ A 2D maze. """

    # Write your Maze methods here.
    def __init__(self, maze, rat_1, rat_2):
        """(Maze, list of list of str, Rat, Rat) -> NoneType

        Initialize a maze with two rats.
        
        Args:
            maze (list of list of str): a maze with contents.
            rat_1 (object): the first rat in the maze.
            rat_2 (object): the second rat in the maze.

        Example call: 
        Maze([['#', '#', '#', '#', '#', '#', '#'], 
        ['#', '.', '.', '.', '.', '.', '#'], 
        ['#', '.', '#', '#', '#', '.', '#'], 
        ['#', '.', '.', '@', '#', '.', '#'], 
        ['#', '@', '#', '.', '@', '.', '#'], 
        ['#', '#', '#', '#', '#', '#', '#']], 
        Rat('J', 1, 1),
        Rat('P', 1, 4))
        """

        self.maze = maze
        self.rat_1 = rat_1
        self.rat_2 = rat_2

        self.num_sprouts_left = 0
        # Count the number of sprouts left in the maze
        for i in range(len(self.maze)):
            row = self.maze[i]
            self.num_sprouts_left += row.count('@') 

    
    def is_wall(self, row, col):
        """(Maze, int, int) -> bool​

        Return True if there is a wall at the row and col.

        Args:
            row (int): row to check if there is a wall.
            col (int): column to check if there is a wall.
        """

        if self.maze[row][col] == '#':
            return True
        else:
            return False


    def get_character(self, row, col):
        """(Maze, int, int) -> str​

        Return the character in the maze at the given row and column.

        Args:
            row (int): row of maze to check.
            col (int): col of maze to check.
        """
        if (row == self.rat_1.row) and (col == self.rat_1.col):
            return self.rat_1.name
        if (row == self.rat_2.row) and (col == self.rat_2.col):
            return self.rat_2.name
        else:
            return self.maze[row][col]



    def move(self, rat, vert_direct, hor_direct):
        """(Maze, Rat, int, int) -> bool​

        Move the rat in the given direction, unless there is a wall in the way. Also, check for a Brussels sprout at that location.
        If a sprout is eaten: 
        - make the location a HALL
        - decrease the num_sprouts_left by 1
        - return True if and only if there wasn't a wall 

        Args:
            rat ([type]): object of the rat that moves.
            vert_direct ([type]): vertical direction change (UP, NO_CHANGE or DOWN).
            hor_direct ([type]): horizontal direction change (LEFT, NO_CHANGE or RIGHT).
        """

        new_row, new_col = rat.row + vert_direct, rat.col + hor_direct 
        
        if self.is_wall(new_row, new_col) == False:
            rat.set_location(new_row, new_col)
            # Eat sprout when rat moved to a location of a sprout.
            # Change sprout to hall.
            if (self.get_character(new_row, new_col) == rat.name) and (self.maze[new_row][new_col] == "@"):
                rat.eat_sprout()
                self.num_sprouts_left -= 1
                self.maze[new_row][new_col] = '.'

            return True
        else:
            return False


    def __str__(self):
        """(Maze) -> str

        Return a string representation of the maze.
        """

        # check row location of rats
        rat1_row = self.rat_1.row
        rat1_col = self.rat_1.col
        rat2_row = self.rat_2.row
        rat2_col = self.rat_2.col

        string = ''
        for i in range(len(self.maze)):
            row = self.maze[i]
            row_string = ""

            # Set name symbol at column location of row
            if i == rat1_row:
                row[rat1_col] = self.rat_1.name
            if i == rat2_row:
                row[rat2_col] = self.rat_2.name

            # convert a row of symbols to a string
            for symbol in row:
                row_string += symbol

            string = string + row_string  + '\n'


        string = string + self.rat_1.__str__() + '\n' + self.rat_2.__str__()

        return string


if __name__ == '__main__':
    import doctest
    doctest.testmod()