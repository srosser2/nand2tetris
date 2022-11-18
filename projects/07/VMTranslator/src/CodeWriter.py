from src.CommandType import CommandType

class CodeWriter:
    SP = 0
    LCL = 1015
    ARGUMENT = 0
    THIS = 0
    THAT = 0
    CONSTANT = 0
    STATIC = 16
    TEMP = 5
    POINTER = 0

    def __init__(self):
        self.instruction_count = 0

    def map_memory(self):
        return(f'// map memory\n'
        '@SP\n'
        'M=256\n'
        '@LCL\n'
        'M=300\n'
        '@ARG\n'
        'M=400\n'
        '@THIS\n'
        'M=3000\n'
        '@THAT\n'
        'M=3010\n'
        )

    def set_file_name(self, file_name: str):
        pass
    
    def write_arithmetic(self, command: str):
        # True is represented by -1 and False is represented by 0
        if command == 'add':
            assembly_string = '// add\n'
            assembly_string += self.pop_to_d_register()
            assembly_string += self.pop_to_m_register()
            assembly_string += (f'M=D+M\n'
            '@SP\n'
            'M=M+1\n'
            )
            return assembly_string
        if command == 'sub':
            assembly_string = '// sub\n'
            assembly_string += self.pop_to_d_register()
            assembly_string += self.pop_to_m_register()
            assembly_string += (f'M=M-D\n'
            '@SP\n'
            'M=M+1\n'
            )
            return assembly_string
        if command == 'eq':
            self.instruction_count += 1
            
            assembly_string = '// eq\n'

            assembly_string += self.pop_to_d_register()
            assembly_string += self.pop_to_m_register()

            assembly_string += (
                'D=M-D\n'
                f'@SET_TRUE_{self.instruction_count}\n'
                'D;JEQ\n'
                f'@SET_FALSE_{self.instruction_count}\n'
                '0;JMP\n'
            )

            assembly_string += (
                f'(SET_TRUE_{self.instruction_count})\n'
                '@SP\n'
                'A=M\n'
                'M=-1\n'
                '@SP\n'
                'M=M+1\n'
                f'@CONTINUE_{self.instruction_count}\n'
                '0;JMP\n'

                f'(SET_FALSE_{self.instruction_count})\n'
                '@SP\n'
                'A=M\n'
                'M=0\n'
                '@SP\n'
                'M=M+1\n'
                f'@CONTINUE_{self.instruction_count}\n'
                '0;JMP\n'

                f'(CONTINUE_{self.instruction_count})\n'
            )

            return assembly_string
        if command == 'lt':
            self.instruction_count += 1
            
            assembly_string = '// eq\n'

            assembly_string += self.pop_to_d_register()
            assembly_string += self.pop_to_m_register()

            assembly_string += (
                'D=M-D\n'
                f'@SET_TRUE_{self.instruction_count}\n'
                'D;JLT\n'
                f'@SET_FALSE_{self.instruction_count}\n'
                '0;JMP\n'
            )

            assembly_string += (
                f'(SET_TRUE_{self.instruction_count})\n'
                '@SP\n'
                'A=M\n'
                'M=-1\n'
                '@SP\n'
                'M=M+1\n'
                f'@CONTINUE_{self.instruction_count}\n'
                '0;JMP\n'

                f'(SET_FALSE_{self.instruction_count})\n'
                '@SP\n'
                'A=M\n'
                'M=0\n'
                '@SP\n'
                'M=M+1\n'
                f'@CONTINUE_{self.instruction_count}\n'
                '0;JMP\n'

                f'(CONTINUE_{self.instruction_count})\n'
            )

            return assembly_string
        if command == 'gt':
            self.instruction_count += 1
            
            assembly_string = '// eq\n'

            assembly_string += self.pop_to_d_register()
            assembly_string += self.pop_to_m_register()

            assembly_string += (
                'D=M-D\n'
                f'@SET_TRUE_{self.instruction_count}\n'
                'D;JGT\n'
                f'@SET_FALSE_{self.instruction_count}\n'
                '0;JMP\n'
            )

            assembly_string += (
                f'(SET_TRUE_{self.instruction_count})\n'
                '@SP\n'
                'A=M\n'
                'M=-1\n'
                '@SP\n'
                'M=M+1\n'
                f'@CONTINUE_{self.instruction_count}\n'
                '0;JMP\n'

                f'(SET_FALSE_{self.instruction_count})\n'
                '@SP\n'
                'A=M\n'
                'M=0\n'
                '@SP\n'
                'M=M+1\n'
                f'@CONTINUE_{self.instruction_count}\n'
                '0;JMP\n'

                f'(CONTINUE_{self.instruction_count})\n'
            )

            return assembly_string
        if command == 'neg':
            assembly_string = '// neg\n'
            assembly_string += self.pop_to_d_register()
            assembly_string += (f'D=-D\n'
                '@SP\n'
                'A=M\n'
                'M=D\n'
                '@SP\n'
                'M=M+1\n'
            )
            return assembly_string

        if command == 'and':
            assembly_string = '// and\n'
            assembly_string += self.pop_to_d_register()
            assembly_string += self.pop_to_m_register()
            assembly_string += (f'M=D&M\n'
                '@SP\n'
                'M=M+1\n'
            )
            return assembly_string
        if command == 'or':
            assembly_string = '// or\n'
            assembly_string += self.pop_to_d_register()
            assembly_string += self.pop_to_m_register()
            assembly_string += (f'M=D|M\n'
                '@SP\n'
                'M=M+1\n'
            )
            return assembly_string
        if command == 'not':
            assembly_string = '// not\n'
            assembly_string += self.pop_to_m_register()
            assembly_string += (f'M=!M\n'
                '@SP\n'
                'M=M+1\n'
            )
            return assembly_string

    def write_push_pop(self, command: str, segment: str, index: int):
        if command == CommandType.C_PUSH:
           return self.__handle_push_command(segment, index)

    def __handle_push_command(self, segment: str, index: int):
        if segment == 'constant':
            return (f'// push constant {index}\n'
                f'@{index}\n'
                'D=A\n'
                '@SP\n'
                'A=M\n'
                'M=D\n'
                '@SP\n'
                'M=M+1\n'
            )

    def pop_to_d_register(self):
        return (f'@SP\n'
            'M=M-1\n'
            'A=M\n'
            'D=M\n'
            )

    def pop_to_m_register(self):
        return (f'@SP\n'
            'M=M-1\n'
            'A=M\n'
            )
