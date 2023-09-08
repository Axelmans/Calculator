# Generated from Calculator.g4 by ANTLR 4.9.2
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .CalculatorParser import CalculatorParser
else:
    from CalculatorParser import CalculatorParser

# This class defines a complete generic visitor for a parse tree produced by CalculatorParser.

class CalculatorVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by CalculatorParser#MulExpr.
    def visitMulExpr(self, ctx:CalculatorParser.MulExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CalculatorParser#Num.
    def visitNum(self, ctx:CalculatorParser.NumContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CalculatorParser#BracedExpr.
    def visitBracedExpr(self, ctx:CalculatorParser.BracedExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CalculatorParser#NegExpr.
    def visitNegExpr(self, ctx:CalculatorParser.NegExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CalculatorParser#AddExpr.
    def visitAddExpr(self, ctx:CalculatorParser.AddExprContext):
        return self.visitChildren(ctx)



del CalculatorParser