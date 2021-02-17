import unittest
import restaurant_rec as res

class TestRestaurant(unittest.TestCase):

    name_to_rating = {  'Georgie Porgie': 87,
                        'Queen St. Cafe': 82,
                        'Dumplings R Us': 71,
                        'Mexican Grill': 85,
                        'Deep Fried Everything': 52}


    def test_build_rating_list(self):
        self.assertEqual(res.build_rating_list(self.name_to_rating, ['Georgie Porgie']), [[[87, 'Georgie Porgie']]])
        self.assertEqual(res.build_rating_list(self.name_to_rating, ['Deep Fried Everything']), [[[52, 'Deep Fried Everything']]])
        self.assertEqual(res.build_rating_list(self.name_to_rating, ['Dumplings R Us']), [[[71, 'Dumplings R Us']]])


if __name__ == '__main__':
    unittest.main()