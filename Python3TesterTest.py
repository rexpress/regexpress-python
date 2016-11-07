import unittest

from Python3Tester import Python3Tester


class Python3TesterTest(unittest.TestCase):
    tester = Python3Tester()
    test_strings = ["Hello Python Test!", "Hello2 Python2 Test2"]

    def test_match(self):
        config = {
            "test_type": "match",
            "regex": "([A-Z])"
        }
        result = self.tester.test_regex(config, self.test_strings)
        self.assertEqual(result["result"]["resultList"][0], True)
        self.assertEqual(result["result"]["resultList"][1], True)

    def test_group(self):
        config = {
            "test_type": "group",
            "regex": "([A-Za-z]*)"
        }
        result = self.tester.test_regex(config, self.test_strings)
        self.assertEqual(result["result"]["resultList"][0]["list"][0], ["Hello", "Hello"])
        self.assertEqual(result["result"]["resultList"][0]["list"][2], ["Python", "Python"])
        self.assertEqual(result["result"]["resultList"][0]["list"][4], ["Test", "Test"])
        self.assertEqual(result["result"]["resultList"][1]["list"][0], ["Hello", "Hello"])
        self.assertEqual(result["result"]["resultList"][1]["list"][3], ["Python", "Python"])
        self.assertEqual(result["result"]["resultList"][1]["list"][6], ["Test", "Test"])

    def test_replace(self):
        config = {
            "test_type": "replace",
            "regex": "([A-Z])",
            "replace": "\\1_"
        }
        result = self.tester.test_regex(config, self.test_strings)
        self.assertEqual(result["result"]["resultList"][0], "H_ello P_ython T_est!")
        self.assertEqual(result["result"]["resultList"][1], "H_ello2 P_ython2 T_est2")

    def test_findall(self):
        config = {
            "test_type": "findall",
            "regex": "([A-Z])"
        }
        result = self.tester.test_regex(config, self.test_strings)
        self.assertEqual(result["result"]["resultList"][0]["list"], [["H"], ["P"], ["T"]])
        self.assertEqual(result["result"]["resultList"][1]["list"], [["H"], ["P"], ["T"]])

if __name__ == '__main__':
    unittest.main()