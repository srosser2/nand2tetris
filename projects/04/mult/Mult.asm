// This file is part of www.nand2tetris.org
// and the book "The Elements of Computing Systems"
// by Nisan and Schocken, MIT Press.
// File name: projects/04/Mult.asm

// Multiplies R0 and R1 and stores the result in R2.
// (R0, R1, R2 refer to RAM[0], RAM[1], and RAM[2], respectively.)
//
// This program only needs to handle arguments that satisfy
// R0 >= 0, R1 >= 0, and R0*R1 < 32768.

// Put your code here.

// Multiply 2 numbers in RAM[0] and RAM[1]
// initalize x, y, i
// while i > 0:
//     total = total + x
//     i--
// Store value in RAM[2]

    @total
    // reset total
    D=0
    M=D
    // Select RAM[1] and set i to value
    @R1
    D=M
    @i
    M=D

(LOOP)
    @i
    D=M
    // Jump out of the loop if i = 0;
    @STOP
    D;JEQ

    // Select RAM[0]
    @R0
    D=M
    // Total = total + RAM[0]
    @total
    D=D+M
    M=D

    // Decrease i by 1
    @i
    D=M-1
    M=D

    @LOOP
    0;JMP

(STOP)
    @total
    D=M
    @R2
    M=D

(END)
    @END
    0;JMP