from calculator_src import CalculatorIVisitor


class INode(object):

    def type(self):
        return self.__class__.__name__

    def __init__(self, value=None):
        self.value = value

    def accept(self, visitor: CalculatorIVisitor):
        pass


class NodeNum(INode):

    def __init__(self, value=None):
        super().__init__(value)

    def accept(self, visitor: CalculatorIVisitor):
        return visitor.visitNodeNum(self)


class NodeExpr(INode):

    def __init__(self, expression: INode = None, negative: bool = False):
        super().__init__()
        self.expression = expression
        self.negative = negative

    def accept(self, visitor: CalculatorIVisitor):
        return visitor.visitNodeExpr(self)


class NodeBinary(INode):

    def __init__(self, value=None, left: INode = None, right: INode = None):
        super().__init__(value)
        self.left = left
        self.right = right

    def accept(self, visitor: CalculatorIVisitor):
        return visitor.visitNodeBinary(self)
