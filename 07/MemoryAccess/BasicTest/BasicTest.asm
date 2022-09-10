@10 // A = val
    D=A
    @SP // A = SP
    A=M // A = RAM[A]
    M=D // RAM[A] = D
    @SP // A = SP
    M=M+1// SP++
@LCL
        D=M// D=LCL
        @0
        D=D+A// D=LCL+0=addr
        @SP
        M=M-1// SP--
        A=M+1// A = SP+1
        M=D// *(SP+1) = addr
        @SP
        A=M// A = SP
        D=M// D = *SP
        @SP
        A=M+1// A = SP+1
        A=M// A = *(SP+1) = addr
        M=D// *addr = *SP
@21 // A = val
    D=A
    @SP // A = SP
    A=M // A = RAM[A]
    M=D // RAM[A] = D
    @SP // A = SP
    M=M+1// SP++
@22 // A = val
    D=A
    @SP // A = SP
    A=M // A = RAM[A]
    M=D // RAM[A] = D
    @SP // A = SP
    M=M+1// SP++
@ARG
        D=M// D=ARG
        @2
        D=D+A// D=ARG+2=addr
        @SP
        M=M-1// SP--
        A=M+1// A = SP+1
        M=D// *(SP+1) = addr
        @SP
        A=M// A = SP
        D=M// D = *SP
        @SP
        A=M+1// A = SP+1
        A=M// A = *(SP+1) = addr
        M=D// *addr = *SP
@ARG
        D=M// D=ARG
        @1
        D=D+A// D=ARG+1=addr
        @SP
        M=M-1// SP--
        A=M+1// A = SP+1
        M=D// *(SP+1) = addr
        @SP
        A=M// A = SP
        D=M// D = *SP
        @SP
        A=M+1// A = SP+1
        A=M// A = *(SP+1) = addr
        M=D// *addr = *SP
@36 // A = val
    D=A
    @SP // A = SP
    A=M // A = RAM[A]
    M=D // RAM[A] = D
    @SP // A = SP
    M=M+1// SP++
@THIS
        D=M// D=THIS
        @6
        D=D+A// D=THIS+6=addr
        @SP
        M=M-1// SP--
        A=M+1// A = SP+1
        M=D// *(SP+1) = addr
        @SP
        A=M// A = SP
        D=M// D = *SP
        @SP
        A=M+1// A = SP+1
        A=M// A = *(SP+1) = addr
        M=D// *addr = *SP
@42 // A = val
    D=A
    @SP // A = SP
    A=M // A = RAM[A]
    M=D // RAM[A] = D
    @SP // A = SP
    M=M+1// SP++
@45 // A = val
    D=A
    @SP // A = SP
    A=M // A = RAM[A]
    M=D // RAM[A] = D
    @SP // A = SP
    M=M+1// SP++
@THAT
        D=M// D=THAT
        @5
        D=D+A// D=THAT+5=addr
        @SP
        M=M-1// SP--
        A=M+1// A = SP+1
        M=D// *(SP+1) = addr
        @SP
        A=M// A = SP
        D=M// D = *SP
        @SP
        A=M+1// A = SP+1
        A=M// A = *(SP+1) = addr
        M=D// *addr = *SP
@THAT
        D=M// D=THAT
        @2
        D=D+A// D=THAT+2=addr
        @SP
        M=M-1// SP--
        A=M+1// A = SP+1
        M=D// *(SP+1) = addr
        @SP
        A=M// A = SP
        D=M// D = *SP
        @SP
        A=M+1// A = SP+1
        A=M// A = *(SP+1) = addr
        M=D// *addr = *SP
@510 // A = val
    D=A
    @SP // A = SP
    A=M // A = RAM[A]
    M=D // RAM[A] = D
    @SP // A = SP
    M=M+1// SP++
@5
    D=A
    @6
    D=A+D// A = addr = 5 + val
    @SP
    M=M-1// SP--
    A=M+1// A = SP+1
    M=D// *(SP+1) = addr
    @SP
    A=M// A=SP
    D=M// D=*SP
    @SP
    A=M+1// A = SP+1
    A=M// A = *(SP+1) = addr
    M=D// *addr = *SP
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
@THAT
        D=M// D=THAT
        @5
        A=D+A// A=THAT+5
        D=M// D=*(THAT+5)
        @SP
        A=M// A = SP
        M=D// *SP = D
        @SP
        M=M+1// SP++
@SP
            M=M-1// SP = SP--
            A=M// A = SP
            D=M// D = *SP (second arg)
            A=A-1// A = SP-1 (first arg)
            M=M+D// *SP + *(SP-1)
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
@SP
            M=M-1// SP = SP--
            A=M// A = SP
            D=M// D = *SP (second arg)
            A=A-1// A = SP-1 (first arg)
            M=M-D// *SP + *(SP-1)
@THIS
        D=M// D=THIS
        @6
        A=D+A// A=THIS+6
        D=M// D=*(THIS+6)
        @SP
        A=M// A = SP
        M=D// *SP = D
        @SP
        M=M+1// SP++
@THIS
        D=M// D=THIS
        @6
        A=D+A// A=THIS+6
        D=M// D=*(THIS+6)
        @SP
        A=M// A = SP
        M=D// *SP = D
        @SP
        M=M+1// SP++
@SP
            M=M-1// SP = SP--
            A=M// A = SP
            D=M// D = *SP (second arg)
            A=A-1// A = SP-1 (first arg)
            M=M+D// *SP + *(SP-1)
@SP
            M=M-1// SP = SP--
            A=M// A = SP
            D=M// D = *SP (second arg)
            A=A-1// A = SP-1 (first arg)
            M=M-D// *SP + *(SP-1)
@5
    D=A
    @6
    A=A+D// A = addr = 5 + val
    D=M// D = *addr
    @SP // A = &SP
    A=M // A = SP
    M=D // *SP = D
    @SP // A = &SP
    M=M+1// SP++
@SP
            M=M-1// SP = SP--
            A=M// A = SP
            D=M// D = *SP (second arg)
            A=A-1// A = SP-1 (first arg)
            M=M+D// *SP + *(SP-1)