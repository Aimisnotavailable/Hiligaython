from scripts.parser import Parser
from scripts.lexer import Lexer
from scripts.executor import Executor
from scripts.builtins import Builtins

lexer = Lexer()
while True:
    input_str = input(">> ")

    if input_str.strip() == "exit":
        print("Pagsira.")
        break

    print(lexer.tokenize(input_str))
    
'Ini amo ang hiligaynon .'