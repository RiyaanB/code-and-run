
class TestCase:
    def __init__(self, inputs, output):
        self.inputs = inputs
        self.output = output


class Question:
    def __init__(self, name, description, test_cases=None):
        self.name = name
        self.description = description
        self.test_cases = [] if test_cases is None else test_cases

    def add_case(self, inputs, output):
        self.test_cases.append(TestCase(inputs, output))


question1 = Question("Beginners question", "Input two integers. If the sum is greater than 9, throw an Exception," +
                     " else print the sum")

question1.add_case("1\n2", "3")
question1.add_case("4\n5", "9")
question1.add_case("10\n12", "null")
question1.add_case("3\n8", "null")
question1.add_case("-10\n20", "null")

question2 = Question("Even & Odd", "Input Integer N. If N is even, throw an exception else print the first N even " +
                                   "numbers greater than 0")

question2.add_case("3", "2\n4\n6")
question2.add_case("4", "null")
question2.add_case("5", "2\n4\n6\n8\n10")
question2.add_case("2", "null")
question2.add_case("7", "2\n4\n6\n8\n10\n12\n14")
