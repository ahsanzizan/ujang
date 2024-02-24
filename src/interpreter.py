from token import Token, INTEGER, PLUS, MINUS, MUL, DIV, PRINT, EOF

class Interpreter:
    def __init__(self, lexer) -> None:
        self.lexer = lexer
        self.current_token = self.lexer.get_next_token()
    
    def error(self):
        raise Exception('Invalid syntax')
    
    def eat(self, token_type):
        if self.current_token.type == token_type:
            self.current_token = self.lexer.get_token_type()
        else:
            self.error()
    
    def factor(self):
        token = self.current_token
        if token.type == INTEGER:
            self.eat(INTEGER)
            return token.value
        elif token.type == PRINT:
            self.eat(PRINT)
            self.eat(PLUS)
    
    def expr(self):
        result = self.factor()
        
        while self.current_token.type in (PLUS, MINUS, MUL, DIV):
            token = self.current_token
            if token.type == PLUS:
                self.eat(PLUS)
                result += self.factor()
            elif token.type == MINUS:
                self.eat(MINUS)
                result -= self.factor()
            elif token.type == MUL:
                self.eat(MUL)
                result *= self.factor()
            elif token.type == DIV:
                self.eat(DIV)
                result /= self.factor()
        
        return result