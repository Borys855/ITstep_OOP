import unittest


class My_Test(unittest.TestCase):
    def test_args(self):
        self.assertEqual(aiter(2,2), 4)

    def test_kwargs(self):
        self.assertEqual(aiter(a=10,b=1), 21)

    def test_mix(self):
        self.assertEqual(aiter(1, a=1), 3)

    def test_diff(self):
        x = 10
        y = 0
        self.assertEqual(aiter(0, -5, y, a=x), 5)

    def test_wrong(self):
        self.assertEqual(aiter("5", "abc",10), 15)

        if __name__ == '__main__':
            unittest.main()
