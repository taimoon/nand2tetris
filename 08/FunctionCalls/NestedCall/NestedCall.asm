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
// function Sys.init 0
    (Sys.init)
    
    // end of initializing local variables

// push const 4000
    @4000
    D=A
    @SP
    A=M
    M=D
    @SP
    M=M+1

// pop pointer 0
    @SP
    AM=M-1 // SP--
    D=M// D=*SP
    @THIS
    M=D// THIS/THAT = *SP

// push const 5000
    @5000
    D=A
    @SP
    A=M
    M=D
    @SP
    M=M+1

// pop pointer 1
    @SP
    AM=M-1 // SP--
    D=M// D=*SP
    @THAT
    M=D// THIS/THAT = *SP

// call Sys.main 0
    // save the caller's frame
    @NestedCall$Sys.init$Sys.main$ret.0
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
    @Sys.main
    0;JMP
    (NestedCall$Sys.init$Sys.main$ret.0) // translated-generated label
    // end of call Sys.main 0

// pop temp 1
    // addr = 5 + 1
    @6
    D=A// A = addr = 5 + val
    // store addr as temp var
    @SP
    A=M
    M=D
    @SP
    AM=M-1// A=SP--
    D=M// D=*SP
    A=A+1
    A=M// A = *(SP+1) = addr
    M=D// *addr = *SP

// label LOOP
    (NestedCall$Sys.init$LOOP)

// goto LOOP
    @NestedCall$Sys.init$LOOP
    0;JMP

// function Sys.main 5
    (Sys.main)
    
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
    

    @SP
    A=M
    M=0
    @SP
    M=M+1
    
    // end of initializing local variables

// push const 4001
    @4001
    D=A
    @SP
    A=M
    M=D
    @SP
    M=M+1

// pop pointer 0
    @SP
    AM=M-1 // SP--
    D=M// D=*SP
    @THIS
    M=D// THIS/THAT = *SP

// push const 5001
    @5001
    D=A
    @SP
    A=M
    M=D
    @SP
    M=M+1

// pop pointer 1
    @SP
    AM=M-1 // SP--
    D=M// D=*SP
    @THAT
    M=D// THIS/THAT = *SP

// push const 200
    @200
    D=A
    @SP
    A=M
    M=D
    @SP
    M=M+1

// pop LCL 1
    @LCL
    D=M// D=LCL
    @1
    D=D+A// D=LCL+1=addr
    @SP// *SP = addr+pos
    A=M
    M=D
    @SP
    AM=M-1// A = SP--
    D=M// D = *SP
    A=A+1// A = SP+1
    A=M// A = *(SP+1) = addr
    M=D// *addr = *SP

// push const 40
    @40
    D=A
    @SP
    A=M
    M=D
    @SP
    M=M+1

// pop LCL 2
    @LCL
    D=M// D=LCL
    @2
    D=D+A// D=LCL+2=addr
    @SP// *SP = addr+pos
    A=M
    M=D
    @SP
    AM=M-1// A = SP--
    D=M// D = *SP
    A=A+1// A = SP+1
    A=M// A = *(SP+1) = addr
    M=D// *addr = *SP

// push const 6
    @6
    D=A
    @SP
    A=M
    M=D
    @SP
    M=M+1

// pop LCL 3
    @LCL
    D=M// D=LCL
    @3
    D=D+A// D=LCL+3=addr
    @SP// *SP = addr+pos
    A=M
    M=D
    @SP
    AM=M-1// A = SP--
    D=M// D = *SP
    A=A+1// A = SP+1
    A=M// A = *(SP+1) = addr
    M=D// *addr = *SP

// push const 123
    @123
    D=A
    @SP
    A=M
    M=D
    @SP
    M=M+1

// call Sys.add12 1
    // save the caller's frame
    @NestedCall$Sys.main$Sys.add12$ret.0
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
    @Sys.add12
    0;JMP
    (NestedCall$Sys.main$Sys.add12$ret.0) // translated-generated label
    // end of call Sys.add12 1

// pop temp 0
    // addr = 5 + 0
    @5
    D=A// A = addr = 5 + val
    // store addr as temp var
    @SP
    A=M
    M=D
    @SP
    AM=M-1// A=SP--
    D=M// D=*SP
    A=A+1
    A=M// A = *(SP+1) = addr
    M=D// *addr = *SP

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

// push LCL 2
        @LCL
        D=M// D=LCL
        @2
        A=D+A// A=LCL+2
        D=M// D=*(LCL+2)
        @SP
        A=M// A = SP
        M=D// *SP = D
        @SP
        M=M+1// SP++

// push LCL 3
        @LCL
        D=M// D=LCL
        @3
        A=D+A// A=LCL+3
        D=M// D=*(LCL+3)
        @SP
        A=M// A = SP
        M=D// *SP = D
        @SP
        M=M+1// SP++

// push LCL 4
        @LCL
        D=M// D=LCL
        @4
        A=D+A// A=LCL+4
        D=M// D=*(LCL+4)
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

// arithmetic add
            @SP
            AM=M-1// SP = SP--
            D=M// D = *SP (second arg)
            A=A-1// A = SP-1 (first arg)
            MD=M+D// *SP + *(SP-1)

// arithmetic add
            @SP
            AM=M-1// SP = SP--
            D=M// D = *SP (second arg)
            A=A-1// A = SP-1 (first arg)
            MD=M+D// *SP + *(SP-1)

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

// function Sys.add12 0
    (Sys.add12)
    
    // end of initializing local variables

// push const 4002
    @4002
    D=A
    @SP
    A=M
    M=D
    @SP
    M=M+1

// pop pointer 0
    @SP
    AM=M-1 // SP--
    D=M// D=*SP
    @THIS
    M=D// THIS/THAT = *SP

// push const 5002
    @5002
    D=A
    @SP
    A=M
    M=D
    @SP
    M=M+1

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

// push const 12
    @12
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