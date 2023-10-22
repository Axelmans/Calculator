import abc
from calculator_src import CalculatorNodes


# an interface for a calculator ast visitor; adding visitors for more functionality possible
class CalculatorIVisitor(abc.ABC):

    # one visit function for each type of node used by the calculator
    @abc.abstractmethod
    def visitNodeNum(self, node: CalculatorNodes.NodeNum):
        pass

    @abc.abstractmethod
    def visitNodeBinary(self, node: CalculatorNodes.NodeBinary):
        pass

    @abc.abstractmethod
    def visitNodeExpr(self, node: CalculatorNodes.NodeExpr):
        pass
