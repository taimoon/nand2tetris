from tokenizer import Token, buffer_tokenizer
from symbol_table import *
from itertools import count
def print_and_return(itm):
    print(itm)
    return itm

class ParseTree:
    # allow typeless ParseTree represented by type = ""
    def __init__(self, type, attr, *nodes):
        self.type = type
        self.attrs = [attr] + list(nodes)
    def to_xml(self):
        res = ""
        for attr in self.attrs:
            if isinstance(attr, Token) or isinstance(attr, ParseTree):
                res = f"{res}\n{attr.to_xml()}"
            elif attr != "":
                content = Token.escape_corpsd.get(attr, attr)
                res = f"{res}\n{content}"
        if self.type == "":
            return res.lstrip()
        return f"<{self.type}> {res}\n</{self.type}>"
    def __repr__(self):
        return self.to_xml()
    def __str__(self):
        return self.to_xml()

def read_file(path):
    res = ""
    with open(path, "r") as f:
        res = f.read()
    return res

# the compilation part always consuming tokens(popping) unless stated

class Parser:
    semicolon_token = Token("symbol", ";")
    left_bracket_token = Token("symbol", "(")
    right_bracket_token = Token("symbol", ")")
    left_curly_bracket_token = Token("symbol", "{")
    right_curly_bracket_token = Token("symbol", "}")
    left_square_bracket_token = Token("symbol", "[")
    right_square_bracket_token = Token("symbol", "]")
    comma_token = Token("symbol", ",")
    dot_token = Token("symbol", ".")
    equal_token = Token("symbol", "=")

    bracket_token_pair = left_bracket_token, right_bracket_token
    curly_bracket_token_pair = left_curly_bracket_token, right_curly_bracket_token
    square_bracket_token = left_square_bracket_token, right_square_bracket_token
    
    def __init__(self):
        pass

    def next_token(self) -> Token:
        return self.tokenizer.next_token()
    
    def peek_next_token(self) -> Token:
        return self.tokenizer.peek_next_token()
    
    def put_back_token(self, tk:Token):
        self.tokenizer.put_back_token(tk)
    
    def peek(self, pos = -1):
        return self.tokenizer.peek(pos)

    def parse(self, str_prog = ""):
        self.tokenizer = buffer_tokenizer(str_prog)
        self.prog = []
        try:
            while self.peek_next_token() == Token("keyword", "class"):
                self.prog.append(self.compile_class())
        except StopIteration:
            return self.prog
    
    def write(self, input_path = ""):
        from os.path import dirname, splitext,basename, isdir
        
        if isdir(input_path):
            from os import listdir
            rel_path = input_path
            ext_of_file = lambda f : f[f.rfind('.')+1:]
            jack_files = [f for f in listdir(input_path) if ext_of_file(f) == "jack"]
            for input_file in jack_files:
                jack_file = f"{rel_path}\\{input_file}"
                name_of_file = lambda f : f[:f.rfind('.')]
                dest = f"{rel_path}\\{name_of_file(input_file)}.vm"
                with open(dest, "w") as f:
                    for cls in self.parse(str_prog=read_file(jack_file)):
                        f.write(str(cls))
        else:
            rel_path = dirname(input_path)
            input_file_name = splitext(basename(input_path))[0]
            dest = f"{rel_path}\\{input_file_name}.vm"
            with open(dest,"w") as f:
                for cls in self.parse(str_prog=read_file(input_path)):
                    f.write(str(cls))


    class_var_decl_types = set("static field".split())
    def is_class_var_decl(self, tk:Token):
        return tk.attr in self.class_var_decl_types

    subroutine_decl_types = set("constructor function method".split())
    def is_subroutine_decl(self, tk:Token):
        return tk.attr in self.subroutine_decl_types
    
    # type := 'int' | 'char' | 'boolean' | className
    jack_data_types = set("int char boolean".split())
    def is_valid_data_type(self, tk:Token):
        return tk.type == "keyword" and tk.attr in self.jack_data_types or \
            self.is_identifier(tk) # class var
    
    # type := 'int' | 'char' | 'boolean' | className
    def parse_type(self):
        tk = self.next_token()
        if not self.is_valid_data_type(tk):
            raise Exception(f"Unkown data types {tk}")
        return tk
    
    def is_identifier(self, tk:Token):
        return tk.type == "identifier"

    def parse_identifier(self):
        tk = self.next_token()
        if not self.is_identifier(tk):
            raise Exception(f"Exepect identifier {tk}")
        return tk
    
    def is_var_decl(self, tk:Token):
        return tk == Token("keyword", "var")

    variable_mapping = {
        "field": "this",
        "var": "local",
        "static": "static",
        "arg" : "argument"
    }
    # compile access variable
    def compile_pushpop_symbol(self, instruction, var_name):
        var_type = self.subroutine_symbol_table.type_of(var_name)
        var_kind = self.subroutine_symbol_table.kind_of(var_name)
        idx = self.subroutine_symbol_table.index(var_name)
        if var_type is None:
            var_type = self.class_symbol_table.type_of(var_name)
            var_kind = self.class_symbol_table.kind_of(var_name)
            idx = self.class_symbol_table.index(var_name)
        if var_type is None:
            # raise Exception(f"Warning: Unknown Type {var_name}")
            # print((f"Warning in {self.class_symbol_table.name}: Unknown Type {var_name}"))
            return None
        return f"{instruction} {self.variable_mapping[var_kind]} {idx}"
    
    #'var' type varName (',' varName)* ';'
    def compile_var_decl(self):
        '''
        add var declaration to subroutine symbol table

        return "" # empty string
        '''

        self.next_token() # discard var keyword
        dat_type = self.parse_type().attr
        var_name = self.parse_identifier().attr
        self.subroutine_symbol_table.add_symbol(var_name, dat_type, "var")

        curr_tkn = self.next_token()
        while curr_tkn != self.semicolon_token:
            if curr_tkn != self.comma_token:
                raise Exception(f"var declaration expects either , or ; but not {curr_tkn}")
            
            var_name = self.parse_identifier().attr
            self.subroutine_symbol_table.add_symbol(var_name, dat_type, "var")
            curr_tkn = self.next_token()
        
        return ""
    
    # ( type varName, (',' type varName)* )?
    # doesn't return enclosed
    # possibly empty
    # return type1 var1, .., typeN varN
    # also consume the right bracket
    def compile_parameter_list(self, subroutine_decl_type):
        '''
        add the parameters to the symbol table

        return "" # empty string
        '''

        # if empty parameter list
        if self.peek_next_token() == self.right_bracket_token: 
            self.next_token() # discard bracket token
            return ""

        if subroutine_decl_type.attr == "method":
            self.subroutine_symbol_table.add_symbol("this", self.class_symbol_table.name, "arg")
        
        dat_type = self.parse_type().attr
        arg_name = self.parse_identifier().attr
        self.subroutine_symbol_table.add_symbol(arg_name, dat_type, "arg")

        curr_tkn = self.next_token()
        while curr_tkn != self.right_bracket_token:
            if curr_tkn != self.comma_token:
                raise Exception(f"parameter list expects either ending ) or , but not {curr_tkn}")
            
            dat_type = self.parse_type().attr
            arg_name = self.parse_identifier().attr
            self.subroutine_symbol_table.add_symbol(arg_name, dat_type, "arg")

            curr_tkn = self.next_token()
        
        return ""

    
    def is_valid_return_type(self, tk:Token):
        return self.is_valid_data_type(tk) or \
            tk == Token("keyword", "void")
    
    # ('constructor'| 'function'| 'method') ('void'| type) subroutineName '(' parameterList ')' subroutineBody
    # subroutine_decl_type return_type subroutineName '(' parameterList ')' subroutineBody
    def compile_subroutine_decl(self):
        # not need to check as 
        # it has been checked before calling this function
        subroutine_decl_type = self.next_token()
        subroutine_return_type = self.next_token()

        if not self.is_valid_return_type(subroutine_return_type):
            raise Exception(f"Uknown return type {subroutine_return_type}")
        
        subroutine_name = self.parse_identifier()
        self.subroutine_symbol_table = Symbol_Table(self.class_symbol_table.name + "." + subroutine_name.attr)

        if self.next_token() != self.left_bracket_token:
            raise Exception(f"subroutine expects ( here")
        
        # not to put them in the ParseTree constructor
        # to ensure params, body are evaluated in order
        self.compile_parameter_list(subroutine_decl_type)
        body = self.compile_subroutine_body()
        
        # vm note: function functionName nVars
        # not nArgs

        if subroutine_decl_type.attr == "constructor":
            return "\n".join([
                f"function {self.class_symbol_table.name}.{subroutine_name.attr} {self.subroutine_symbol_table.count_of('var')}",
                f"push constant {self.class_symbol_table.count_of('field')}",
                f"call Memory.alloc 1",
                f"pop pointer 0",
                body
            ])
        elif subroutine_decl_type.attr == "method":
            return "\n".join([
                f"function {self.class_symbol_table.name}.{subroutine_name.attr} {self.subroutine_symbol_table.count_of('var')}",
                f"push argument 0",
                f"pop pointer 0",
                body
            ])
        return "\n".join([
            f"function {self.class_symbol_table.name}.{subroutine_name.attr} {self.subroutine_symbol_table.count_of('var')}",
            body
        ])
    # subroutineBody :=
    # '{' varDec* statements '}'
    # varDec and statements can be interleaved,
    # requiring different treatment
    def compile_subroutine_body(self):
        self.flow_label_count = count(0) # if-goto, goto, label counts
        
        if self.next_token() != self.left_curly_bracket_token:
            raise Exception("subroutine body expect { here")
        
        curr_tkn = self.peek_next_token() # the token is required for compile_statements
        body = []
        
        while curr_tkn != self.right_curly_bracket_token:
            if self.is_var_decl(curr_tkn):
                self.compile_var_decl()
                curr_tkn = self.peek_next_token() # next token might be a statement
            else:
                prog = self.compile_statements()
                if prog != "":
                    body.append(prog) 
                curr_tkn = self.next_token() # compile_statements stops at non-statement token
            
        return "\n".join(body) if body != [] else ""

    # ('static' | 'field' ) type varName (',' varName)* ';'
    def compile_class_var_decl(self):
        '''
            add class variables to class symbol table

            return "" # empty string
        '''
        
        lifetime_type = self.next_token().attr # not need to check
        dat_type = self.parse_type().attr
        var_name = self.parse_identifier().attr
        self.class_symbol_table.add_symbol(var_name, dat_type, lifetime_type)

        curr_tkn = self.next_token()
        while curr_tkn == self.comma_token and curr_tkn !=  self.semicolon_token:
            var_name = self.parse_identifier().attr
            self.class_symbol_table.add_symbol(var_name, dat_type, lifetime_type)
            curr_tkn = self.next_token()
        
        return ""

    # 'class' className '{' classVarDec* subroutineDec* '}'
    def compile_class(self):
        self.next_token() # discard the class keyword

        class_name = self.parse_identifier()
        self.class_symbol_table = Symbol_Table(class_name.attr) # class_name also signify a type

        if self.next_token() != self.left_curly_bracket_token:
            raise Exception("class expects { here")

        class_body = []
        curr_tkn = self.peek_next_token()
        while curr_tkn != self.right_curly_bracket_token:
            if self.is_class_var_decl(curr_tkn):
                self.compile_class_var_decl()
                # class_body.append(self.compile_class_var_decl())
            elif self.is_subroutine_decl(curr_tkn):
                class_body.append(self.compile_subroutine_decl())
            else:
                raise Exception(f"Unkown tokens {curr_tkn} in compiling class")
            curr_tkn = self.peek_next_token()
        
        self.next_token() # discard the bracket

        return "\n".join(class_body) if class_body != [] else ""
    
    def compile_statements(self):
        statement_kw_corpsd = {
            "let": self.compile_let_stmt,
            "if": self.compile_if_stmt,
            "while": self.compile_while_stmt,
            "do": self.compile_do_stmt,
            "return": self.compile_return_stmt
        }

        stmts = []
        nxt_tk = self.next_token()
        compile_fn = statement_kw_corpsd.get(nxt_tk.attr, False)

        while compile_fn != False:
            stmts.append(compile_fn())
            nxt_tk = self.next_token()
            compile_fn = statement_kw_corpsd.get(nxt_tk.attr, False)
        
        # put back the token that's not a statement keyword
        self.put_back_token(nxt_tk) 

        return "\n".join(stmts) if stmts != [] else ""
    
    # 'let' varName ('[' expr ']')? '=' expr ';'
    def compile_let_stmt(self):
        var_name = self.parse_identifier().attr
        curr_tkn = self.next_token()
        
        if curr_tkn == self.left_square_bracket_token: # for array, it requires special treatment
            opt_expr = self.compile_expression()
            if self.next_token() != self.right_square_bracket_token:
                raise Exception(f"let statement expects ]")
            if self.next_token() != self.equal_token:
                raise Exception(f"let statement expects =, not {curr_tkn}")
            expr = self.compile_expression()

            if self.next_token() != self.semicolon_token:
                raise Exception(f"let statement expects ending ;")
            return '\n'.join([
                opt_expr,
                self.compile_pushpop_symbol("push", var_name),
                "add",
                expr,
                "pop temp 0",
                "pop pointer 1",
                "push temp 0",
                "pop that 0"
            ])
        
        if curr_tkn != self.equal_token:
            raise Exception(f"let statement expects =, not {curr_tkn}")
        expr = self.compile_expression()
        if self.next_token() != self.semicolon_token:
                raise Exception(f"let statement expects ending ;")
        return expr + '\n' +\
                self.compile_pushpop_symbol("pop", var_name)
    
    # left compiler() right
    def parse_enclosed_helper(self, parser, pair, caller):
        if self.next_token() != pair[0]:
                raise Exception(f"{caller} expects {pair[0]} here")
        res = parser()
        if self.next_token() != pair[1]:
            raise Exception(f"{caller} expects {pair[1]} here")
        return [pair[0], res, pair[1]]
    def compile_enclosed_helper(self, compiler, pair, caller):
        if self.next_token() != pair[0]:
                raise Exception(f"{caller} expects {pair[0]} here")
        res = compiler()
        if self.next_token() != pair[1]:
            raise Exception(f"{caller} expects {pair[1]} here")
        return res
        

    # 'if' '(' expr ')' '{' statements '}' ( 'else' '{' statements '}')
    def compile_if_stmt(self):
        cond_expr = self.compile_enclosed_helper(self.compile_expression, self.bracket_token_pair, "if expression")
        stmts = self.compile_enclosed_helper(self.compile_statements, self.curly_bracket_token_pair, "if statements")
        if_lbl_num = next(self.flow_label_count)
        
        if self.peek_next_token() == Token("keyword", "else"):
            self.next_token() # discard else keyword
            else_stmts = self.compile_enclosed_helper(self.compile_statements, self.curly_bracket_token_pair, "else statements")
            return '\n'.join([
                cond_expr,
                f"if-goto IF_TRUE{if_lbl_num}",
                f"goto IF_FALSE{if_lbl_num}",
                f"label IF_TRUE{if_lbl_num}",
                stmts,
                f"goto IF_END{if_lbl_num}",
                f"label IF_FALSE{if_lbl_num}",
                else_stmts,
                f"label IF_END{if_lbl_num}"
            ]) 
            # another form
            return '\n'.join([
                cond_expr,
                "not",
                f"if-goto IF_ALT{if_lbl_num}",
                stmts,
                f"goto IF_END{if_lbl_num}",
                f"label IF_ALT{if_lbl_num}",
                else_stmts,
                f"label IF_END{if_lbl_num}"
            ])
        return '\n'.join([
            cond_expr,
            f"if-goto IF_TRUE{if_lbl_num}",
            f"goto IF_END{if_lbl_num}",
            f"label IF_TRUE{if_lbl_num}",
            stmts,
            f"label IF_END{if_lbl_num}"
        ])
        # another form
        return '\n'.join([
            cond_expr,
            "not", 
            f"if-goto IF_END{if_lbl_num}",
            stmts,
            f"goto IF_END{if_lbl_num}",
            f"label IF_END{if_lbl_num}"
        ])
    
    # 'while' '(' expr ')' '{' statements '}'
    def compile_while_stmt(self):
        while_lbl_num = next(self.flow_label_count)
        while_expr = self.compile_enclosed_helper(self.compile_expression, self.bracket_token_pair, "while expression")
        stmts = self.compile_enclosed_helper(self.compile_statements, self.curly_bracket_token_pair, "while statements")
        
        return '\n'.join([
                f"label WHILE_EXP{while_lbl_num}",
                while_expr,
                "not",
                f"if-goto WHILE_END{while_lbl_num}",
                stmts,
                f"goto WHILE_EXP{while_lbl_num}",
                f"label WHILE_END{while_lbl_num}"
            ])

    # 'do' subroutineCall ';'
    # subroutineCall returned value is cleaned after calling
    def compile_do_stmt(self):
        subroutine_call = self.compile_subroutine_call()
        nxt_tk = self.next_token()
        if nxt_tk != self.semicolon_token:
            raise Exception(f"do statement expects ending ; not {nxt_tk}")
        return f"{subroutine_call}\npop temp 0"

    # 'return' expression? ';'
    def compile_return_stmt(self):
        if self.peek_next_token() != self.semicolon_token:
            expr = self.compile_expression()
            if self.next_token() != self.semicolon_token:
                raise Exception("no ending ; after return statment")
            return expr + "\nreturn"
        
        self.next_token() # discard the semicolon
        # return; must return something (garbage)
        return f"push constant 0\nreturn"
    
    # handling expression
    keyword_constant_set = set("true false null this".split())
    def is_keyword_constant(self, tk:Token):
        return tk.type == "keyword" and tk.attr in self.keyword_constant_set
        
    bi_op_set = set("+ - * / & | < > =".split())
    def is_op(self, tk:Token):
        return tk.type == "symbol" and tk.attr in self.bi_op_set
    
    uni_op_set = set(['~', '-'])
    def is_uni_op(self, tk:Token):
        return tk.type == "symbol" and tk.attr in self.uni_op_set
    jack_vm_bi_op_corspd = {
        "+" : "add",
        "-" : "sub",
        "*" : "call Math.multiply 2",
        "/" : "call Math.divide 2",
        "=" : "eq",
        "<" : "lt",
        ">" : "gt",
        "&" : "and",
        "|" : "or"
        # more primitives here
    }
    jack_vm_uni_op_corspd ={
        "-": "neg",
        "~": "not"
        # more primitives here
    }
    # term (op term)*
    def compile_expression(self):
        first_term = self.compile_term()
        
        nxt_tk = self.peek(0)
        if self.is_op(nxt_tk):
            op = self.next_token().attr	
            return "\n".join([
                first_term,
                self.compile_term(),
                self.jack_vm_bi_op_corspd[op]
            ])
        else:
            return first_term
        
    # contain too many cases (8), pls refer to doc
    def compile_term(self):
        tk = self.peek(0)
        if tk.type == "integerConstant": 
            return f"push constant {self.next_token().attr}"
        elif tk.type == "stringConstant": 
            str_val = self.next_token().attr
            append_char_helper = lambda c : '\n'.join([
                f"push constant {ord(c)}",
                f"call String.appendChar 2"
                # f"\t// {c}"
            ])
            return '\n'.join([
                # f'// "{str_val}"',
                f"push constant {len(str_val)}",
                f"call String.new 1",
            ]+[append_char_helper(c) for c in str_val])
        elif self.is_keyword_constant(tk):
            kw_inst_mapping = {
                "null" : "push constant 0",
                "false" : "push constant 0",
                "true" : "push constant 0\nnot", # another form: "push constant 1\nneg"
                "this" : "push pointer 0"
            }
            kw_const = self.next_token().attr
            return kw_inst_mapping[kw_const]
        # '(' expr ')'
        elif tk == self.left_bracket_token:
            self.next_token() # skip bracket
            expr = self.compile_expression()
            if self.next_token() != self.right_bracket_token:
                raise Exception("compile_term error expects right bracket")
            return expr
        # unaryOp term
        elif self.is_uni_op(tk):
            unaryOp = self.next_token().attr
            return self.compile_term() + '\n' + self.jack_vm_uni_op_corspd[unaryOp]

        nxt_tk = self.peek_next_token()
        # varName'[' expr ']'
        if nxt_tk == self.left_square_bracket_token:
            var_name = self.parse_identifier().attr
            self.next_token()
            expr = self.compile_expression()

            if self.next_token() != self.right_square_bracket_token:
                raise Exception("array variable expected ending ]")
            
            return '\n'.join([
                expr,
                self.compile_pushpop_symbol("push", var_name),
                "add",
                "pop pointer 1",
                "push that 0" # push the value of arr[expr] to the stack
            ])
        # subroutine_call
        elif nxt_tk == self.left_bracket_token or nxt_tk == self.dot_token:
            return self.compile_subroutine_call()
        else: # this complicates the compile_expression
            var_name = self.parse_identifier().attr
            return self.compile_pushpop_symbol("push", var_name)
    
    # subroutineName '(' expressionList ') |
    # (className| varName) '.' subroutineName '(' expressionList ')'
    def compile_subroutine_call(self):
        subroutine_name = self.parse_identifier()
        curr_tkn = self.next_token()
        if curr_tkn == self.dot_token:
            obj_name = subroutine_name
            subroutine_name = self.parse_identifier()
            curr_tkn = self.next_token()

            if curr_tkn != self.left_bracket_token:
                raise Exception(f"COMPILE_SUBROUTINE_CALL: Unknown token {curr_tkn}")
            
            expr_li = self.compile_expr_list()
            push_obj_instruction = self.compile_pushpop_symbol("push", obj_name.attr)
            implicit_count = 0 if push_obj_instruction is None else 1
            push_obj_instruction = [] if push_obj_instruction is None else [push_obj_instruction]
            # translate the OOP to Procedural Code
            # found obj_type in subroutine scope
            # if not found, then proceed to class level
            # use the obj_name as type if nothing is found
            obj_type = self.subroutine_symbol_table.type_of(obj_name.attr)
            obj_type = obj_type if obj_type is not None else self.class_symbol_table.type_of(obj_name.attr)
            obj_type = obj_type if obj_type is not None else obj_name.attr
            return '\n'.join(
                push_obj_instruction +
                expr_li +
                [f"call {obj_type}.{subroutine_name.attr} {len(expr_li)+implicit_count}"]
            )
        elif curr_tkn == self.left_bracket_token:
            # push the current class implicitly by default
            push_instruction = self.subroutine_symbol_table.kind_of("this")
            expr_li = self.compile_expr_list()
            # if push_instruction is not None:
            # 	print(Warning("no object is specified for calling method; using current class"))
            # 	print(f"call {self.class_symbol_table.name}.{subroutine_name.attr} {len(expr_li)+1}")
            # 	push_instruction = "push argument 0"
            # 	push_instruction += "\npush pointer 0"
            # else:
            # 	push_instruction = "push pointer 0"

            # "push pointer 0", # push the current class implicitly by default
            push_instruction = "push pointer 0"
            return '\n'.join(
                [push_instruction] +
                expr_li +
                [f"call {self.class_symbol_table.name}.{subroutine_name.attr} {len(expr_li)+1}"]
            )
        else:
            raise Exception(f"compile_subroutine_call error {curr_tkn}")


    # doesn't return enclosed
    # (expr (',' expr)*)?
    # return a list rather a str
    def compile_expr_list(self): 
        '''
        return a list of compiled push instructions
        '''
        expr_li = []
        curr_tk = self.peek_next_token()
        if curr_tk != self.right_bracket_token: # if not empty
            expr_li.append(self.compile_expression())
            curr_tk = self.next_token()
            while curr_tk != self.right_bracket_token and curr_tk == self.comma_token:
                expr_li.append(self.compile_expression())
                curr_tk = self.next_token()
        else:
            self.next_token() # discard the bracket
        return expr_li
        
