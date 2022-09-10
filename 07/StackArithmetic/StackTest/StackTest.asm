@17 // A = val
    D=A
    @SP // A = SP
    A=M // A = RAM[A]
    M=D // RAM[A] = D
    @SP // A = SP
    M=M+1// SP++
@17 // A = val
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
            D=M-D
            @__BOOL0
            D;JEQ
            @SP
            A=M-1
            M=0 // 0 represent false value
            @__ENDBOOL0
            0;JMP
            (__BOOL0)
            @SP
            A=M-1
            M=-1
            (__ENDBOOL0)
@17 // A = val
    D=A
    @SP // A = SP
    A=M // A = RAM[A]
    M=D // RAM[A] = D
    @SP // A = SP
    M=M+1// SP++
@16 // A = val
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
            D=M-D
            @__BOOL1
            D;JEQ
            @SP
            A=M-1
            M=0 // 0 represent false value
            @__ENDBOOL1
            0;JMP
            (__BOOL1)
            @SP
            A=M-1
            M=-1
            (__ENDBOOL1)
@16 // A = val
    D=A
    @SP // A = SP
    A=M // A = RAM[A]
    M=D // RAM[A] = D
    @SP // A = SP
    M=M+1// SP++
@17 // A = val
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
            D=M-D
            @__BOOL2
            D;JEQ
            @SP
            A=M-1
            M=0 // 0 represent false value
            @__ENDBOOL2
            0;JMP
            (__BOOL2)
            @SP
            A=M-1
            M=-1
            (__ENDBOOL2)
@892 // A = val
    D=A
    @SP // A = SP
    A=M // A = RAM[A]
    M=D // RAM[A] = D
    @SP // A = SP
    M=M+1// SP++
@891 // A = val
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
            D=M-D
            @__BOOL3
            D;JLT
            @SP
            A=M-1
            M=0 // 0 represent false value
            @__ENDBOOL3
            0;JMP
            (__BOOL3)
            @SP
            A=M-1
            M=-1
            (__ENDBOOL3)
@891 // A = val
    D=A
    @SP // A = SP
    A=M // A = RAM[A]
    M=D // RAM[A] = D
    @SP // A = SP
    M=M+1// SP++
@892 // A = val
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
            D=M-D
            @__BOOL4
            D;JLT
            @SP
            A=M-1
            M=0 // 0 represent false value
            @__ENDBOOL4
            0;JMP
            (__BOOL4)
            @SP
            A=M-1
            M=-1
            (__ENDBOOL4)
@891 // A = val
    D=A
    @SP // A = SP
    A=M // A = RAM[A]
    M=D // RAM[A] = D
    @SP // A = SP
    M=M+1// SP++
@891 // A = val
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
            D=M-D
            @__BOOL5
            D;JLT
            @SP
            A=M-1
            M=0 // 0 represent false value
            @__ENDBOOL5
            0;JMP
            (__BOOL5)
            @SP
            A=M-1
            M=-1
            (__ENDBOOL5)
@32767 // A = val
    D=A
    @SP // A = SP
    A=M // A = RAM[A]
    M=D // RAM[A] = D
    @SP // A = SP
    M=M+1// SP++
@32766 // A = val
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
            D=M-D
            @__BOOL6
            D;JGT
            @SP
            A=M-1
            M=0 // 0 represent false value
            @__ENDBOOL6
            0;JMP
            (__BOOL6)
            @SP
            A=M-1
            M=-1
            (__ENDBOOL6)
@32766 // A = val
    D=A
    @SP // A = SP
    A=M // A = RAM[A]
    M=D // RAM[A] = D
    @SP // A = SP
    M=M+1// SP++
@32767 // A = val
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
            D=M-D
            @__BOOL7
            D;JGT
            @SP
            A=M-1
            M=0 // 0 represent false value
            @__ENDBOOL7
            0;JMP
            (__BOOL7)
            @SP
            A=M-1
            M=-1
            (__ENDBOOL7)
@32766 // A = val
    D=A
    @SP // A = SP
    A=M // A = RAM[A]
    M=D // RAM[A] = D
    @SP // A = SP
    M=M+1// SP++
@32766 // A = val
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
            D=M-D
            @__BOOL8
            D;JGT
            @SP
            A=M-1
            M=0 // 0 represent false value
            @__ENDBOOL8
            0;JMP
            (__BOOL8)
            @SP
            A=M-1
            M=-1
            (__ENDBOOL8)
@57 // A = val
    D=A
    @SP // A = SP
    A=M // A = RAM[A]
    M=D // RAM[A] = D
    @SP // A = SP
    M=M+1// SP++
@31 // A = val
    D=A
    @SP // A = SP
    A=M // A = RAM[A]
    M=D // RAM[A] = D
    @SP // A = SP
    M=M+1// SP++
@53 // A = val
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
@112 // A = val
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
            M=M-D// *SP + *(SP-1)
@SP
            A=M-1// A = SP-1
            M=-M
@SP
            M=M-1// SP = SP--
            A=M// A = SP
            D=M// D = *SP (second arg)
            A=A-1// A = SP-1 (first arg)
            M=M&D// *SP + *(SP-1)
@82 // A = val
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
            M=M|D// *SP + *(SP-1)
@SP
            A=M-1// A = SP-1
            M=!M