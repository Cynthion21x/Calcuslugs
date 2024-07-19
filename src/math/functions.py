import math
import src.shared.logger as l
import src.shared.constants as c

# Instructions
class Node:

    def __init__(self, type, value=None, left=None, down=None, right=None):

        self.type = type
        self.value = value
        self.left = left
        self.down = down
        self.right = right

# Tokenise Text + Generate AST
class Interpteter:

    def __init__(self, string):

        self.tokens = self.tokenize(string)
        self.length = len(self.tokens)
        self.index = 0

        self.ast = self.parse()

    # Read tokens and generate AST
    def parse(self):

        return self.addSub()
    
    # Addition / subtraction step
    def addSub(self):

        node = self.mulDiv()

        while self.index < self.length and self.tokens[self.index][0] in [c.tokens.ADD, c.tokens.SUB]:

            if self.tokens[self.index][0] == c.tokens.ADD:
                self.index += 1
                node = Node(c.tokens.ADD, left=node, right=self.mulDiv())
            elif self.tokens[self.index][0] == c.tokens.SUB:
                self.index += 1
                node = Node(c.tokens.SUB, left=node, right=self.mulDiv())

        return node

    # Multiplication / division step
    def mulDiv(self):

        node = self.exp()

        while self.index < self.length and self.tokens[self.index][0] in [c.tokens.MULT, c.tokens.DIV]:

            if self.tokens[self.index][0] == c.tokens.MULT:
                self.index += 1
                node = Node(c.tokens.MULT, left=node, right=self.exp())
            elif self.tokens[self.index][0] == c.tokens.DIV:
                self.index += 1
                node = Node(c.tokens.DIV, left=node, right=self.exp())     

        return node

    # Indicies step
    def exp(self):

        node = self.factor()

        while self.index < self.length and self.tokens[self.index][0] == c.tokens.POWER:

            self.index += 1
            node = Node(c.tokens.POWER, left=node, right=self.factor())

        return node

    # Brackets step
    def factor(self):

        token_type, token_value = self.tokens[self.index]

        if token_type == c.tokens.NEG:
            self.index += 1      
            return Node(token_type, down = self.factor())
        
        elif token_type in [c.tokens.ABSFUNC, c.tokens.SIN, c.tokens.COS, c.tokens.TAN, c.tokens.LOG, c.tokens.LN, c.tokens.SQRT]:
            self.index += 1
            return Node(token_type, down = self.factor())
        
        elif token_type == c.tokens.ABS:
            self.index += 1
            node = Node(c.tokens.ABSFUNC, down = self.parse())

            if self.index < self.length and self.tokens[self.index][0] == c.tokens.ABS:
                self.index += 1
                return node
        
        elif token_type == c.tokens.LBRACKET:
            self.index += 1
            node = self.parse()
            if self.index < self.length and self.tokens[self.index][0] == c.tokens.RBRACKET:
                self.index += 1
                return node
            
        elif token_type in [c.tokens.NUM, c.tokens.E, c.tokens.PI]:

            self.index += 1

            if token_type == c.tokens.PI:
                return Node(c.tokens.NUM, value=math.pi)
            elif token_type == c.tokens.E:
                return Node(c.tokens.NUM, value=math.e)
            elif token_type == c.tokens.NUM:
                return Node(c.tokens.NUM, value=float(token_value))
            
        elif token_type == c.tokens.VAR:

            self.index += 1

            return Node(c.tokens.VAR)
            
    # Loop over input and generate tokens to be parsed
    def tokenize(self, string):

        tokens = []

        # Numbers to be used
        digits = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '.']

        # Operators and their id
        operators = {

            "-" : c.tokens.SUB,
            "+" : c.tokens.ADD,
            "*" : c.tokens.MULT,
            "/" : c.tokens.DIV,
            "^" : c.tokens.POWER,
            "(" : c.tokens.LBRACKET,
            ")" : c.tokens.RBRACKET,
            "|" : c.tokens.ABS,
            "e" : c.tokens.E,
            "pi" : c.tokens.PI,
            "ln" : c.tokens.LN,
            "abs" : c.tokens.ABSFUNC,
            "log" : c.tokens.LOG,
            "sin" : c.tokens.SIN,
            "cos" : c.tokens.COS,
            "tan" : c.tokens.TAN,
            "sqrt" : c.tokens.SQRT,
            "x" : c.tokens.VAR

        }

        funcs = {
            "e" : c.tokens.E,
            "pi" : c.tokens.PI,
            "ln" : c.tokens.LN,
            "abs" : c.tokens.ABSFUNC,
            "log" : c.tokens.LOG,
            "sin" : c.tokens.SIN,
            "cos" : c.tokens.COS,
            "tan" : c.tokens.TAN,
            "sqrt" : c.tokens.SQRT,
            "x" : c.tokens.VAR
        }

        i = 0
        length = len(string)
        prev = '#'

        # Main Loop
        while i < length:

            curr = string[i].lower()

            two = ''
            three = ''
            four = ''

            if i < length - 3:
                four = string[i: i + 4].lower()

            if i < length - 2:
                three = string[i: i + 3].lower()

            if i < length - 1:
                two = string[i: i + 2].lower()

            addMult = curr in funcs or two in funcs or three in funcs or four in funcs

            if addMult or curr in ["("]:

                if i > 1:
                    if string[i-1] in digits:
                        tokens.append((c.tokens.MULT, "*"))

                if prev in [")"]:
                    tokens.append((c.tokens.MULT, "*"))


            if curr in operators:

                if (prev in operators or i == 0) and curr == '-':
                    tokens.append((c.tokens.NEG, curr))
                else:
                    tokens.append((operators[curr], curr))

            elif two in operators:

                tokens.append((operators[two], two))
                i += 1

            elif three in operators:

                tokens.append((operators[three], three))
                i += 2

            elif four in operators:

                tokens.append((operators[four], four))
                i += 3

            elif curr in digits:

                while i + 1 < length and string[i + 1] in digits:

                    i += 1
                    curr += string[i]

                tokens.append((c.tokens.NUM, curr))

            if i < length - 1:

                if curr in ["e", "x", ")"]:

                    if string[i+1] in digits:

                        tokens.append((c.tokens.MULT, "*"))

            if i < length - 2:

                if two in ["pi"]:

                    if string[i+2] in digits:

                        tokens.append((c.tokens.MULT, "*"))

            i += 1

            prev = curr

        l.Logger.log(tokens)
        return tokens
    
