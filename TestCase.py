
class TestCase:
    def __init__(self, inputs, output):
        self.inputs = inputs
        self.output = output

questions = list()

class Question:
    def __init__(self, test_case_list, description, difficulty, number):
        self.test_case_list = test_case_list
        self.description = description
        self.difficulty = difficulty
        self.number = number
        global questions
        questions.append(self)


test_cases = list()
test_cases.append(TestCase("1\n4", "5"))
test_cases.append(TestCase("3\n1", "4"))
test_cases.append(TestCase("8\n5", None))
test_cases.append(TestCase("6\n9", None))
test_cases.append(TestCase("2\n3", "5"))
test_cases.append(TestCase("4\n0", "4"))

Question(test_cases, "Take two inputs as Integers. If sum is greater than 9, throw/raise Exception else print the sum",
         1, 1)

test_cases = list()
test_cases.append(TestCase("2", "2 4"))
test_cases.append(TestCase("3", None))
test_cases.append(TestCase("4", "2 4 6 8"))
test_cases.append(TestCase("5", None))
test_cases.append(TestCase("10", "2 4 6 8 10 12 14 16 18 20"))

Question(test_cases, "Take one input n as an Integer. If n is odd, then throw/raise Exception else print first n even" +
         "numbers greater than 0", 2, 2)
