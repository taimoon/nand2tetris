@111 // A = val
    D=A
    @SP // A = SP
    A=M // A = RAM[A]
    M=D // RAM[A] = D
    @SP // A = SP
    M=M+1// SP++
@333 // A = val
    D=A
    @SP // A = SP
    A=M // A = RAM[A]
    M=D // RAM[A] = D
    @SP // A = SP
    M=M+1// SP++
@888 // A = val
    D=A
    @SP // A = SP
    A=M // A = RAM[A]
    M=D // RAM[A] = D
    @SP // A = SP
    M=M+1// SP++
@SP
    M=M-1// SP--
    A=M// A=SP
    D=M// D=*SP
    @24
    M=D// RAM[POS+16] = D = *SP
@SP
    M=M-1// SP--
    A=M// A=SP
    D=M// D=*SP
    @19
    M=D// RAM[POS+16] = D = *SP
@SP
    M=M-1// SP--
    A=M// A=SP
    D=M// D=*SP
    @17
    M=D// RAM[POS+16] = D = *SP
@19
    D=M// D=RAM[pos+16]
    @SP 
    A=M // A=SP
    M=D// *SP = D
    @SP
    M=M+1// SP++
@17
    D=M// D=RAM[pos+16]
    @SP 
    A=M // A=SP
    M=D// *SP = D
    @SP
    M=M+1// SP++
@SP
            M=M-1// SP = SP--
            A=M// A = SP
            D=M// D = *SP (second arg)
            A=A-1// A = SP-1 (first arg)
            M=M-D// *SP + *(SP-1)
@24
    D=M// D=RAM[pos+16]
    @SP 
    A=M // A=SP
    M=D// *SP = D
    @SP
    M=M+1// SP++
@SP
            M=M-1// SP = SP--
            A=M// A = SP
            D=M// D = *SP (second arg)
            A=A-1// A = SP-1 (first arg)
            M=M+D// *SP + *(SP-1)