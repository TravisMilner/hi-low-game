from game import hi_low

import unittest

class TestWin(unittest.TestCase):
    def test_won(self):
        
        self.assertEqual("Loser",hi_low(5,10))
        self.assertEqual("Tie", hi_low(10,10))
        self.assertEqual("Winner", hi_low(10,5))

if __name__ == '__main__':
    unittest.main()
