import sys
from lexer import Lexer
from interpreter import Interpreter

if __name__ == '__main__':
    if len(sys.argv) != 2:
        print('Usage: python3 main.py <filename>')
        sys.exit(1)
    
    filename = sys.argv[1]
    try:
        # If the file is not a .ujang file
        if filename.split('.')[1] != 'ujang':
            raise Exception(f"'{filename}' is not an ujang file")
        
        with open(filename, 'r') as ujang_file:
            text = ujang_file.read()
    except FileNotFoundError:
        print(f"File '{filename}' not found.")
        sys.exit(1)
    
    lexer = Lexer(text)
    interpreter = Interpreter(lexer)
    result = interpreter.expr()
    print(result)