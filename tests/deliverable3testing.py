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
    # a preprocessor function to make indenting and dedenting easier
    input_text = indent_dedent_function(input_text)
    lexer = ArithmeticLexer(InputStream(input_text))
    stream = CommonTokenStream(lexer)
    parser = ArithmeticParser(stream)
    parser.buildParseTrees = True
    tree = parser.start()
    return tree, parser

def indent_dedent_function(input_text):
    # so that we have a list of lines, not including the newline or \r whatever that does
    input_text_list = input_text.splitlines()
    output_text_list = []
    current_indent = 0
    for input_text_line in input_text_list:
        # we should not care about lines that are stripped or that have a hashtag cause its a comment
        if not input_text_line.strip() or input_text_line.strip()[0] == "#":
            output_text_list.append(input_text_line)
            continue
        
        indent_count = 0
        # counts the number of indents (since space is one and tab is 4)
        for i in input_text_line:
            if i == '\t':
                indent_count += 4
            elif i == ' ':
                indent_count += 1
            else:
                break
        
        if indent_count % 4 != 0:
            print("evil ahh tabing") # TODO prob change this lol
            sys.exit(1)

        indent_change = indent_count - current_indent

        indent_change = indent_change / 4

        if indent_change < 0:
            output_text_list.append('<dedent>')
        elif indent_change > 0:
            output_text_list.append('<indent>')
        
        output_text_list.append(input_text_line)

        current_indent = indent_count
        
    while(current_indent > 0):
        output_text_list.append('<dedent>')
        current_indent-=4
    
    print('\n'.join(output_text_list))

    return '\n'.join(output_text_list)

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
    "if(True):\n\tx=1\n\ty=2\n",  
    "if(True):\n\tx=1\n\ty=2\n\tif(False):\n\t\tz=3\n\tb=4\n\t\tg=4\n\t"
])

def test_valid_syntax(input_text):
    _, parser = parse_input(input_text)
    assert parser.getNumberOfSyntaxErrors() == 0
    