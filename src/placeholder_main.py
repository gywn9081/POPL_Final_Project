# This file will be the one that runs all of the outputs from antlr4
import sys
from antlr4 import *
from build.src.ExprLexer import ExprLexer
from build.src.ExprParser import ExprParser

def main(input_stream):
    lexer = ExprLexer(input_stream)
    stream = CommonTokenStream(lexer)
    parser = ExprParser(stream)
    tree = parser.prog()
    print(tree.toStringTree(recog=parser))

if __name__ == "__main__":
    input_text = InputStream("3 + 4 * (2 - 1)\n")
    main(input_text)
