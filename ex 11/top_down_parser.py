class TopDownParser:
    def __init__(self, input_string):
        self.input = input_string
        self.index = 0

    def match(self, char):
        if self.index < len(self.input) and self.input[self.index] == char:
            self.index += 1
            return True
        return False

    # S → aA
    def S(self):
        if self.match('a'):
            return self.A()
        return False

    # A → bA | c
    def A(self):
        if self.match('b'):
            return self.A()
        elif self.match('c'):
            return True
        return False

    def parse(self):
        if self.S() and self.index == len(self.input):
            print("String Accepted")
        else:
            print("String Rejected")


# Main Program
string = input("Enter the string: ")
parser = TopDownParser(string)
parser.parse()
