from calculator_src import CalculatorIVisitor


# self-made ast will work with nodes; basic interface that makes adding more nodes easier
class INode(object):

    def type(self):
        return self.__class__.__name__

    def __init__(self, value=None):
        # this value has different purposes depending on the concrete object
        self.value = value

    # this interface and the visitor interface form the visitor design pattern
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
        # a boolean to determine if an expression is negative
        self.negative = negative

    def accept(self, visitor: CalculatorIVisitor):
        return visitor.visitNodeExpr(self)


class NodeBinary(INode):

    def __init__(self, value=None, left: INode = None, right: INode = None):
        # store operator as value of interface object
        super().__init__(value)
        # also store the left and right operands
        self.left = left
        self.right = right

    def accept(self, visitor: CalculatorIVisitor):
        return visitor.visitNodeBinary(self)
