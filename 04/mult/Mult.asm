// This file is part of www.nand2tetris.org
// and the book "The Elements of Computing Systems"
// by Nisan and Schocken, MIT Press.
// File name: projects/04/Mult.asm

// Multiplies R0 and R1 and stores the result in R2.
// (R0, R1, R2 refer to RAM[0], RAM[1], and RAM[2], respectively.)
//
// This program only needs to handle arguments that satisfy
// R0 >= 0, R1 >= 0, and R0*R1 < 32768.

//	Pseudocode:
//		int r0, r1, r2
//		int i = 0
//		while(i < r1) //i-r1 < 0
//			r2 = r2 + r0
//			++i
//			END


// Put your code here.
//@symbol, it is like abstract pointer

	@R2
	M=0
	@i
	M=0
(LOOP)
	@i
	D=M
	@R1
	D=D-M		//D=i-R1
	@END		//the address of (END)
	D;JGE		//if i-R1 >= 0, then goto end
	@R0
	D=M
	@R2
	M=D+M
	@i
	M=M+1
	@LOOP
	0;JMP
(END)
	@END
	0;JMP



	