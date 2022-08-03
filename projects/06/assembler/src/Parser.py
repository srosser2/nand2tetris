from enum import Enum
import re

class CommandType(Enum):
    A_COMMAND = 1
    C_COMMAND = 2
    L_COMMAND = 3

class Parser:
    def __init__(self, file):
        pass
    
    def has_more_commands(self, line):
        return line[-1] != '\n'

    def advance():
        pass
    
    def command_type(self, instruction: str) -> CommandType:
        if (self.__should_be_ignored(instruction)):
            return

        if (self.__is_a_instruction(instruction)):
            return CommandType.A_COMMAND

        if (self.__is_c_instruction(instruction)):
            return CommandType.C_COMMAND
        
        if (self.__is_l_instruction(instruction)):
            return CommandType.L_COMMAND

    def symbol(self, instruction: str):
        regex = '(?<=\().*?(?=\))'
        if instruction[0] == '@':
            return instruction[1::]
        elif re.search(regex, instruction):
            return re.search(regex, instruction).group(0)

    def dest(self, instruction: str):
        assignment_operator = self.__index_of('=', instruction)
        if (assignment_operator > 0):
            return instruction[0:assignment_operator:]
        return

    def comp(self, instruction: str):
        comp_instruction = instruction

        if self.__index_of('=', instruction) > 0:
            comp_instruction = comp_instruction.split('=')[1]
        
        if self.__index_of(';', instruction) > 0:
            comp_instruction = comp_instruction.split(';')[0]
        
        return comp_instruction

    def jump(self, instruction: str):
        if self.__index_of(';', instruction) > 0:
           return instruction.split(';')[1]

    # Private methods
    def __is_a_instruction(self, instruction: str) -> bool:
        if (instruction[0] == '@'):
            return True

    def __is_c_instruction(self, instruction: str) -> bool:
        regex = '^[(A|M|D){1,2}]+=[(A|M|D|0|\-|\!){1,2}]|^[(A|M|D|0)];'
        if (re.search(regex, instruction)):
            return True

    def __is_l_instruction(self, instruction: str) -> bool:
        if (self.__index_of('(', instruction)) == 0 and instruction[-1] == ')':
            return True
    
    def __should_be_ignored(self, instruction: str) -> bool:
        if (
            len(instruction) == 0
            or instruction == '\n'
            or instruction == '\r\n'
            or instruction[:2] == '//'
        ):
            return True

    def __index_of(self, token: str, string: str) -> int:
        return string.index(token) if token in string else -1
