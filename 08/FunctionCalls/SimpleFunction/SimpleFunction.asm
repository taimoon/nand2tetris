// function SimpleFunction.test 2
    (SimpleFunction.test)
    
    @SP
    A=M
    M=0
    @SP
    M=M+1
    

    @SP
    A=M
    M=0
    @SP
    M=M+1
    
    // end of initializing local variables

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

// push LCL 1
        @LCL
        D=M// D=LCL
        @1
        A=D+A// A=LCL+1
        D=M// D=*(LCL+1)
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

// arithmetic not
            @SP
            A=M-1// A = SP-1
            M=!M

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

// arithmetic add
            @SP
            AM=M-1// SP = SP--
            D=M// D = *SP (second arg)
            A=A-1// A = SP-1 (first arg)
            MD=M+D// *SP + *(SP-1)

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

// arithmetic sub
            @SP
            AM=M-1// SP = SP--
            D=M// D = *SP (second arg)
            A=A-1// A = SP-1 (first arg)
            MD=M-D// *SP + *(SP-1)

// return
    // return the value to the caller
    // store retaddr as temp var at R13
    @5
    D=A
    @LCL
    A=M-D
    D=M
    @R13// R13 = return address
    M=D
    @SP// *ARG = pop()
    AM=M-1
    D=M// return value
    @ARG
    A=M
    M=D
    // reposition SP of the caller
    @ARG// SP = ARG + 1 
    D=M+1
    @SP
    M=D
    
        @LCL
        AM=M-1
        D=M
        @THAT
        M=D
    

        @LCL
        AM=M-1
        D=M
        @THIS
        M=D
    

        @LCL
        AM=M-1
        D=M
        @ARG
        M=D
    

        @LCL
        AM=M-1
        D=M
        @LCL
        M=D
    
    @R13
    A=M
    0;JMP
    // end of returning