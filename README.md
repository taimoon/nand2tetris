# nand2tetris

This is my programs for following and doing [nand2tetris](https://www.nand2tetris.org/). It is currently complete for all project modules. 
It was a fruitful yet gentle introduction to computer architecture. I would recommend this course to everyone who is not CS major but know some programming 
and interested in understanding and building a modern computer.

## Note
1. I'm not familiar with Java as much as Python.
2. The Hack is the binary code for the hack platform proposed in the project.
3. The assembly here is custom-made for the hack platform. It is not the conventional assembly language. 
4. Jack is a Java-like language.
5. The [assembler](/06/hack_assembler.py) and [jack compiler](/11/code_generator.py) are implemented using Python and used on the hack platform.
6. The repo does not include software tools provided by nand2tetris but can be found the same website.

## Implications and Challenges
1. In translating high level langauge to virtual machine script, the method of handling function calling and recursion function are very similiar to my observation of assembly code of C files.
2. The hack cpu is essentially a stack-based machine.
3. Pointers by C is an abstraction over low-level address manipulation.
4. Regex is particularly useful in tokenizing the languages.
5. This is my first time of applying heap data structure for memory os in implementing jack os.
6. Debugging the virtual machine translator is challenging especially in implementing nestedcall.vm. Indeed, a good debugger really helps.
7. Jack is not only similar to Java in term of syntax but also implementation that both compiles the source to virtual machine code then run on virtual machine. Try `javac` and `javap -c` a simple java file and compare it with vm code generated from jack file.

## Afterthought
1. In current implementation, the jack compiler does parse and generate vm code at the same time from tokens in one pass. Instead, it could generate code from AST due to parse (two passes). This is not explicitly hinted by the courses.
2. The grammar for infix expression is ambiguous which yield multiple parse tree. Naively evaluate or compile based traversal of the parse tree yield different result; depending on the structure of parse tree. To simplify thing, all expressions are evaluated from left to right (left associative) but parenthesised expression is prioritized. One of the solution, it is to define a new grammar that consider precedence and associativity.

    This raise a question. Usually, parse tree (or grammar) doesn't affect the semantic of programming language but it does affect the semantic. Sometimes, we wish only compiler/interpreter handle the semantic of the language but we must consider the syntatical matter in this case. 
    
    On the other hand, prefix and postfix expression are particularly convenient for evaluating expression. Postfix expression can be naturally applied to stack-based evaluation; prefix expression is just usual function call evaluation (or it is merely procedure application in LISP). Although elegant implementation and consistency, prefix or postfix expressions are indeed ugly to newcomers.
3. One day, I wish to run the hack assembly code without expand the code and run these on simulator. As inspired by the interpreter in SICP and EOPL, I can develop a program to interpret the hack assembly code.  Another motivation would be that it is very inconvenient to get the x86 assembly code run on my pc and the the instruction set is too complex for learning. Why not I design my own instruction set and develop interpreter to test my design for educational purpose? After researching, I realized that this is how Python, Lua and Java could be implemented using virtual machine. This is also the content of SICP chapter 5. These would be part of formal education in CS but I'm not CS student. The contents from nand2tetris and SICP are valuable to me as a non-CS student.
