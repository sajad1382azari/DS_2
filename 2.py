import math

# Base class for tree nodes
class Node:
    def evaluate(self, variables):
        raise NotImplementedError("Subclasses should implement this method!")

# Class for operand nodes (binary operations)
class OperandNode(Node):
    def __init__(self, operator, left, right):
        self.operator = operator
        self.left = left
        self.right = right

    def evaluate(self, variables):
        if self.operator == '+':
            return self.left.evaluate(variables) + self.right.evaluate(variables)
        elif self.operator == '-':
            return self.left.evaluate(variables) - self.right.evaluate(variables)
        elif self.operator == '*':
            return self.left.evaluate(variables) * self.right.evaluate(variables)
        elif self.operator == '/':
            return self.left.evaluate(variables) / self.right.evaluate(variables)
        else:
            raise ValueError(f"Unknown operator: {self.operator}")
class FunctionNode(Node):
    def __init__(self, function, child):
        self.function = function
        self.child = child

    def evaluate(self, variables):
        value = self.child.evaluate(variables)
        if self.function == 'tanh':
            return math.tanh(value)
        elif self.function == 'sin':
            return math.sin(value)
        elif self.function == 'cos':
            return math.cos(value)
        else:
            raise ValueError(f"Unknown function: {self.function}")
class VariableNode(Node):
    def __init__(self, var_name):
        self.var_name = var_name

    def evaluate(self, variables):
        return variables[self.var_name]
