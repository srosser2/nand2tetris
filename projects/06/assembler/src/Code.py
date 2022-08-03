class Code:
    def dec_to_bin(self, symbol):
        num = int(symbol)
        i = 15
        binary_str = ''
        while i >= 0:
            power = 2 ** i
            if (num >= power):
                num -= power
                binary_str += '1'
            else:
                binary_str += '0'
            i -= 1

        return binary_str

    def dest(self, mnemonic):
        valid_dests = {
            'M': '001',
            'D': '010',
            'MD': '011',
            'A': '100',
            'AM': '101',
            'AD': '110',
            'AMD': '111'
        }
        if mnemonic == None:
            return '000'

        if not mnemonic in valid_dests:
            raise Exception('Invalid dest mnemoic: ' + mnemonic)

        return valid_dests[mnemonic]
    
    def comp(self, mnemonic):
        valid_comps = {
            '0': '101010',
            '1': '111111',
            '-1': '111010',
            'D': '001100',
            'A': '110000',
            'M': '110000',
            '!D': '001101',
            '!A': '110001',
            '!M': '110001',
            '-D': '001111',
            '-A': '110011',
            '-M': '110011',
            'D+1': '011111',
            'A+1': '110111',
            'M+1': '110111',
            'D-1': '001110',
            'A-1': '110010',
            'M-1': '110010',
            'D+A': '000010',
            'D+M': '000010',
            'D-A': '010011',
            'D-M': '010011',
            'A-D': '000111',
            'M-D': '000111',
            'D&A': '000000',
            'D&M': '000000',
            'D|A': '010101',
            'D|M': '010101'
        }
        if not mnemonic in valid_comps:
            raise Exception('Invalid comp mnemoic: ' + mnemonic)
        
        a_bit = '1' if 'M' in mnemonic else '0'

        return a_bit + valid_comps[mnemonic]

    def jump(self, mnemonic):
        valid_jumps = {
            'JGT': '001',
            'JEQ': '010',
            'JGE': '011',
            'JLT': '100',
            'JNE': '101',
            'JLE': '110',
            'JMP': '111'
        }
        if mnemonic == None:
            return '000'

        elif not mnemonic in valid_jumps.keys():
            raise Exception('Invalid jump mnemoic: ' + mnemonic)
        
        else:
            return valid_jumps[mnemonic]
