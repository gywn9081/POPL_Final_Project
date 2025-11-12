# This file will be the one that runs all of the outputs from antlr4
# import sys

# # Add the parent directory to sys.path
# project_root = Path(__file__).parent.parent
# sys.path.insert(0, str(project_root))

from antlr4 import InputStream, CommonTokenStream
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
    # input_text = "array1 = [1, 2, 3, 4, 5]"
    with open("./tests/deliverable1_tests.txt", "r", encoding="utf-8") as file:
        input_text = file.read()
    input_text = InputStream(input_text)
    main(input_text)
