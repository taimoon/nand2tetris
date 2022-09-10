// push const 0
@0
D=A
@SP
A=M
M=D
@SP
M=M+1

// pop LCL 0
@LCL
D=M// D=LCL
@0
D=D+A// D=LCL+0=addr
@SP// *SP = addr+pos
A=M
M=D
@SP
AM=M-1// A = SP--
D=M// D = *SP
A=A+1// A = SP+1
A=M// A = *(SP+1) = addr
M=D// *addr = *SP

// label LOOP_START
(BasicLoop$LOOP_START)

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

// push LCL 0
@LCL
D=M// D=LCL
@0
A=D+A// A=LCL+0
D=M// D=*(LCL+0)
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

// pop LCL 0
@LCL
D=M// D=LCL
@0
D=D+A// D=LCL+0=addr
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

// if-goto LOOP_START
@SP
M=M-1// SP--
A=M// A=SP
D=M// D=*SP
@BasicLoop$LOOP_START
D;JNE // jump if not false (ie.: not equal to 0)

// push LCL 0
@LCL
D=M// D=LCL
@0
A=D+A// A=LCL+0
D=M// D=*(LCL+0)
@SP
A=M// A = SP
M=D// *SP = D
@SP
M=M+1// SP++