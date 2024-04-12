#Luna Lexer
import interpreter
from interpreter import command_line, string, function_name, tokens

'put.console >> "Hello World\n" >> '
[
    {
        tokens[0] == 'put.console'
    }
]
[
    {
        string[0] == 'Hello World'
    }
]
[
    {
        string[0] == 'Good Bye World'
    }
]
[
    {
        tokens[0] == 'FLOAT'
    }
]
[
    {
        string[0] == 'FLOAT = A'
    }
]
[
    {
        string[0] == 'FLOAT = X'
    }
]
[
    {
        string[0] == 'FLOAT = Y'
    }
]
[
    {
        tokens[0] == 'put.show_time'
    }
]
[
    [
        string[0] == 'Hello World'
    ]
]
[
    {
        string[0] == 'Good Bye World'
    }
]