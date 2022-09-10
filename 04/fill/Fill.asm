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

@block
M=0
(INPUT)
	@KBD
	D=M
	@LOOP
	D;JNE
	@LOOP1
	D;JEQ
	@INPUT
	0;JMP
(ENDINPUT)
(LOOP)
	@block
	D=M
	@8192
	D=D-A			//D = block - 8192
	@INPUT
	D;JGE			//if block >= 8192, then block-8192 >= 0, and jump out
	@block
	D=M
	@SCREEN
	A=A+D
	D=!M
	M=D|M
	@block
	M=M+1
	@INPUT
	0;JMP
(END)
(LOOP1)
	@block
	D=M
	@INPUT
	D;JLT			//if block == 0, then jump out
	@block
	D=M
	@SCREEN
	A=A+D
	D=!M
	M=D&M
	@block
	M=M-1
	@INPUT
	0;JMP
(END1)
	@END1
	0;JMP