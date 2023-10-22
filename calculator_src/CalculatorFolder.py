from calculator_src import CalculatorIVisitor, CalculatorNodes


class CalculatorFolder(CalculatorIVisitor):

    def visitNodeExpr(self, node: CalculatorNodes.NodeExpr):
        # fold the expression
        node.expression = node.expression.accept(self)
        # negate if necessary
        if node.negative:
            node.expression.value *= -1
        return node.expression

    def visitNodeBinary(self, node: CalculatorNodes.NodeBinary):
        # fold operands first
        left = node.left.accept(self)
        right = node.right.accept(self)
        # check operator and calculate result
        if node.value == "+":
            return CalculatorNodes.NodeNum(left.value + right.value)
        elif node.value == "-":
            return CalculatorNodes.NodeNum(left.value - right.value)
        elif node.value == "*":
            return CalculatorNodes.NodeNum(left.value * right.value)
        elif node.value in ["/", "%"]:
            # division/modulo 0 is undefined
            if right.value == 0:
                raise ValueError("Division by 0 error!")
            if node.value == "/":
                return CalculatorNodes.NodeNum(left.value / right.value)
            return CalculatorNodes.NodeNum(left.value % right.value)

    def visitNodeNum(self, node: CalculatorNodes.NodeNum):
        # a number is already folded by default
        return node
