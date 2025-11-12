# POPL Final Project

**Group:** Many Deers; One Headlight

## Authors

Harry Bloch,
Justin Bowers,
The Culbertson twins: Andrew and Kaden

## Setup

### Python Path Configuration

The build directory (default: `build/`) must be on your `PYTHONPATH` since ANTLR4 outputs are placed there.

```bash
export PYTHONPATH=$PYTHONPATH:build/
```

**Note:** The test files automatically include the parent directory in the path, so this may not be necessary when running tests.

## Building

Generate the ANTLR parser and lexer files:

```bash
GRAMMAR_DIR="." make -f Makefile
```

## Running Tests

Test files are organized by deliverable. Run tests from the project root directory:

```bash
pytest tests/deliverable1.py
```

For verbose output:

```bash
pytest tests/deliverable1.py -v
```

## Language Specification

### Whitespace Rules

A newline ends a statement **unless**:

- You're inside parentheses `()`, brackets `[]`, or braces `{}`
- The line ends with a backslash `\` for line continuation
- You're inside a multiline string

This means that to accomplish python like whitespace you will need to issue indent and dedent tokens.

References (most to least useful):
1. https://docs.python.org/3/reference/compound_stmts.html#grammar-token-suite
2. https://github.com/no-context/moo/issues/55
3. https://discuss.python.org/t/indentation-is-important/19835

---

## Project Structure

The following was obtained from this tree command `tree -L 2 -I '__pycache__|*.pyc'`

```
.
├── build/          # ANTLR-generated files
├── src
│   ├── grammars    # g4 files used by ANTLR
│   └── /           # Files to run deliverable g4 with input
├── tests/          # Test files organized by deliverable
├── Makefile        # Build configuration
├── requirements.txt # Project requirements file t install
└── readme.md
```
