// initialise i
@i
M=0

// number of iterations
@20
D=A
@limit
M=D

(LOOP)

// increase i
@i
M=M+1

// iteration code here

@i
D=M
@limit
A=M
D=A-D

// Compare (limit - i) == 0
@LOOP
D;JGT
