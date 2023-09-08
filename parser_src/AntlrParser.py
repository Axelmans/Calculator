from antlr4generated import *
from calculator_src import *
from parser_src import *


class AntlrParser(IParser):
    def parse(self, user_input: str):
        lexer = CalculatorLexer(InputStream(user_input))
        stream = CommonTokenStream(lexer)
        parser = CalculatorParser(stream)
        tree = parser.expression()
        builder = CalculatorBuilder()
        ast = builder.visit(tree)
        folder = CalculatorFolder()
        ast = ast.accept(folder)
        self.print(ast.value)
