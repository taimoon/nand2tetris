@3030 // A = val
    D=A
    @SP // A = SP
    A=M // A = RAM[A]
    M=D // RAM[A] = D
    @SP // A = SP
    M=M+1// SP++
@SP
    M=M-1 // SP--
    A=M// A=SP
    D=M// D=*SP
    @THIS
    M=D// THIS/THAT = *SP
@3040 // A = val
    D=A
    @SP // A = SP
    A=M // A = RAM[A]
    M=D // RAM[A] = D
    @SP // A = SP
    M=M+1// SP++
@SP
    M=M-1 // SP--
    A=M// A=SP
    D=M// D=*SP
    @THAT
    M=D// THIS/THAT = *SP
@32 // A = val
    D=A
    @SP // A = SP
    A=M // A = RAM[A]
    M=D // RAM[A] = D
    @SP // A = SP
    M=M+1// SP++
@THIS
        D=M// D=THIS
        @2
        D=D+A// D=THIS+2=addr
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
@46 // A = val
    D=A
    @SP // A = SP
    A=M // A = RAM[A]
    M=D // RAM[A] = D
    @SP // A = SP
    M=M+1// SP++
@THAT
        D=M// D=THAT
        @6
        D=D+A// D=THAT+6=addr
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
@THIS
    D=M// D=THIS/THAT
    @SP
    A=M // A=SP
    M=D// *SP = THIS/THAT
    @SP
    M=M+1// SP++
@THAT
    D=M// D=THIS/THAT
    @SP
    A=M // A=SP
    M=D// *SP = THIS/THAT
    @SP
    M=M+1// SP++
@SP
            M=M-1// SP = SP--
            A=M// A = SP
            D=M// D = *SP (second arg)
            A=A-1// A = SP-1 (first arg)
            M=M+D// *SP + *(SP-1)
@THIS
        D=M// D=THIS
        @2
        A=D+A// A=THIS+2
        D=M// D=*(THIS+2)
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
@THAT
        D=M// D=THAT
        @6
        A=D+A// A=THAT+6
        D=M// D=*(THAT+6)
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