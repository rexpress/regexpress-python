import re
import json
import sys

from Python3Tester import Python3Tester

tester = Python3Tester()
test_strings =["Hello Python Test!", "Hello2 Python2 Test2"]

config = {
    "test_type": "match",
    "regex": "([A-Z])"
}
tester.test_regex(config, test_strings)

config = {
    "test_type": "group",
    "regex": "([A-Za-z]*)"
}
tester.test_regex(config, test_strings)

config = {
    "test_type": "replace",
    "regex": "([A-Z])",
    "replaceString": "\\1_"
}
tester.test_regex(config, test_strings)

config = {
    "test_type": "findall",
    "regex": "([A-Z])"
}
tester.test_regex(config, test_strings)