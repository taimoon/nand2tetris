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
// function Class1.set 0
    (Class1.set)
    
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

// pop static 0
    @SP
    AM=M-1// SP--
    D=M// D=*SP
    @Class1.0
    M=D// RAM[pos+16] = D = *SP

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

// pop static 1
    @SP
    AM=M-1// SP--
    D=M// D=*SP
    @Class1.1
    M=D// RAM[pos+16] = D = *SP

// push const 0
    @0
    D=A
    @SP
    A=M
    M=D
    @SP
    M=M+1

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

// function Class1.get 0
    (Class1.get)
    
    // end of initializing local variables

// push static 0
    @Class1.0
    D=M
    @SP 
    A=M // A=SP
    M=D// *SP = D
    @SP
    M=M+1// SP++

// push static 1
    @Class1.1
    D=M
    @SP 
    A=M // A=SP
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
// function Class2.set 0
    (Class2.set)
    
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

// pop static 0
    @SP
    AM=M-1// SP--
    D=M// D=*SP
    @Class2.0
    M=D// RAM[pos+16] = D = *SP

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

// pop static 1
    @SP
    AM=M-1// SP--
    D=M// D=*SP
    @Class2.1
    M=D// RAM[pos+16] = D = *SP

// push const 0
    @0
    D=A
    @SP
    A=M
    M=D
    @SP
    M=M+1

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

// function Class2.get 0
    (Class2.get)
    
    // end of initializing local variables

// push static 0
    @Class2.0
    D=M
    @SP 
    A=M // A=SP
    M=D// *SP = D
    @SP
    M=M+1// SP++

// push static 1
    @Class2.1
    D=M
    @SP 
    A=M // A=SP
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
// function Sys.init 0
    (Sys.init)
    
    // end of initializing local variables

// push const 6
    @6
    D=A
    @SP
    A=M
    M=D
    @SP
    M=M+1

// push const 8
    @8
    D=A
    @SP
    A=M
    M=D
    @SP
    M=M+1

// call Class1.set 2
    // save the caller's frame
    @StaticsTest$Sys.init$Class1.set$ret.0
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
    
    @7 // ARG = SP - (2 + 5) ; reposition ARG
    D=A
    @SP
    D=M-D
    @ARG
    M=D
    @SP//  LCL = SP ; reposition LCL
    D=M
    @LCL
    M=D
    @Class1.set
    0;JMP
    (StaticsTest$Sys.init$Class1.set$ret.0) // translated-generated label
    // end of call Class1.set 2

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

// push const 23
    @23
    D=A
    @SP
    A=M
    M=D
    @SP
    M=M+1

// push const 15
    @15
    D=A
    @SP
    A=M
    M=D
    @SP
    M=M+1

// call Class2.set 2
    // save the caller's frame
    @StaticsTest$Sys.init$Class2.set$ret.0
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
    
    @7 // ARG = SP - (2 + 5) ; reposition ARG
    D=A
    @SP
    D=M-D
    @ARG
    M=D
    @SP//  LCL = SP ; reposition LCL
    D=M
    @LCL
    M=D
    @Class2.set
    0;JMP
    (StaticsTest$Sys.init$Class2.set$ret.0) // translated-generated label
    // end of call Class2.set 2

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

// call Class1.get 0
    // save the caller's frame
    @StaticsTest$Sys.init$Class1.get$ret.0
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
    @Class1.get
    0;JMP
    (StaticsTest$Sys.init$Class1.get$ret.0) // translated-generated label
    // end of call Class1.get 0

// call Class2.get 0
    // save the caller's frame
    @StaticsTest$Sys.init$Class2.get$ret.0
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
    @Class2.get
    0;JMP
    (StaticsTest$Sys.init$Class2.get$ret.0) // translated-generated label
    // end of call Class2.get 0

// label WHILE
    (StaticsTest$Sys.init$WHILE)

// goto WHILE
    @StaticsTest$Sys.init$WHILE
    0;JMP