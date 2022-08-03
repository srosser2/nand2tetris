// This file is part of www.nand2tetris.org
// and the book "The Elements of Computing Systems"
// by Nisan and Schocken, MIT Press.
// File name: projects/04/Fill.asm

// Runs an infinite loop that listens to the keyboard input.
// When a key is pressed (any key), the program blackens the screen,
// i.e. writes "black" in every pixel;
// the screen should remain fully black as long as the key is pressed. 
// When no key is pressed, the program clears the screen, i.e. writes
// "white" in every pixel;
// the screen should remain fully clear as long as no key is pressed.

// Put your code here.

// 256 * 512
// 512 / 16 = 32 -> 32 16bit registers in a row
// 256 * 32 = 8192 -> all address

(START)
    // set RAM[16] to screen address 
    @SCREEN
    M=D
    D=A
    @addr // RAM16
    M=D

    // set RAM[17] to total screen addr
    @8192
    D=A
    @n
    M=D

    // set RAM[18] to i
    @0
    D=A
    @i
    M=D

    // set RAM[19] to fill to blank
    @fill
    M=0

    // SELECT KEY
    @KBD
    D=M

(BLACK) // set fill to black and jump to start of loop
    @fill
    M=-1
    @LOOP
    0;JMP

(WHITE) // set fill to white and jump to start of loop
    // resset RAM[17] to total screen addr
    @8192
    D=A
    @n
    M=D

    // reset addr
    @SCREEN
    D=A
    @addr
    M=D

    // set fill to 0
    @fill
    M=0
    @LOOP
    0;JMP

(LOOP)
    // Check if n = 0 (all screen has been covered)
    @n
    D=M
    @END
    D;JEQ // Does n = 0?
    
    @addr
    D=M
    M=D

    @fill
    D=M

    @addr
    A=M
    M=D

    @addr
    D=M
    M=D+1
    
    @n
    D=M
    M=D-1


    // LOOP TO KEY CHOICE
    // Decide whether to go to WHITE or BLACK
    // set D to keyboard value
    @KBD
    D=M

    @BLACK
    D;JGT // if greater than 0 - key is pressed

    @WHITE
    D;JEQ // if equal 0

(END)
    @KBD
    D=M
    @WHITE
    D;JEQ
    @END
    0;JMP
