class SymbolTable:
    def __init__(self):
        self.symbol_table = {
            'SP': 0,
            'LCL': 1,
            'ARG': 2,
            'THIS': 3,
            'THAT': 4,
            'R0': 0,
            'R1': 1,
            'R2': 2,
            'R3': 3,
            'R4': 4,
            'R5': 5,
            'R6': 6,
            'R7': 7,
            'R8': 8,
            'R9': 9,
            'R10': 10,
            'R11': 11,
            'R12': 12,
            'R13': 13,
            'R14': 14,
            'R15': 15,
            'SCREEN': 16384,
            'KBD': 24576
        }

    def add_entry(self, sym: str, address: int):
        self.symbol_table[sym] = address
    
    def contains(self, sym: str):
        return True if sym in self.symbol_table.keys() else False

    def get_address(self, sym: str):
        return self.symbol_table[sym]
