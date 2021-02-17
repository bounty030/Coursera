import unittest
import a2



class TestRat(unittest.TestCase):
    """
    Test class for class Rat.
    """

    rat1 = a2.Rat("Tim", 1, 2)
    rat2 = a2.Rat("Claudia", 3, 4)

    def test_rat_init(self):
        """
        Test the initialization of two rats.
        """

        self.assertEqual(self.rat1.name, "Tim")
        self.assertEqual(self.rat2.name, "Claudia")

        self.assertEqual(self.rat1.row, 1)
        self.assertEqual(self.rat1.col, 2)

        self.assertEqual(self.rat2.row, 3)
        self.assertEqual(self.rat2.col, 4)


    def test_set_location(self):
        """
        Test set location method by changing the location of two rats.
        """

        r1 = 3
        r2 = 5

        self.rat1.set_location(r1, r1)
        self.rat2.set_location(r2, r2)

        self.assertEqual(self.rat1.row, r1)
        self.assertEqual(self.rat1.col, r1)

        self.assertEqual(self.rat2.row, r2)
        self.assertEqual(self.rat2.col, r2)


    def test_eat_sprout(self):
        """
        Test the method eat sprout by: 
        - check number of sprouts eaten after initialization
        - check number of sprouts eaten after calling method eat_sprouts.
        """

        self.assertEqual(self.rat1.num_sprouts_eaten, 0)

        self.rat1.eat_sprout()

        self.assertEqual(self.rat1.num_sprouts_eaten, 1)


    def test_rat_str(self):
        """
        Test the print function of rat.
        """

        string = '{0} at ({1}, {2}) ate {3} sprouts.'.format(self.rat2.name, self.rat2.row, self.rat2.col, self.rat2.num_sprouts_eaten)

        self.assertEqual(self.rat2.__str__(), string)


class TestMaze(unittest.TestCase):
    """
    Test the class Maze.
    """

    rat1 = a2.Rat('J', 1, 1)
    rat2 = a2.Rat('P', 1, 4)
    maze = a2.Maze([['#', '#', '#', '#', '#', '#', '#'], 
                    ['#', '.', '.', '.', '.', '.', '#'], 
                    ['#', '.', '#', '#', '#', '.', '#'], 
                    ['#', '.', '.', '@', '#', '.', '#'], 
                    ['#', '@', '#', '.', '@', '.', '#'], 
                    ['#', '#', '#', '#', '#', '#', '#']], 
                    rat1,
                    rat2)

    def test_maze_init(self):
        """
        Test the initialization of a maze.
        """
        self.assertEqual(self.maze.num_sprouts_left, 3)
        self.assertEqual(self.maze.rat_1, self.rat1)
        self.assertEqual(self.maze.rat_2, self.rat2)


    def test_is_wall(self):
        """
        Test the is_wall method by:
        - checking a wall
        - checking a sprout
        - checking a hall
        """

        self.assertEqual(self.maze.is_wall(0, 0), True) # wall
        self.assertEqual(self.maze.is_wall(3, 4), True) # wall
        self.assertEqual(self.maze.is_wall(1, 1), False) # hall
        self.assertEqual(self.maze.is_wall(4, 1), False) # sprout


    def test_get_char(self):
        """
        Test the get_character method by:
        - checking a location of a sprout
        - checking a location of a wall
        - checking a location of a hall
        - checking a location of a rat
        """

        self.assertEqual(self.maze.get_character(0, 0), "#") # wall
        self.assertEqual(self.maze.get_character(3, 4), "#") # wall
        self.assertEqual(self.maze.get_character(1, 2), ".") # hall
        self.assertEqual(self.maze.get_character(4, 1), "@") # sprout
        self.assertEqual(self.maze.get_character(1, 1), "J") # rat1
        self.assertEqual(self.maze.get_character(1, 4), "P") # rat2


    def test_maze_move(self):
        """
        Test the method move by:
        - moving a rat to a hall
        - moving a rat to a wall
        - moving a rat to a sprout
        """

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


        # Do not move rat1.
        self.maze.move(self.rat1, NO_CHANGE, NO_CHANGE)
        self.assertEqual(self.rat1.row, 1)
        self.assertEqual(self.rat1.col, 1)

        # Move rat1 to a hall.
        self.maze.move(self.rat1, DOWN, NO_CHANGE)
        self.assertEqual(self.rat1.row, 2)
        self.assertEqual(self.rat1.col, 1)

        # Move rat1 to a wall. The rat should not move.
        result = self.maze.move(self.rat1, NO_CHANGE, DOWN)
        self.assertEqual(result, False)
        self.assertEqual(self.rat1.row, 2)
        self.assertEqual(self.rat1.col, 1)        
 
        """
        Move rat1 to a sprout:
        - make the location a HALL
        - decrease the num_sprouts_left by 1
        - return True if and only if there wasn't a wall 
        """
        # number of sprouts eaten before a sprout was eaten
        self.assertEqual(self.rat1.num_sprouts_eaten, 0) 

        # move rat to sprout
        self.maze.move(self.rat1, DOWN, NO_CHANGE) # rat is at (3, 1) - hall
        self.maze.move(self.rat1, NO_CHANGE, RIGHT) # rat is at (3, 2) - hall
        self.assertEqual(self.maze.get_character(3, 3), "@") # check if sprout is at (3, 3)
        self.maze.move(self.rat1, NO_CHANGE, RIGHT) # rat is at (3, 3) - sprout
        
        # check if rat is at (3, 3)
        self.assertEqual(self.rat1.row, 3)
        self.assertEqual(self.rat1.col, 3)
 
        # check if rat ate sprout
        self.assertEqual(self.rat1.num_sprouts_eaten, 1) 

        # check if rats location is returned
        self.assertEqual(self.maze.get_character(3, 3), "J")

        # move rat and check if brussel sprout changed to hall
        self.maze.move(self.rat1, DOWN, NO_CHANGE) # rat is at (4, 3) - hall
        self.assertEqual(self.maze.get_character(3, 3), ".")


        # check if number of sprouts left is reduced by one
        self.assertEqual(self.maze.num_sprouts_left, 2)


    def test_maze_str(self):

        rat1 = a2.Rat('J', 1, 1)
        rat2 = a2.Rat('P', 1, 4)

        maze = a2.Maze([['#', '#', '#', '#', '#', '#', '#'], 
                    ['#', '.', '.', '.', '.', '.', '#']], 
                    rat1,
                    rat2)

        maze_string = "#######\n#J..P.#\n"
        rat1_string = rat1.__str__()
        rat2_string = rat2.__str__()
        result = maze_string + rat1_string + "\n" + rat2_string

        self.assertEqual(maze.__str__(), result)

if __name__ == "__main__":
    unittest.main(exit=False)