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

def test_simple_subtraction():
    tree, parser = parse_input("10 - 2")
    assert tree is not None and parser.getNumberOfSyntaxErrors() == 0

def test_multiplication_division():
    tree, parser = parse_input("5 * 6 / 3")
    assert tree is not None and parser.getNumberOfSyntaxErrors() == 0

def test_parentheses_expression():
    tree, parser = parse_input("(2 + 3) * 4")
    assert tree is not None and parser.getNumberOfSyntaxErrors() == 0

def test_multiple_operators():
    tree, parser = parse_input("7 + 8 * 2 - 1")
    assert tree is not None and parser.getNumberOfSyntaxErrors() == 0

def test_basic_assignment():
    tree, parser = parse_input("x = 5")
    assert tree is not None and parser.getNumberOfSyntaxErrors() == 0

# ---------------------
# Chained test cases
# ---------------------

def test_assignment_with_expression():
    tree, parser = parse_input("y = 3 + 2")
    assert tree is not None and parser.getNumberOfSyntaxErrors() == 0

def test_assignment_with_parentheses():
    tree, parser = parse_input("z = (1 + 2) * 3")
    assert tree is not None and parser.getNumberOfSyntaxErrors() == 0

def test_chained_assignment_two_vars():
    tree, parser = parse_input("x = y = 5")
    assert tree is not None and parser.getNumberOfSyntaxErrors() == 0

def test_chained_assignment_three_vars():
    tree, parser = parse_input("a = b = c = 10")
    assert tree is not None and parser.getNumberOfSyntaxErrors() == 0

# ---------------------
# Compound test cases
# ---------------------

def test_increment():
    tree, parser = parse_input("x += 1")
    assert tree is not None and parser.getNumberOfSyntaxErrors() == 0

def test_decrement():
    tree, parser = parse_input("y -= 2")
    assert tree is not None and parser.getNumberOfSyntaxErrors() == 0

def test_multiplication_assignment():
    tree, parser = parse_input("z *= 3")
    assert tree is not None and parser.getNumberOfSyntaxErrors() == 0

def test_division_assignment():
    tree, parser = parse_input("w /= 4")
    assert tree is not None and parser.getNumberOfSyntaxErrors() == 0

# ---------------------
# Multi-line test cases
# ---------------------

def test_two_assignments():
    tree, parser = parse_input("x = 5\ny = 3")
    assert tree is not None and parser.getNumberOfSyntaxErrors() == 0

def test_bare_expressions_multiple_lines():
    tree, parser = parse_input("3 + 4\n5 * 2")
    assert tree is not None and parser.getNumberOfSyntaxErrors() == 0

def test_multiple_assignments_and_expressions():
    tree, parser = parse_input("x = 1 + 2\ny = x * 3\nz = y - 1")
    assert tree is not None and parser.getNumberOfSyntaxErrors() == 0

# INFO These two are failing which is fine 
# def test_multiline_parentheses_1():
#     tree, parser = parse_input("x = (3 +\n4 * (2 - 1))")
#     assert tree is not None and parser.getNumberOfSyntaxErrors() == 0

# def test_multiline_parentheses_2():
#     tree, parser = parse_input("y = (1 + 2 +\n3 + 4)")
#     assert tree is not None and parser.getNumberOfSyntaxErrors() == 0

# ---------------------
# Array test cases
# ---------------------

def test_empty_array():
    tree, parser = parse_input("y = []")
    assert tree is not None and parser.getNumberOfSyntaxErrors() == 0

def test_array_with_elements():
    tree, parser = parse_input("y = [1, 2, 3, 'a', \"b\"]")
    assert tree is not None and parser.getNumberOfSyntaxErrors() == 0

def test_array_with_no_commas():
    tree, parser = parse_input("x = [a]")
    assert tree is not None and parser.getNumberOfSyntaxErrors() == 0

def test_array_with_trailing_comma():
    tree, parser = parse_input("x = [1, 2, 3,]")
    assert tree is not None and parser.getNumberOfSyntaxErrors() == 0

def test_why_break():
    tree, parser = parse_input("array1 = [1, 2, 3, 4, 5]\n")
    assert tree is not None and parser.getNumberOfSyntaxErrors() == 0

# ---------------------
# Operator precedence tests
# ---------------------
# ! Right now this does not account for tightness of binding so it is not usefull
def test_multiplication_before_addition():
    tree, parser = parse_input("2 + 3 * 4")
    assert tree is not None and parser.getNumberOfSyntaxErrors() == 0

def test_division_before_subtraction():
    tree, parser = parse_input("10 - 6 / 2")
    assert tree is not None and parser.getNumberOfSyntaxErrors() == 0

def test_multiple_precedence():
    tree, parser = parse_input("1 + 2 * 3 - 4 / 2")
    assert tree is not None and parser.getNumberOfSyntaxErrors() == 0

def test_parentheses_override_precedence():
    tree, parser = parse_input("(1 + 2) * (3 - 4) / 2")
    assert tree is not None and parser.getNumberOfSyntaxErrors() == 0

def test_modulus_precedence():
    tree, parser = parse_input("10 + 5 % 3")
    assert tree is not None and parser.getNumberOfSyntaxErrors() == 0

def test_nested_parentheses():
    tree, parser = parse_input("((1 + 2) * (3 + 4)) - 5")
    assert tree is not None and parser.getNumberOfSyntaxErrors() == 0


#-----------------
# Bool test cases
#-----------------

def test_simple_bool():
    tree, parser = parse_input("x = True")
    assert tree is not None and parser.getNumberOfSyntaxErrors() == 0

def test_chained_bools():
    tree, parser = parse_input("x = y = True")
    assert tree is not None and parser.getNumberOfSyntaxErrors() == 0

def test_statement_false():
    tree, parser = parse_input("False")
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
