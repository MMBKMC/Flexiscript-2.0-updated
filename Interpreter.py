def interpreter(parsed_code):
    variables = {}

    for instruction in parsed_code:
        if instruction[0] == 'SET':
            variables[instruction[1]] = instruction[2]
        elif instruction[0] == 'PRINT':
            print(variables.get(instruction[1], "Variable not found"))
        elif instruction[0] == 'IF':
            condition, if_block, else_block = instruction[1], instruction[2], instruction[3]
            if eval(condition, variables):
                for sub_instruction in if_block:
                    if sub_instruction[0] == 'PRINT':
                        print(sub_instruction[1])
                    elif sub_instruction[0] == 'SET':
                        variables[sub_instruction[1]] = sub_instruction[2]
            else:
                for sub_instruction in else_block:
                    if sub_instruction[0] == 'PRINT':
                        print(sub_instruction[1])
                    elif sub_instruction[0] == 'SET':
                        variables[sub_instruction[1]] = sub_instruction[2]
                    elif sub_instruction[0] == 'IMPORT':
                        variables[sub_instruction[1]] = sub_instruction[2]
                    elif sub_instruction[0] == 'Python':
                        variables[sub_instruction[1]] = sub_instruction[1]
                        format("The python command line is allow the python code.")
                    elif sub_instruction[0] == 'INT_MAIN':
                        variables[sub_instruction[1]] = sub_instruction[1]
                    elif sub_instruction[1] == 'CLASS':
                        variables[sub_instruction[1]] = sub_instruction[2]
                    elif sub_intruction[1] == 'CONSOLE':
                        varibles[sub_instruction[1]] = sub_intruction[2]
# Flexicode source code to be written into test.flc
flexicode_code = """
IMPORT Interpreter.py
IMPORT Lexer.py
IMPORT Parser.py

SET (10)
PRINT("Hello World!/n")

SET (10)
PRINT("Hello World!/n")
"""

# Write Flexicode code into test.flc file
with open('test.flc', 'w') as file:
    file.write(flexicode_code)

print("test.flc file has been created successfully.")

import sys
from Lexer import lexer
from Parser import parser
from Interpreter import interpreter

def read_flexicode_file(filename):
    with open(filename, 'r') as file:
        return file.read()

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python Interpreter.py <filename>")
        sys.exit(1)
    
    filename = sys.argv[1]

    # Read Flexicode code from the file
    code = read_flexicode_file(filename)

    # Tokenize, parse, and interpret the code
    tokens = lexer(code)
    parsed_code = parser(tokens)
    interpreter(parsed_code)

