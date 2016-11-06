import re
import json
import sys


class Python3Tester:
    def __init__(self):
        pass

    def test_regex(self, config, test_strings):
        try:
            flags = 0
            if "IGNORECASE" in config and config["IGNORECASE"] is True:
                flags |= re.I
            if "LOCALE" in config and config["LOCALE"] is True:
                flags |= re.L
            if "MULTILINE" in config and config["MULTILINE"] is True:
                flags |= re.M
            if "DOTALL" in config and config["DOTALL"] is True:
                flags |= re.D
            if "ASCII" in config and config["ASCII"] is True:
                flags |= re.A
            if "VERBOSE" in config and config["VERBOSE"] is True:
                flags |= re.V

            if "test_type" not in config:
                raise Exception("test_type parameter doesn't exists.")

            test_type = config["test_type"]
            regex = config["regex"]
            pattern = re.compile(regex, flags)
            result = {
                "type": "",
                "result": {
                    "resultList": []
                }
            }

            if test_type == "match":
                result["type"] = "MATCH"

                for test_string in test_strings:
                    if pattern.match(test_string):
                        result["result"]["resultList"].append(True)
                    else:
                        result["result"]["resultList"].append(False)
            elif test_type == "group":
                result["type"] = "GROUP"
                for test_string in test_strings:
                    iterator = pattern.finditer(test_string)

                    groupsList = {"list": []}
                    result["result"]["resultList"].append(groupsList)
                    for match in iterator:
                        groups = []
                        for group in match.groups():
                            groups.append(group)
                        groupsList["list"].append(groups);
            elif test_type == "replace":
                for test_string in test_strings:
                    result["type"] = "STRING"
                    replace_string = ""
                    if "replace" in config:
                        replace_string = config["replace"]
                    replaced = pattern.sub(replace_string, test_string)
                    result["result"]["resultList"].append(replaced)
            elif test_type == "findall":
                result["type"] = "GROUP"
                for test_string in test_strings:
                    groupsList = {"list": [[]]}
                    result["result"]["resultList"].append(groupsList)
                    found = pattern.findall(test_string)
                    for word in found:
                        groupsList["list"][0].append(word);

        except Exception as e:
            result = {
                "exception": str(e)
            }

        return result


def main():
    config = json.loads(sys.argv[1])
    test_strings = json.loads(sys.argv[2])

    tester = Python3Tester()
    result = tester.test_regex(config, test_strings)

    print("##START_RESULT##")
    print(json.dumps(result))
    print("##END_RESULT##")


if __name__ == "__main__":
    main()
