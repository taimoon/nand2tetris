@256
        D=A
        @SP
        M=D
        // call Sys.init 0
    // save the caller's frame
    @__BOOTSTRAP$Sys.init$ret.0
    D=A
    @SP
    A=M
    M=D
    @SP
    M=M+1
    
        @LCL
        D=M
        @SP
        A=M
        M=D
        @SP
        M=M+1
    
    
        @ARG
        D=M
        @SP
        A=M
        M=D
        @SP
        M=M+1
    
    
        @THIS
        D=M
        @SP
        A=M
        M=D
        @SP
        M=M+1
    
    
        @THAT
        D=M
        @SP
        A=M
        M=D
        @SP
        M=M+1
    
    @5 // ARG = SP - (0 + 5) ; reposition ARG
    D=A
    @SP
    D=M-D
    @ARG
    M=D
    @SP//  LCL = SP ; reposition LCL
    D=M
    @LCL
    M=D
    @Sys.init
    0;JMP
    (__BOOTSTRAP$Sys.init$ret.0) // translated-generated label
    // end of call Sys.init 0
// function Main.fibonacci 0
    (Main.fibonacci)
    
    // end of initializing local variables

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

// arithmetic lt
            @SP
            AM=M-1// SP = SP--
            D=M// D = *SP (second arg)
            A=A-1// A = SP-1 (first arg)
            MD=M-D// *SP + *(SP-1)
        @__BOOL0
                D;JLT
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

// if-goto IF_TRUE
    @SP
    M=M-1// SP--
    A=M// A=SP
    D=M// D=*SP
    @FibonacciElement$Main.fibonacci$IF_TRUE
    D;JNE // jump if not false (ie.: not equal to 0)

// goto IF_FALSE
    @FibonacciElement$Main.fibonacci$IF_FALSE
    0;JMP

// label IF_TRUE
    (FibonacciElement$Main.fibonacci$IF_TRUE)

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

// label IF_FALSE
    (FibonacciElement$Main.fibonacci$IF_FALSE)

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

// call Main.fibonacci 1
    // save the caller's frame
    @FibonacciElement$Main.fibonacci$Main.fibonacci$ret.0
    D=A
    @SP
    A=M
    M=D
    @SP
    M=M+1
    
        @LCL
        D=M
        @SP
        A=M
        M=D
        @SP
        M=M+1
    
    
        @ARG
        D=M
        @SP
        A=M
        M=D
        @SP
        M=M+1
    
    
        @THIS
        D=M
        @SP
        A=M
        M=D
        @SP
        M=M+1
    
    
        @THAT
        D=M
        @SP
        A=M
        M=D
        @SP
        M=M+1
    
    @6 // ARG = SP - (1 + 5) ; reposition ARG
    D=A
    @SP
    D=M-D
    @ARG
    M=D
    @SP//  LCL = SP ; reposition LCL
    D=M
    @LCL
    M=D
    @Main.fibonacci
    0;JMP
    (FibonacciElement$Main.fibonacci$Main.fibonacci$ret.0) // translated-generated label
    // end of call Main.fibonacci 1

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

// call Main.fibonacci 1
    // save the caller's frame
    @FibonacciElement$Main.fibonacci$Main.fibonacci$ret.1
    D=A
    @SP
    A=M
    M=D
    @SP
    M=M+1
    
        @LCL
        D=M
        @SP
        A=M
        M=D
        @SP
        M=M+1
    
    
        @ARG
        D=M
        @SP
        A=M
        M=D
        @SP
        M=M+1
    
    
        @THIS
        D=M
        @SP
        A=M
        M=D
        @SP
        M=M+1
    
    
        @THAT
        D=M
        @SP
        A=M
        M=D
        @SP
        M=M+1
    
    @6 // ARG = SP - (1 + 5) ; reposition ARG
    D=A
    @SP
    D=M-D
    @ARG
    M=D
    @SP//  LCL = SP ; reposition LCL
    D=M
    @LCL
    M=D
    @Main.fibonacci
    0;JMP
    (FibonacciElement$Main.fibonacci$Main.fibonacci$ret.1) // translated-generated label
    // end of call Main.fibonacci 1

// arithmetic add
            @SP
            AM=M-1// SP = SP--
            D=M// D = *SP (second arg)
            A=A-1// A = SP-1 (first arg)
            MD=M+D// *SP + *(SP-1)

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
// function Sys.init 0
    (Sys.init)
    
    // end of initializing local variables

// push const 4
    @4
    D=A
    @SP
    A=M
    M=D
    @SP
    M=M+1

// call Main.fibonacci 1
    // save the caller's frame
    @FibonacciElement$Sys.init$Main.fibonacci$ret.0
    D=A
    @SP
    A=M
    M=D
    @SP
    M=M+1
    
        @LCL
        D=M
        @SP
        A=M
        M=D
        @SP
        M=M+1
    
    
        @ARG
        D=M
        @SP
        A=M
        M=D
        @SP
        M=M+1
    
    
        @THIS
        D=M
        @SP
        A=M
        M=D
        @SP
        M=M+1
    
    
        @THAT
        D=M
        @SP
        A=M
        M=D
        @SP
        M=M+1
    
    @6 // ARG = SP - (1 + 5) ; reposition ARG
    D=A
    @SP
    D=M-D
    @ARG
    M=D
    @SP//  LCL = SP ; reposition LCL
    D=M
    @LCL
    M=D
    @Main.fibonacci
    0;JMP
    (FibonacciElement$Sys.init$Main.fibonacci$ret.0) // translated-generated label
    // end of call Main.fibonacci 1

// label WHILE
    (FibonacciElement$Sys.init$WHILE)

// goto WHILE
    @FibonacciElement$Sys.init$WHILE
    0;JMP