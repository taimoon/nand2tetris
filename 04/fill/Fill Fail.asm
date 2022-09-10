// This file is part of www.nand2tetris.org
// and the book "The Elements of Computing Systems"
// by Nisan and Schocken, MIT Press.
// File name: projects/04/Fill.asm

// Runs an infinite loop that listens to the keyboard input.
// When a key is pressed (any key), the program blackens the screen,
// i.e. writes "black" in every pixel;
// the screen should remain fully black as long as the key is pressed. 
// When no key is pressed, the program clears the screen, i.e. writes
// "white" in every pixel;
// the screen should remain fully clear as long as no key is pressed.

// Put your code here.

//IO pointer - SCREEN, KBD
//backspace 129
@ptr
M=0
D=M

(LOOP)
	@END
	@KBD
	D=M
	@LOOP1
	D;JEQ
	@ptr
	D=M
	@SCREEN
	A=A+D
	M=1
	D=D+1
	@ptr
	M=D
	@LOOP
	0;JMP
(END)
(LOOP1)
	@END1
	@KBD
	D=M
	@LOOP
	D;JNE
	@ptr
	D=M
	@SCREEN
	A=A+D
	M=0
	@ENDCOND1		//Avoid decreasing the ptr < 0
	D;JLE
	(COND1)
		D=D-1
		@ptr
		M=D
	(ENDCOND1)
	@LOOP1
	0;JMP
(END1)