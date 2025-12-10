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

if len(sys.argv) != 2:
    print(f"Usage: {sys.argv[0]} <text_to_test.txt>")
    sys.exit(1)

with open(sys.argv[1], "r", encoding="utf-8") as f:
    input_text = f.read()

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
            print("Error. Expected tab spacing amount to use a multiple of 4.")
            sys.exit(1)

        indent_change = indent_count - current_indent

        indent_change = indent_change / 4
        
        current_indent = indent_count
        while indent_change != 0:
            if indent_change < 0:
                output_text_list.append('<debang>')
                indent_change += 1
            elif indent_change > 0:
                output_text_list.append('<bang>')
                indent_change -= 1
        
        output_text_list.append(input_text_line)

        
    while(current_indent > 0):
        output_text_list.append('<debang>')
        current_indent-=4
    
    return '\n'.join(output_text_list)

# a preprocessor function to make indenting and dedenting easier
input_text = indent_dedent_function(input_text)
lexer = ArithmeticLexer(InputStream(input_text))
stream = CommonTokenStream(lexer)
parser = ArithmeticParser(stream)
parser.buildParseTrees = True # ! Delete later
tree = parser.start() # ! Delete later