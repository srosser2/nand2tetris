from src.CommandType import CommandType

class Parser:
    def __init__(self):
        pass

    def command_type(self, command: str) -> CommandType:
        type = command.split()[0]

        if type == 'push':
            return CommandType.C_PUSH

        if type == 'pop':
            return CommandType.C_POP

        if type in ['add', 'sub', 'eq', 'lt', 'gt', 'neg', 'and', 'or', 'not']:
            return CommandType.C_ARITHMETIC

    def arg1(self, command: str) -> str:
        cmd_type = self.command_type(command)
        cmd_tokens = command.split()
        
        if cmd_type == CommandType.C_ARITHMETIC:
            return cmd_tokens[0]
        
        return cmd_tokens[1]
    
    def arg2(self, command: str) -> str:
        cmd_type = self.command_type(command)
        cmd_tokens = command.split()
        
        if cmd_type == CommandType.C_ARITHMETIC:
            return None
        
        return cmd_tokens[2]

    def clean_command(self, line):
        line = line.split('//')[0]
        return line.strip()
