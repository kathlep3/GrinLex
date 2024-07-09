import grin.parsing as p
from grin.token import GrinToken, GrinTokenKind
from grin.arithmetic import Arithmetic


class State:
    def __init__(self):
        self.variables = {}
        self.labels = {}
        self.gosub_lines = []


class Interpreter:
    """This class will contain code for the Grin interpreter"""
    def __init__(self):
        """Initialization, stores a set of the variables"""
        self.state = State()
        self.current_line = 0

    def let(self, tokens):
        variable = tokens[1].text()
        value = self.eval_expression(tokens[2:])
        self.state.variables[variable] = value

    def eval_expression(self, tokens):
        if len(tokens) == 1:
            token = tokens[0]
            if token.kind() == GrinTokenKind.LITERAL_INTEGER:
                return int(token.text())
            elif token.kind() == GrinTokenKind.LITERAL_FLOAT:
                return float(token.text())
            elif token.kind() == GrinTokenKind.LITERAL_STRING:
                return token.text()
            elif token.kind() == GrinTokenKind.IDENTIFIER:
                return self.state.variables.get(token.text(), 0)
        raise Exception("Invalid Expression.")

#if PRINT command is called BEFORE a LET, then the variable = 0
    def print_(self, tokens):
        """print function"""
        variable = tokens[1].text()
        if variable in self.state.variables:
            print(self.state.variables[variable])
        else:
            raise Exception("Variable '{variable}' is undefined")

    def readIn(self, tokens):
        """function for taking input for INNUM and INSTR token"""
        token_type = tokens[0]
        variable = tokens[1].text()
        if token_type.kind() == GrinTokenKind.INNUM:
            value = int(input("Enter number: "))
        elif token_type.kind() == GrinTokenKind.INSTR:
            value = input("Enter string: ")
        self.state.variables[variable] = value

    def goto(self, tokens):
        """function for goto token"""
        label = tokens[1].text()
        self.current_line = self.state.labels[label]

    def gosub(self, tokens):
        """function for gosub token"""
        label = tokens[1].text()
        self.state.gosub_lines.append(self.current_line)
        self.current_line = self.state.labels[label]

    def return_(self, tokens):
        """return function"""
        self.current_line = self.state.gosub_lines.pop()

    def end(self, tokens):
        """end function"""
        exit()

    def read_line(self, tokens):
        """This will check for the token type"""
        arithmetic = Arithmetic(tokens, self.state)
        if not tokens:
            return

#need to account for labels

        token_type = tokens[0]
        # ARITHMETIC
        if token_type.kind() in (GrinTokenKind.ADD, GrinTokenKind.SUB, GrinTokenKind.MULT, GrinTokenKind.DIV):
            variable = tokens[1].text()  # VALUE, CHECK IF INSIDE self.variables TOO
            operand = self.eval_expression(tokens[2:])
            if variable not in self.state.variables:
                self.state.variables[variable] = 0

            value = self.state.variables[variable]
            arithmetic = Arithmetic(tokens, self.state)

            if token_type.kind() == GrinTokenKind.ADD:
                self.state.variables[variable] = arithmetic.add(value, operand)  #######
            elif token_type.kind() == GrinTokenKind.SUB:
                self.state.variables[variable] = arithmetic.sub(value, operand)  #######
            elif token_type.kind() == GrinTokenKind.MULT:
                self.state.variables[variable] = arithmetic.mult(value, operand)  ######
            elif token_type.kind() == GrinTokenKind.DIV:
                self.state.variables[variable] = arithmetic.div(value, operand)  #######
        # LABELSSSSSSSSSSS
#LET
        elif token_type.kind() == GrinTokenKind.LET:
            self.let(tokens)
#PRINT
        elif token_type.kind() == GrinTokenKind.PRINT:
            self.print_(tokens)
#INNUM, INSTR
        elif token_type.kind() == GrinTokenKind.INNUM:
            self.readIn(tokens)
        elif token_type.kind() == GrinTokenKind.INSTR:
            self.readIn(tokens)

#GOTO, GOSUB
        elif token_type.kind() == GrinTokenKind.GOTO:
            self.goto(tokens)
        elif token_type.kind() == GrinTokenKind.GOSUB:
            self.gosub(tokens)
#RETURN
        elif token_type.kind() == GrinTokenKind.RETURN:
            self.return_(tokens)
#END
        elif token_type.kind() == GrinTokenKind.END:
            self.end(tokens)


#have a function that will run parsing.py for tokens
    def run(self, lines):
        for tokens in p.parse(lines):
            self.read_line(tokens)
