// push ARG 1
@ARG
D=M// D=ARG
@1
A=D+A// A=ARG+1
D=M// D=*(ARG+1)
@SP
A=M// A = SP
M=D// *SP = D
@SP
M=M+1// SP++

// pop pointer 1
@SP
AM=M-1 // SP--
D=M// D=*SP
@THAT
M=D// THIS/THAT = *SP

// push const 0
@0
D=A
@SP
A=M
M=D
@SP
M=M+1

// pop THAT 0
@THAT
D=M// D=THAT
@0
D=D+A// D=THAT+0=addr
@SP// *SP = addr+pos
A=M
M=D
@SP
AM=M-1// A = SP--
D=M// D = *SP
A=A+1// A = SP+1
A=M// A = *(SP+1) = addr
M=D// *addr = *SP

// push const 1
@1
D=A
@SP
A=M
M=D
@SP
M=M+1

// pop THAT 1
@THAT
D=M// D=THAT
@1
D=D+A// D=THAT+1=addr
@SP// *SP = addr+pos
A=M
M=D
@SP
AM=M-1// A = SP--
D=M// D = *SP
A=A+1// A = SP+1
A=M// A = *(SP+1) = addr
M=D// *addr = *SP

// push ARG 0
@ARG
D=M// D=ARG
@0
A=D+A// A=ARG+0
D=M// D=*(ARG+0)
@SP
A=M// A = SP
M=D// *SP = D
@SP
M=M+1// SP++

// push const 2
@2
D=A
@SP
A=M
M=D
@SP
M=M+1

// arithmetic sub
@SP
AM=M-1// SP = SP--
D=M// D = *SP (second arg)
A=A-1// A = SP-1 (first arg)
MD=M-D// *SP + *(SP-1)

// pop ARG 0
@ARG
D=M// D=ARG
@0
D=D+A// D=ARG+0=addr
@SP// *SP = addr+pos
A=M
M=D
@SP
AM=M-1// A = SP--
D=M// D = *SP
A=A+1// A = SP+1
A=M// A = *(SP+1) = addr
M=D// *addr = *SP

// label MAIN_LOOP_START
(FibonacciSeries$MAIN_LOOP_START)

// push ARG 0
@ARG
D=M// D=ARG
@0
A=D+A// A=ARG+0
D=M// D=*(ARG+0)
@SP
A=M// A = SP
M=D// *SP = D
@SP
M=M+1// SP++

// if-goto COMPUTE_ELEMENT
@SP
M=M-1// SP--
A=M// A=SP
D=M// D=*SP
@FibonacciSeries$COMPUTE_ELEMENT
D;JNE // jump if not false (ie.: not equal to 0)

// goto END_PROGRAM
@FibonacciSeries$END_PROGRAM
0;JMP

// label COMPUTE_ELEMENT
(FibonacciSeries$COMPUTE_ELEMENT)

// push THAT 0
@THAT
D=M// D=THAT
@0
A=D+A// A=THAT+0
D=M// D=*(THAT+0)
@SP
A=M// A = SP
M=D// *SP = D
@SP
M=M+1// SP++

// push THAT 1
@THAT
D=M// D=THAT
@1
A=D+A// A=THAT+1
D=M// D=*(THAT+1)
@SP
A=M// A = SP
M=D// *SP = D
@SP
M=M+1// SP++

// arithmetic add
@SP
AM=M-1// SP = SP--
D=M// D = *SP (second arg)
A=A-1// A = SP-1 (first arg)
MD=M+D// *SP + *(SP-1)

// pop THAT 2
@THAT
D=M// D=THAT
@2
D=D+A// D=THAT+2=addr
@SP// *SP = addr+pos
A=M
M=D
@SP
AM=M-1// A = SP--
D=M// D = *SP
A=A+1// A = SP+1
A=M// A = *(SP+1) = addr
M=D// *addr = *SP

// push pointer 1
@THAT
D=M// D=THIS/THAT
@SP
A=M // A=SP
M=D// *SP = THIS/THAT
@SP
M=M+1// SP++

// push const 1
@1
D=A
@SP
A=M
M=D
@SP
M=M+1

// arithmetic add
@SP
AM=M-1// SP = SP--
D=M// D = *SP (second arg)
A=A-1// A = SP-1 (first arg)
MD=M+D// *SP + *(SP-1)

// pop pointer 1
@SP
AM=M-1 // SP--
D=M// D=*SP
@THAT
M=D// THIS/THAT = *SP

// push ARG 0
@ARG
D=M// D=ARG
@0
A=D+A// A=ARG+0
D=M// D=*(ARG+0)
@SP
A=M// A = SP
M=D// *SP = D
@SP
M=M+1// SP++

// push const 1
@1
D=A
@SP
A=M
M=D
@SP
M=M+1

// arithmetic sub
@SP
AM=M-1// SP = SP--
D=M// D = *SP (second arg)
A=A-1// A = SP-1 (first arg)
MD=M-D// *SP + *(SP-1)

// pop ARG 0
@ARG
D=M// D=ARG
@0
D=D+A// D=ARG+0=addr
@SP// *SP = addr+pos
A=M
M=D
@SP
AM=M-1// A = SP--
D=M// D = *SP
A=A+1// A = SP+1
A=M// A = *(SP+1) = addr
M=D// *addr = *SP

// goto MAIN_LOOP_START
@FibonacciSeries$MAIN_LOOP_START
0;JMP

// label END_PROGRAM
(FibonacciSeries$END_PROGRAM)