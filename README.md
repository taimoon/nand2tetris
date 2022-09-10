# nand2tetris

This is my programs for following and doing [nand2tetris](https://www.nand2tetris.org/). It is currently complete for all project modules. 
It was a fruitful yet gentle introduction to computer architecture. I would recommend this course to everyone who is not CS major but know some programming 
and interested in understanding and building a modern computer.

## Note:
1. The Hack is the binary code for the hack platform proposed in the project.
2. The assembly here is custom-made for the hack platform. It is not the conventional assembly language. 
3. Jack is a Java-like language.
4. The [assembler](/06/hack_assembler.py) and [jack compiler](/11/code_generator.py) are implemented using Python and used on the hack platform.
5. The repo does not include software tools provided by nand2tetris but can be found the same website.

## Implications and Challenges
1. In translating high level langauge to virtual machine script, the method of handling function calling and recursion function are very similiar to my observation of assembly code of C files.
2. The hack cpu is essentially a stack-based machine which can be compared to the Turing Tape machine model.
3. Pointers by C is an abstraction over low-level address manipulation.
4. Regex is particular useful in tokenizing the languages.
5. This is my first time of applying heap data structure for memory os in implementing jack os.
6. Debugging the virtual machine translator is challenging especially in implementing nestedcall.vm. Indeed, a good debugger really helps.
