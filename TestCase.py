
class TestCase:
    def __init__(self, inputs, output):
        self.inputs = inputs
        self.output = output


test_cases = list()
test_cases.append(TestCase("1 4", "5"))
test_cases.append(TestCase("3 1", "4"))
test_cases.append(TestCase("8 5", "Exception"))
test_cases.append(TestCase("6 9", "Exception"))
test_cases.append(TestCase("2 3", "5"))
test_cases.append(TestCase("4 0", "4"))
