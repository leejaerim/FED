import unittest

from components.wantedparser import WantedParser


class MyTestCase(unittest.TestCase):
    def setUp(self) -> None:
        #before start each method
        pass
    def tearDown(self) -> None:
        #after methods end.
        pass
    def test_something(self):
        self.assertEqual(True, True)  # add assertion here
    def test_parser_return_must_be_dict(self):
        wp = WantedParser("https://www.wanted.co.kr").get_row_data()
        self.assertEqual(type({}),type(wp))  # parser's result must be dict

if __name__ == '__main__':
    unittest.main()
