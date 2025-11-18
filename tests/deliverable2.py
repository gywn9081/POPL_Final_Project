# The following was taken from deliverable 1 tests file
import pytest
import sys
from pathlib import Path

# Add the parent directory to sys.path
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))


from antlr4 import InputStream, CommonTokenStream
from build.ArithmeticLexer import ArithmeticLexer
from build.ArithmeticParser import ArithmeticParser

# Helper function to parse input; raises exception on errors
def parse_input(input_text):
    lexer = ArithmeticLexer(InputStream(input_text))
    stream = CommonTokenStream(lexer)
    parser = ArithmeticParser(stream)
    parser.buildParseTrees = True
    tree = parser.start()
    return tree, parser


# ---------------------
# Positive test cases
# ---------------------

def test_simple_addition():
    tree, parser = parse_input("3 + 4")
    assert tree is not None and parser.getNumberOfSyntaxErrors() == 0

#--------------------
# String test cases
#--------------------

def test_empty_string():
    tree, parser = parse_input("")
    assert tree is not None and parser.getNumberOfSyntaxErrors() == 0

def test_multiline_string():
    tree, parser = parse_input("\n\n\ntest\n\n\n")
    assert tree is not None and parser.getNumberOfSyntaxErrors() == 0

# ---------------------
# Negative test cases
# ---------------------

@pytest.mark.parametrize("input_text", [
    "3 +",           # incomplete expression
    "* 4",           # operator without left operand
    "=",             # assignment without variable
    "x + = 5",       # invalid operator sequence
    "(2 + 3",        # missing closing parenthesis
    "x += (3 + )",   # incomplete expression inside parentheses
])
def test_invalid_syntax(input_text):
    _, parser = parse_input(input_text)
    assert parser.getNumberOfSyntaxErrors() > 0
