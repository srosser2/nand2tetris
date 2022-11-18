import sys
from src.CodeWriter import CodeWriter
from src.CommandType import CommandType
from src.Parser import Parser

def main():
    file_path = sys.argv[1]

    file = open(file_path, 'r+')

    lines = file.readlines()

    parser = Parser()
    code_writer = CodeWriter()

    # Set the stack pointer to 256
    output = (f'@256\n'
        'D=A\n'
        '@SP\n'
        'M=D\n')

    for line in lines:
        cmd = parser.clean_command(line)
        if not cmd:
            continue

        cmd_type = parser.command_type(cmd)

        if cmd_type == CommandType.C_ARITHMETIC:
            a = code_writer.write_arithmetic(cmd)
            output += a

        if cmd_type == CommandType.C_PUSH or cmd_type == CommandType.C_POP:
            a = code_writer.write_push_pop(cmd_type, parser.arg1(cmd), parser.arg2(cmd))
            output += a

    print(output)

    assembly_file = open("cpu-test.asm", "w")
    assembly_file.write(output)
    assembly_file.close()


main()
