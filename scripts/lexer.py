class Lexer:
    
    TT_EOF = 'EOF'
    TT_INT = 'INT'
    TT_FLOAT = 'FLOAT'
    TT_STRING = 'STRING'
    TT_MINUS = 'MINUS'
    TT_PLUS = 'PLUS'
    TT_MUL = 'MUL'
    TT_DIV = 'DIV'
    TT_LPAREN = 'LPAREN'
    TT_RPAREN = 'RPAREN'

    class Token:
        def __init__(self, type_, value):
            self.type = type_
            self.value = value
        
        def __repr__(self):
            return f"Token({self.type}, {self.value})"
    

    class Error:
        def __init__(self, file_name, pos_start, pos_end, error_name, details):
            self.file_name = file_name
            self.pos_start = pos_start
            self.pos_end = pos_end
            self.error_name = error_name
            self.details = details
        
        def as_string(self):
            result  = f"{self.error_name}: {self.details}\n"
            result += f"File {self.file_name}, line {self.pos_start}"
            return result
        
    def __init__(self):
        self.file_name = "<stdin>"
        self.row = 0
        self.col = -1
        self.current_char = None
        self.pos = -1
        self.text = ""
        self.advance()

    def advance(self):
        self.col += 1
        self.pos += 1
        if self.pos < len(self.text):
            self.current_char = self.text[self.pos]
        else:
            self.current_char = None

    def make_number(self) -> 'Lexer.Token':
        num_str = ''
        dot_count = 0
        
        while self.current_char is not None and (self.current_char.isdigit() or self.current_char == '.'):
            if self.current_char == '.':
                if dot_count == 1:
                    break
                dot_count += 1
                num_str += '.'
            else:
                num_str += self.current_char
            self.advance()
        
        if dot_count == 0:
            return self.Token(self.TT_INT, int(num_str))
        else:
            return self.Token(self.TT_FLOAT, float(num_str))
        
    def tokenize(self, input_str) -> list['Lexer.Token']:
        self.text = input_str
        self.pos = -1
        self.advance()
        
        tokens = []
        
        while self.current_char is not None:
            if self.current_char.isspace():
                self.advance()
            elif self.current_char.isdigit():
                tokens.append(self.make_number())
            elif self.current_char == '+':
                tokens.append(self.Token(self.TT_PLUS, '+'))
                self.advance()
            elif self.current_char == '-':
                tokens.append(self.Token(self.TT_MINUS, '-'))
                self.advance()
            elif self.current_char == '*':
                tokens.append(self.Token(self.TT_MUL, '*'))
                self.advance()
            elif self.current_char == '/':
                tokens.append(self.Token(self.TT_DIV, '/'))
                self.advance()
            elif self.current_char == '(':
                tokens.append(self.Token(self.TT_LPAREN, '('))
                self.advance()
            elif self.current_char == ')':
                tokens.append(self.Token(self.TT_RPAREN, ')'))
                self.advance()
            else:
                return self.Error(self.file_name, self.row, self.col, 'Illegal Character', self.current_char).as_string()
        
        self.row += 1
        self.col = 0
        tokens.append(self.Token(self.TT_EOF, None))
        return tokens