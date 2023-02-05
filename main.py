import logging
from lark import Lark, logger

logger.setLevel(logging.DEBUG)

grammar_file = open("grammar.ebnf", "r")
grammar = grammar_file.read()

imp_parser = Lark(grammar, start='command', parser='lalr', debug=True)
grammar_file.close()

sample_prog_file = open("sample_prog.imp", "r")
sample_prog = sample_prog_file.read()

ast = imp_parser.parse(sample_prog)
print(ast)
print(ast.pretty())
