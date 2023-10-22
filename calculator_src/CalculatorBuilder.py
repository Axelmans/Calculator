from calculator_src.CalculatorNodes import *
from antlr4generated.CalculatorVisitor import *
from antlr4generated.CalculatorParser import *


class CalculatorBuilder(CalculatorVisitor):

    # boolean argument (false by default) is used to know if an expression must be negated during calculation
    def visitExpression(self, ctx: CalculatorParser.ExpressionContext, negative=False):
        return NodeExpr(self.visit(ctx.children[0]), negative)

    def visitNum(self, ctx: CalculatorParser.NumContext):
        node = NodeNum()
        # store as float value if the number contains the decimal point
        if ctx.getText().find('.') != -1:
            node.value = float(ctx.getText())
        else:
            node.value = int(ctx.getText())
        return node

    def visitBracedExpr(self, ctx: CalculatorParser.BracedExprContext):
        # can be made into a regular expression since operator precedence is respected by the parsing process
        return NodeExpr(self.visit(ctx.expr))

    def visitNegExpr(self, ctx: CalculatorParser.NegExprContext):
        # store as a regular expression, but set negative to true
        return NodeExpr(self.visit(ctx.expr), negative=True)

    def visitAddExpr(self, ctx: CalculatorParser.AddExprContext):
        # store as a binary operation
        return NodeBinary(ctx.op.text, self.visit(ctx.left), self.visit(ctx.right))

    def visitMulExpr(self, ctx: CalculatorParser.MulExprContext):
        # also store as binary operation, again, operator precedence is already respected
        return NodeBinary(ctx.op.text, self.visit(ctx.left), self.visit(ctx.right))
