from antlr4generated import *
from antlr4.error.ErrorListener import ErrorListener
from calculator_src import *
from parser_src import *


class AntlrParser(IParser):
    def parse(self, user_input: str):
        # parsing might fail, hence the use of try-catch
        try:
            # antlr uses files corresponding to a certain grammar;
            # add an error_listener if printing errors is useful
            error_listener = CalculatorErrorListener()
            # read input
            lexer = CalculatorLexer(InputStream(user_input))
            # refresh error listener
            lexer.removeErrorListeners()
            lexer.addErrorListener(error_listener)
            # turn lexer into stream
            stream = CommonTokenStream(lexer)
            # parse stream; again refresh error listener
            parser = CalculatorParser(stream)
            parser.removeErrorListeners()
            parser.addErrorListener(error_listener)
            # fetch the tree
            tree = parser.expression()
            # use the visitors to build ast and constant fold
            builder = CalculatorBuilder()
            ast = builder.visit(tree)
            folder = CalculatorFolder()
            ast = ast.accept(folder)
            self.print(ast.value)
        except Exception as error:
            print(str(error)+"\n")
