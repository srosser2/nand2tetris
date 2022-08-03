// Multiply R0 by R1 and Save the value in R2
// Clear R2 by seeting it to 0
@R2
M=0
// Setup i as R1
@R1
D=M
@i
M=D
(LOOP)
// Select value from R0 and add it to R2
@R0
D=M
@R2
M=D+M
// Subtract 1 from i and keep looping while greater than 0
@i
M=M-1
D=M
@LOOP
D;JGT

(END)
@END
0;JMP