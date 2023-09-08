from calculator_src import CalculatorIVisitor, CalculatorNodes
import sys


class CalculatorFolder(CalculatorIVisitor):

    def visitNodeExpr(self, node: CalculatorNodes.NodeExpr):
        node.expression = node.expression.accept(self)
        if node.negative:
            node.expression.value *= -1
        return node.expression

    def visitNodeBinary(self, node: CalculatorNodes.NodeBinary):
        left = node.left.accept(self)
        right = node.right.accept(self)
        if node.value == "+":
            return CalculatorNodes.NodeNum(left.value + right.value)
        elif node.value == "-":
            return CalculatorNodes.NodeNum(left.value - right.value)
        elif node.value == "*":
            return CalculatorNodes.NodeNum(left.value * right.value)
        elif node.value in ["/", "%"]:
            if right.value == 0:
                sys.exit("[Error]: division by zero.")
            if node.value == "/":
                return CalculatorNodes.NodeNum(left.value / right.value)
            return CalculatorNodes.NodeNum(left.value % right.value)

    def visitNodeNum(self, node: CalculatorNodes.NodeNum):
        return node
