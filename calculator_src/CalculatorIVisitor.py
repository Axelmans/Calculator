from calculator_src import CalculatorNodes


class CalculatorIVisitor:

    def visitNodeNum(self, node: CalculatorNodes.NodeNum):
        pass

    def visitNodeBinary(self, node: CalculatorNodes.NodeBinary):
        node.left.accept(self)
        node.right.accept(self)

    def visitNodeExpr(self, node: CalculatorNodes.NodeExpr):
        node.expression.accept(self)
