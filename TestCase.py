
class TestCase:
    def __init__(self, inputs, output):
        self.inputs = inputs
        self.output = output

questions = list()


class Question:
    def __init__(self, name, test_case_list, description, difficulty, number):
        self.name = name
        self.test_case_list = test_case_list
        self.test_case_string = self.convert_test_cases_to_string()
        self.description = description
        self.difficulty = difficulty
        self.number = number
        global questions
        questions.append(self)

    def convert_test_cases_to_string(self):
        s = str(len(self.test_case_list)) + "\n"
        for test_case in self.test_case_list:
            s += test_case.inputs
            s += ":"
            s += test_case.output
            s += "\n"
        return s


test_cases = list()
test_cases.append(TestCase("1&4", "5"))
test_cases.append(TestCase("3&1", "4"))
test_cases.append(TestCase("8&5", "null"))
test_cases.append(TestCase("6&9", "null"))
test_cases.append(TestCase("2&3", "5"))
test_cases.append(TestCase("4&0", "4"))

a = Question("Beginner's question", test_cases, "Take two inputs as Integers. If sum is greater than 9, throw/raise Exception else print the sum",
         1, 1)

test_cases = list()
test_cases.append(TestCase("2", "2 4"))
test_cases.append(TestCase("3", "null"))
test_cases.append(TestCase("4", "2 4 6 8"))
test_cases.append(TestCase("5", "null"))
test_cases.append(TestCase("10", "2 4 6 8 10 12 14 16 18 20"))

b = Question("Even numbers", test_cases, "Take one input n as an Integer. If n is odd, then throw/raise Exception else print first n even" +
         "numbers greater than 0", 2, 2)
