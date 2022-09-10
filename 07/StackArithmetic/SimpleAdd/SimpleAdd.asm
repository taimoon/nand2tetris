@7 // A = val
    D=A
    @SP // A = SP
    A=M // A = RAM[A]
    M=D // RAM[A] = D
    @SP // A = SP
    M=M+1// SP++
@8 // A = val
    D=A
    @SP // A = SP
    A=M // A = RAM[A]
    M=D // RAM[A] = D
    @SP // A = SP
    M=M+1// SP++
@SP
            M=M-1// SP = SP--
            A=M// A = SP
            D=M// D = *SP (second arg)
            A=A-1// A = SP-1 (first arg)
            M=M+D// *SP + *(SP-1)