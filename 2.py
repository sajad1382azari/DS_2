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

class VariableNode(Node):
    def __init__(self, var_name):
        self.var_name = var_name

    def evaluate(self, variables):
        return variables[self.var_name]
class ConstantNode(Node):
    def __init__(self, value):
        self.value = value

    def evaluate(self, variables):
        return self.value

class MultiExpressionNode(Node):
    def __init__(self, expressions):
        self.expressions = expressions

    def evaluate(self, variables):
        return tuple(expr.evaluate(variables) for expr in self.expressions)

# Example: f(x1, x2) = (x1 / x2, x2 + x1 + 1, x1 + 1)
example = MultiExpressionNode([
    OperandNode('/', VariableNode('x1'), VariableNode('x2')),
    OperandNode('+', OperandNode('+', VariableNode('x2'), VariableNode('x1')), ConstantNode(1)),
    OperandNode('+', VariableNode('x1'), ConstantNode(1))
])

# Function to evaluate an expression tree given a dictionary of variables
def evaluate_expression_tree(tree, variables):
    return tree.evaluate(variables)

# Test the example
variable_sets = [{'x1': 1, 'x2': 2}, {'x1': 2, 'x2': 3}, {'x1': 3, 'x2': 4}, {'x1': 4, 'x2': 5}]

print("Example: f(x1, x2) = (x1 / x2, x2 + x1 + 1, x1 + 1)")
for variables in variable_sets:
    print(f"x1 = {variables['x1']}, x2 = {variables['x2']}, f(x1, x2) = {evaluate_expression_tree(example, variables)}")

