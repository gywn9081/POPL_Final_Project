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

# def test_multiline_string():
#     tree, parser, lexer = parse_input("\"\n\n\ntest\n\n\n\"")
#     print(parser.getNumberOfSyntaxErrors())
#     assert tree is not None and parser.getNumberOfSyntaxErrors() == 0

#-----------------
# Comment test cases
#-----------------

# def test_basic_comment():
#     tree, parser = parse_input("#x=y\n")
#     assert tree is not None and parser.getNumberOfSyntaxErrors() == 0

# def test_multiple_hashtag():
#     tree, parser = parse_input("######tests\n")
#     assert tree is not None and parser.getNumberOfSyntaxErrors() == 0

# def test_string_comment_single():
#     tree, parser = parse_input("\'\'\'\n\ntesting\'\'\'")
#     assert tree is not None and parser.getNumberOfSyntaxErrors() == 0

# def test_string_comment_double():
#     tree, parser = parse_input("\"\"\"\n\ntesting\"\"\"")
#     assert tree is not None and parser.getNumberOfSyntaxErrors() == 0

# def test_string_comment_assignment():
#     tree, parser = parse_input("x=\"\"\"\n\n\"testing\"\"\"")
#     assert tree is not None and parser.getNumberOfSyntaxErrors() == 0

# ---------------------
# Negative test cases
# ---------------------

@pytest.mark.parametrize("input_text", [
    "\"\n\n\ntest\n\n\n\"", # incomplete expression
    "x=\"\"\"\n\n\"testing\"\"\"\"", # Unterminated string after three quotes
    "=",             # assignment without variable
    "x + = 5",       # invalid operator sequence
    "(2 + 3",        # missing closing parenthesis
    "x += (3 + )",   # incomplete expression inside parentheses
    "\"hi!\"x+2"
])
def test_invalid_syntax(input_text):
    _, parser = parse_input(input_text)
    assert parser.getNumberOfSyntaxErrors() > 0
    
@pytest.mark.parametrize("input_text", [
    "# Hello!\nx+1\nx+2",
    "\"\"\"Hello!\nHi!\"\"\"\nx+2"
])

def test_valid_syntax(input_text):
    _, parser = parse_input(input_text)
    assert parser.getNumberOfSyntaxErrors() == 0
    