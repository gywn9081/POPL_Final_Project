# POPL Final Project

Group: Group Name

## Authors
The Culbertson twins: Andrew and Kaden,
Harry Bloch, 
Justin Bowers


## Notes for running

Please note that the supplied (or default of `build/`) build directory must be on the PYTHONPATH variable since antlr4's outputs will be placed there. You can do this with echo PYTHONPATH=$PYTHONPATH:build/dir


#### Useful commands

GRAMMER_DIR="." make -f MakeFile

### Notes about white space

A newline ends a statement unless:
* You’re inside parentheses (), brackets [], or braces {}.
* The line ends with a backslash \ for line continuation.
* You’re inside a multiline string.
