# This file will be the one that runs all of the outputs from antlr4
import sys
from antlr4 import *
from build.ArithmeticLexer import ArithmeticLexer
from build.ArithmeticParser import ArithmeticParser

# The following was taken from HW2
def main(input_stream):
    lexer = ArithmeticLexer(input_stream)
    tokens = CommonTokenStream(lexer)
    parser = ArithmeticParser(tokens)
    # The following method is the start method defined in the grammar
    tree = parser.start()
    # Default
    # print(tree.toStringTree(recog=parser))
    # Pretty tree
    # pretty_print_tree(tree, parser)
    # Child only pretty tree
    pretty_print_tree(tree, parser, child_only=True)


# Raw trees are terrible so do this
from antlr4.tree.Tree import TerminalNodeImpl

def pretty_print_tree(tree, parser, level=0, child_only=False):
    indent = "  " * level
    if isinstance(tree, TerminalNodeImpl):
        print(f"{indent}{tree.getText()}")
        return
    
    rule_name = parser.ruleNames[tree.getRuleIndex()]
    if not child_only:
        print(f"{indent}{rule_name}")
    
    for child in tree.children or []:
        pretty_print_tree(child, parser, level + 1, child_only=child_only)


# Stop hard coding just one input
if __name__ == "__main__":
    input_text = InputStream("3 + 4 * (2 - 1)\n")
    main(input_text)
