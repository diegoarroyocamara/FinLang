import sys
from antlr4 import *
from FinLangLexer import FinLangLexer
from FinLangParser import FinLangParser
from interpreter import Interpreter

def main(argv):
    if len(argv) < 2:
        print("Uso: python3 main.py <percorso_file.fin>")
        return

    input_stream = FileStream(argv[1], encoding='utf-8')
    
    lexer = FinLangLexer(input_stream)
    stream = CommonTokenStream(lexer)
    parser = FinLangParser(stream)
    
    tree = parser.program()
    
    interpreter = Interpreter()
    interpreter.visit(tree)

if __name__ == '__main__':
    main(sys.argv)