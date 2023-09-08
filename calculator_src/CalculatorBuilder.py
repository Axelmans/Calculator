from calculator_src.CalculatorNodes import *
from antlr4generated.CalculatorVisitor import *
from antlr4generated.CalculatorParser import *


class CalculatorBuilder(CalculatorVisitor):

    def visitExpression(self, ctx: CalculatorParser.ExpressionContext, negative=False):
        return NodeExpr(self.visit(ctx.children[0]), negative)

    def visitNum(self, ctx: CalculatorParser.NumContext):
        node = NodeNum()
        if ctx.getText().find('.') != -1:
            node.value = float(ctx.getText())
        else:
            node.value = int(ctx.getText())
        return node

    def visitBracedExpr(self, ctx: CalculatorParser.BracedExprContext):
        return NodeExpr(self.visit(ctx.expr))

    def visitNegExpr(self, ctx: CalculatorParser.NegExprContext):
        return NodeExpr(self.visit(ctx.expr), negative=True)

    def visitAddExpr(self, ctx: CalculatorParser.AddExprContext):
        return NodeBinary(ctx.op.text, self.visit(ctx.left), self.visit(ctx.right))

    def visitMulExpr(self, ctx: CalculatorParser.MulExprContext):
        return NodeBinary(ctx.op.text, self.visit(ctx.left), self.visit(ctx.right))