# Store AST and run it
class Function:

    def __init__(self, string):

        self.interp = Interpteter(string)
        self.name = string
        self.root = self.interp.ast

    # Start recursion
    def evaluate(self, x):

        self.x = x / 10

        try:
            ans = self.solve(self.root)
            return ans * 10
        
        except ArithmeticError:
            
            #l.Logger.log("Math Error in function", self.name, c.Logs.ERROR)
            return 0
        
        except ValueError:
            
            #l.Logger.log("Math Error in function", self.name, c.Logs.ERROR)
            return 0
   
    # Read nodes and carry out required tasks
    def solve(self, _node):

        if not _node:
            return None
        
        if _node.type == c.tokens.NUM:
            return _node.value
        
        if _node.type == c.tokens.NEG:
            return -1 * self.solve(_node.down)
        
        if _node.type == c.tokens.ABS:
            return abs(self.solve(_node.down))
        
        if _node.type == c.tokens.ABSFUNC:
            return abs(self.solve(_node.down))
        
        if _node.type == c.tokens.SIN:
            return math.sin(self.solve(_node.down))
        
        if _node.type == c.tokens.COS:
            return math.cos(self.solve(_node.down))
        
        if _node.type == c.tokens.TAN:
            return math.tan(self.solve(_node.down))
        
        if _node.type == c.tokens.SQRT:
            return math.sqrt(self.solve(_node.down))
        
        if _node.type == c.tokens.LN:
            return math.log(self.solve(_node.down), math.e)
        
        if _node.type == c.tokens.LOG:
            return math.log(self.solve(_node.down), 10)
        
        if _node.type == c.tokens.POWER:
            return self.solve(_node.left) ** self.solve(_node.right)
        
        if _node.type == c.tokens.MULT:
            return self.solve(_node.left) * self.solve(_node.right)
        
        if _node.type == c.tokens.DIV:
            return self.solve(_node.left) / self.solve(_node.right)
        
        if _node.type == c.tokens.ADD:
            return self.solve(_node.left) + self.solve(_node.right)
        
        if _node.type == c.tokens.SUB:
            return self.solve(_node.left) - self.solve(_node.right)
        
        if _node.type == c.tokens.VAR:
            return self.x
