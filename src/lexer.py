from utoken import Token, INTEGER, PLUS, MINUS, MUL, DIV, PRINT, EOF

class Lexer:
    def __init__(self, text: str) -> None:
        self.text = text
        self.pos = 0
    
    def error(self):
        raise Exception('Invalid character')
    
    def advance(self):
        self.pos += 1
        if self.pos < len(self.text):
            self.current_char = self.text[self.pos]
        else:
            self.current_char = None
    
    def skip_whitespace(self):
        while self.current_char is not None and self.current_char.isspace():
            self.advance()
    
    def get_next_token(self):
        # If the position is still in the text content
        while self.current_char is not None:
            # Skips whitespace
            if self.current_char.isspace():
                self.skip_whitespace()
                continue

            if self.current_char.isdigit():
                return Token(INTEGER, int(self.current_char))

            if self.current_char == '+':
                token = Token(PLUS, self.current_char)
                self.advance()
                return token

            if self.current_char == '-':
                token = Token(MINUS, self.current_char)
                self.advance()
                return token

            if self.current_char == '*':
                token = Token(MUL, self.current_char)
                self.advance()
                return token

            if self.current_char == '/':
                token = Token(DIV, self.current_char)
                self.advance()
                return token

            if self.current_char == 'p':
                token = Token(PRINT, self.current_char)
                self.advance()
                return token

            self.error()

        return Token(EOF, None)
        