from antlr4.error import ErrorListener


class CalculatorErrorListener(ErrorListener.ErrorListener):

    # Override the syntaxError function since this error should be handled in an own way
    def syntaxError(self, recognizer, offendingSymbol, line, column, msg, e):
        raise SyntaxError(f"Syntax Error! Message: {msg}")
