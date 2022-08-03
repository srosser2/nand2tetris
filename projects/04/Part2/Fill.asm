// 256 * 512
// 512 / 16 = 32 -> 32 16bit registers in a row
// 256 * 32 = 8192 -> all addresses

// Get total pixels
@8192
D=A
@total_pixels
M=D

// Get start of screen
@SCREEN
D=A
@start
M=D

// Get end
@SCREEN
D=A
@end
M=D
@total_pixels
D=M
@end
M=D+M

// set position
@start
D=M
@position
M=D

// ---- LOOP ----

// initialise i
@i
M=0

// number of iterations
@total_pixels
D=M
@limit
M=D

(LOOP)

// increase i
@i
M=M+1

// --- loop body start

// select current position and set to black
@color
D=M
M=D

@position
A=M
M=D

@position
M=M+1

// --- loop body end

@i
D=M
@limit
A=M
D=A-D

// Compare (limit - i) == 0
@LOOP
D;JGT

// Handle color
// SELECT KEYBOARD
// if KBD > 0, set color to white (0)
// else set color to black (-1)
@KBD
D=M

// JMP to black if keyboard val is greater than 1
@BLACK
D;JGT

// JMP to white if keyboard val is 0
@WHITE
D;JEQ

(BLACK)
@color
M=-1

@COLOR_SELECTED
0;JMP

(WHITE)
@color
M=0

@COLOR_SELECTED
0;JMP

// RELOOP
// set start postion to screen and jump to the start
(COLOR_SELECTED)

@start
D=M
@position
M=D

// Reset i
@i
M=0

@LOOP
0;JMP
