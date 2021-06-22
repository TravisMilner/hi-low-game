from game import hi_low

import unittest

class TestWin(unittest.TestCase):
    def test_player_choice_wins_if_higher(self):
        
        
        actual = hi_low(10, 5)
        self.assertEqual(10,actual)

    def test_computer_choice_wins_if_higher(self):
         
         actual = hi_low(2,7)
         self.assertEqual(7,actual)

    def test_computer_choice_player_choice_same_is_tie(self):
        
        actual = hi_low(5,5)
        self.assertEqual(5,actual)

if __name__ == '__main__':
    unittest.main()
