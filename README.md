# nand2tetris

This is my programs for following and doing [nand2tetris](https://www.nand2tetris.org/). It is currently complete for all project modules. 
It was a fruitful yet gentle introduction to computer architecture. I would recommend this course to everyone who is not CS major but know some programming 
and interested in understanding and building a modern computer.

## Note
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

## Afterthought
1. The grammar for infix expression is ambiguous which yield multiple parse tree. Naively evaluate or compile based traversal of the parse tree yield different result; depending on the structure of parse tree. To make thing simpler, all expressions are evaluated from left to right (left associative) but parenthesised expression is prioritized. As suggested by the course authors, there are 2 options to resolve ambiguity: during parsing or during code generation. For first option, the parser will parse the infix expression so that its parse tree yield postfix expression that is equivalent evaluating from left to right. For second option, the compiler will generate code by iterating through the infix expression from left to right. However, there is one more alternative option. This option is to define a new grammar that consider precedence and associativity.

    This raise a question. Usually, parse tree (or grammar) doesn't affect the semantic of programming language but it does affect the semantic. Sometimes, we wish only compiler/interpreter handle the semantic of the language but we must consider the syntatical matter in this case. 
    
    On the other hand, prefix and postfix expression are particularly convenient for evaluating expression. Postfix expression can be naturally applied to stack-based evaluation; prefix expression is just usual function call evaluation (or it is merely procedure application in LISP). Althought elegant implementation and consistency, prefix or postfix expressions are indeed ugly to newcomers.
