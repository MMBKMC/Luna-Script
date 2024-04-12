import interpreter
import sys 
from interpreter import*

tokens[0] == 'put.console'
command_line[1] == 'put.console >> "Hello World/n" >>'
command_line[2] == '/n'
function_name[tokens] == (command_line)

string[0] == 'Hello World'
command_line[1] == 'put.console >> "Hello World/n" >> '
command_line[2] == 'X = Hello World'
command_line[3] == 'Y = Hello World'
command_line[4] == 'A = Hello World'
function_name[tokens] == (command_line)

string[0] == 'Good Bye World'
command_line[1] == 'put.console >> "Good Bye World/n" >> '
command_line[2] == 'X = Good Bye World'
command_line[3] == 'Y = Good Bye World'
command_line[4] == 'A = Hello World'

tokens[0] == 'int main()'
command_line[1] == 'int main()'
function_name[tokens] == (command_line)

tokens[0] == 'X'
command_line[1] == 'X = '
function_name[tokens] == (command_line)

tokens[0] == 'Y'
command_line[1] == 'Y = '
function_name[tokens] == (command_line)

tokens[0] == 'A '
command_line[1] == 'A = '
function_name[tokens] == (command_line)

tokens[0] == 'FLOAT '
command_line[1] == 'FLOAT = A'
command_line[2] == 'FLOAT = X'
command_line[3] == 'FLOAT = Y'
function_name[tokens] == (command_line)

tokens[0] == 'put.show_times'
command_line[1] == 'put.show_time("/n")'
function_name[tokens] == (command_line)

string[0] == 'Hello World'
command_line[1] == 'put.show_time(*number* "Hello World/n")'
function_name[tokens] == (command_line)

string[0] == 'Good Bye World'
command_line[1] == 'put.show_time(*number* "Good Bye World/n")'
function_name[tokens] == (command_line)

tokens[0] == 'import'
command_line[1] == 'import <*imports*>'
function_name[tokens] == (command_line)

string[0] == 'os'
command_line[1] == 'import <os>'
function_name[tokens] == (command_line)

string[0] == 'sys'
command_line[1] == 'import <sys>'
function_name[tokens] == (command_line)

string[0] == 'studio.py'
command_line[1] == 'import <studio.py>'
function_name[tokens] == (command_line)

string[0] == 'interpreted.py'
command_line[1] == 'import <interpreted.py>'
function_name[tokens] == (command_line)

string[0] == 'studio.py'
command_line[1] == 'import <studio>'
function_name[tokens] == (command_line)

tokens[0] == 'std::read'
command_line[1] == 'std::read >> "/n" >>'
function_name[tokens] == (command_line)

string[0] == 'LunaMaths'
command_line[1] == 'import <LunaMaths>'
function_name[tokens] == (command_line)

tokens[0] == 'bits'
command_line[1] == 'bits x'
string[1] == '16'
function_name[tokens] == (command_line)