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
