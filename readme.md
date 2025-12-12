# POPL Final Project

## Project Explanation
This project parses Python3 code for specific features, including arithmetic operators, assignment operators, if/elif/else blocks, conditional statements, for/while loops, nested structures, and comments using Python3 and Antlr4. The text file is first put into a python function, which adds indent and dedent text so that the lexer can tokenize indentation (which is not context-free). The new text is then handed off to the Antlr grammar, which then tokenizes and parses the text based on the rules in the Arithmetic.g4 file.

## **Group:** Many Deers; One Headlight

## Authors

Justin Bowers,
Henry Bloch,
Kaden Culbertson,
and Andrew Culbertson

## Requirements

 - Python 3.10 or later (https://www.python.org/downloads/)

 - run $ pip install -r requirements.txt

## How To Run

1. $ cd tests

2. $ antlr4 -Dlanguage=Python3 ../src/grammars/Arithmetic.g4

3. $ python deliverable3.py <text_to_test.txt/.py>

(ex. $ python deliverable3.py deliverable_3.txt or $ python deliverable3.py project_deliverable_3.py)

## How To Get Parse Tree

1. $ cd tests

2. $ python indentation_parse_tree.py <text_to_parse.txt/.py>

(ex. $ python indentation_parse_tree.py deliverable_3.txt or $ python indentation_parse_tree.py project_deliverable_3.py)

3. $ antlr4-parse ../src/grammars/Arithmetic.g4 start -tree -gui tree_input.txt

If you would like more info on installing and running, please feel free to contact us or check out our Github:
https://github.com/gywn9081/POPL_Final_Project
