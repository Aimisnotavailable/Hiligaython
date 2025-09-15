class Executor:
    def __init__(self, parser, lexer):
        self.parser = parser
        self.lexer = lexer

    def execute(self, input_str):
        tokens = self.lexer.tokenize(input_str)
        parsed = self.parser.parse(tokens)
        return parsed