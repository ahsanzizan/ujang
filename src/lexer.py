from token import Token, INTEGER, PLUS, MINUS, MUL, DIV, PRINT, EOF

class Lexer:
    def __init__(self, text: str) -> None:
        self.text = text
        self.pos = 0
    
    def error(self):
        raise Exception('Invalid character')
    
    def get_next_token(self):
        # If the position is out of the text content
        if self.pos >= len(self.text):
            return Token(EOF, None)
        
        current_char = self.text[self.pos]
        
        if current_char.isdigit():
            token = Token(INTEGER, int(current_char))
            self.pos += 1
            return token
        
        if current_char == '+':
            token = Token(PLUS, current_char)
            self.pos += 1
            return token
        
        if current_char == '-':
            token = Token(PLUS, current_char)
            self.pos += 1
            return token
        
        if current_char == '*':
            token = Token(MUL, current_char)
            self.pos += 1
            return token
        
        if current_char == '/':
            token = Token(DIV, current_char)
            self.pos += 1
            return token

        if current_char == 'p':
            token = Token(PRINT, current_char)
            self.pos += 1
            return token

        self.error()
        