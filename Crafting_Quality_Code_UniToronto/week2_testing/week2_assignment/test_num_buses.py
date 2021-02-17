import a1
import unittest


class TestNumBuses(unittest.TestCase):
    """ Test class for function a1.num_buses. """

    # Add your test methods for a1.num_buses here.
    def test_num_buses_higher(self):
        """Boundary condition test.

        Am integer number higher than a threshold.
        """
        
        people = 101
        self.assertEqual(a1.num_buses(people), 3)

    def test_num_buses_lesser(self):
        """Boundary condition test.

        Am integer number lesser than a threshold.
        """
        
        people = 49
        self.assertEqual(a1.num_buses(people), 1)

    def test_num_buses_zero(self):
        """Boundary condition test.

        A zero integer number of people.
        """
        
        people = 0
        self.assertEqual(a1.num_buses(people), 0)

    def test_num_buses_exact(self):
        """Boundary condition test.

        An integer number of people that equals exactly a threshold.
        """
        
        people = 50
        self.assertEqual(a1.num_buses(people), 1)

    def test_num_buses_multiple(self):
        """Boundary condition test.

        An integer number of people that equals a multiply 
        of a threshold.
        """
        
        people = 500
        self.assertEqual(a1.num_buses(people), 10)

if __name__ == '__main__':
    unittest.main(exit=False)
