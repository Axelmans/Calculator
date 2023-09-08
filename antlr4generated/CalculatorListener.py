# Generated from Calculator.g4 by ANTLR 4.9.2
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .CalculatorParser import CalculatorParser
else:
    from CalculatorParser import CalculatorParser

# This class defines a complete listener for a parse tree produced by CalculatorParser.
class CalculatorListener(ParseTreeListener):

    # Enter a parse tree produced by CalculatorParser#MulExpr.
    def enterMulExpr(self, ctx:CalculatorParser.MulExprContext):
        pass

    # Exit a parse tree produced by CalculatorParser#MulExpr.
    def exitMulExpr(self, ctx:CalculatorParser.MulExprContext):
        pass


    # Enter a parse tree produced by CalculatorParser#Num.
    def enterNum(self, ctx:CalculatorParser.NumContext):
        pass

    # Exit a parse tree produced by CalculatorParser#Num.
    def exitNum(self, ctx:CalculatorParser.NumContext):
        pass


    # Enter a parse tree produced by CalculatorParser#BracedExpr.
    def enterBracedExpr(self, ctx:CalculatorParser.BracedExprContext):
        pass

    # Exit a parse tree produced by CalculatorParser#BracedExpr.
    def exitBracedExpr(self, ctx:CalculatorParser.BracedExprContext):
        pass


    # Enter a parse tree produced by CalculatorParser#NegExpr.
    def enterNegExpr(self, ctx:CalculatorParser.NegExprContext):
        pass

    # Exit a parse tree produced by CalculatorParser#NegExpr.
    def exitNegExpr(self, ctx:CalculatorParser.NegExprContext):
        pass


    # Enter a parse tree produced by CalculatorParser#AddExpr.
    def enterAddExpr(self, ctx:CalculatorParser.AddExprContext):
        pass

    # Exit a parse tree produced by CalculatorParser#AddExpr.
    def exitAddExpr(self, ctx:CalculatorParser.AddExprContext):
        pass



del CalculatorParser