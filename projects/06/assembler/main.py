import os
import sys
import re
from src.Parser import Parser, CommandType
from src.Code import Code
from src.SymbolTable import SymbolTable

def main():
    file_path = sys.argv[1]
    if not os.path.exists(file_path):
        raise Exception('File not found: ' + file_path)

    if not '.asm' in file_path:
        raise Exception('File must be .asm file format')

    file = open(file_path, 'r+')

    lines = file.readlines()

    parser = Parser(file)
    code = Code()
    symbol_table = SymbolTable()

    # Pass 1
    free_memory_index = 16
    rom_address = 0
    for line in lines:
        line = line.strip()
        cmd_type = parser.command_type(line)
    
        if cmd_type == CommandType.A_COMMAND or cmd_type == CommandType.C_COMMAND:
            rom_address += 1
        
        if cmd_type == CommandType.L_COMMAND:
            symbol = parser.symbol(line)
            symbol_table.add_entry(parser.symbol(line), rom_address)

    # Pass 2
    file.seek(0)
    # remove parent directories, remove .asm file exention, add hack extension
    output_filename = file.name.split('/')[-1].split('.')[0] + '.hack'
    output = open(output_filename, 'w+')

    for line in lines:
        line = line.strip()
        cmd_type = parser.command_type(line)

        if cmd_type == CommandType.A_COMMAND:
            sym = parser.symbol(line)
            dec = None
            if not sym.isdigit():
                if symbol_table.contains(sym):
                    dec = symbol_table.symbol_table[sym]
                else:
                    symbol_table.add_entry(sym, free_memory_index)
                    dec = symbol_table.symbol_table[sym]
                    free_memory_index += 1
            else:
                dec = int(sym)
            
            binary = code.dec_to_bin(dec)
            output.write(binary)
            output.write('\n')
        
        elif cmd_type == CommandType.C_COMMAND:
            comp = parser.comp(line)
            dest = parser.dest(line)
            jump = parser.jump(line)
            instruction = '111' + code.comp(comp) + code.dest(dest) + code.jump(jump)
            output.write(instruction)
            output.write('\n')

    file.close()
    output.close()

main()
