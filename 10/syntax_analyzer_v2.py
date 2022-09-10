from tokenizer import Token, buffer_tokenizer

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
				content = Token.escape_corpsd(attr, attr)
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
				dest = f"{rel_path}\\{name_of_file(input_file)}_COMPILED_TENGMAN.xml"
				with open(dest, "w") as f:
					for cls in self.parse(str_prog=read_file(jack_file)):
						f.write(str(cls))
		else:
			rel_path = dirname(input_path)
			input_file_name = splitext(basename(input_path))[0]
			dest = f"{rel_path}\\{input_file_name}_TENGMAN.xml"
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

	#'var' type varName (',' varName)* ';'
	def compile_var_decl(self):
		var_kw = self.next_token()
		dat_type = self.parse_type()
		vars = [self.parse_identifier()]
		curr_tkn = self.next_token()
		while curr_tkn != self.semicolon_token:
			if curr_tkn != self.comma_token:
				raise Exception(f"var declaration expects either , or ; but not {curr_tkn}")
			vars.append(curr_tkn)
			vars.append(self.parse_identifier())
			curr_tkn = self.next_token()
		vars.append(self.semicolon_token)
		return ParseTree("varDec", var_kw, dat_type, *vars)
	
	# ( type varName, (',' type varName)* )?
	# doesn't return enclosed
	# possibly empty
	# return type1 var1, .., typeN varN
	# also consume the right bracket
	def compile_parameter_list(self):
		if self.peek_next_token() == self.right_bracket_token: # empty parameter list
			self.next_token() # discard bracket token
			return ParseTree("parameterList", "")
		
		params = [self.parse_type(), self.parse_identifier()]
		curr_tkn = self.next_token()
		while curr_tkn != self.right_bracket_token:
			if curr_tkn != self.comma_token:
				raise Exception(f"parameter list expects either ending ) or , but not {curr_tkn}")
			params.extend([curr_tkn, self.parse_type(), self.parse_identifier()])
			curr_tkn = self.next_token()
		
		return ParseTree("parameterList", *params)

	
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
		
		if self.next_token() != self.left_bracket_token:
			raise Exception(f"subroutine expects ( here")
		# not to put them in the ParseTree constructor
		# to ensure params, body are evaluated in order
		params = self.compile_parameter_list()
		body = self.compile_subroutine_body()
		return ParseTree("subroutineDec", 
						subroutine_decl_type, subroutine_return_type, subroutine_name, 
						self.left_bracket_token, params, self.right_bracket_token, 
						body)

	# subroutineBody :=
	# '{' varDec* statements '}'
	# varDec and statements can be interleaved,
	# requiring different treatment
	def compile_subroutine_body(self):
		if self.next_token() != self.left_curly_bracket_token:
			raise Exception("subroutine body expect { here")
		
		curr_tkn = self.peek_next_token() # the token is required for compile_statements
		body = []
		while curr_tkn != self.right_curly_bracket_token:
			if self.is_var_decl(curr_tkn):
				body.append(self.compile_var_decl())
				curr_tkn = self.peek_next_token() # next token might be a statement
			else:
				body.append(self.compile_statements())
				curr_tkn = self.next_token() # compile_statements stops at non-statement token
		
		body.append(curr_tkn)
		
		return ParseTree("subroutineBody", self.left_curly_bracket_token, *body)

	# ('static' | 'field' ) type varName (',' varName)* ';'
	def compile_class_var_decl(self):
		lifetime_type = self.next_token() # not need to check
		dat_type = self.parse_type()
		vars = [self.parse_identifier()]
		curr_tkn = self.next_token()
		while curr_tkn == self.comma_token and curr_tkn !=  self.semicolon_token:
			vars.append(curr_tkn)
			vars.append(self.parse_identifier())
			curr_tkn = self.next_token()
		vars.append(curr_tkn)
		return ParseTree("classVarDec", lifetime_type, dat_type, *vars)

	# 'class' className '{' classVarDec* subroutineDec* '}'
	def compile_class(self):
		class_kw = self.next_token()
		class_name = self.parse_identifier()
		if self.next_token() != self.left_curly_bracket_token:
			raise Exception("class expects { here")
		
		class_body = []
		curr_tkn = self.peek_next_token()
		while curr_tkn != self.right_curly_bracket_token:
			if self.is_class_var_decl(curr_tkn):
				class_body.append(self.compile_class_var_decl())
			elif self.is_subroutine_decl(curr_tkn):
				class_body.append(self.compile_subroutine_decl())
			else:
				raise Exception(f"Unkown tokens {curr_tkn} in compiling class")
			curr_tkn = self.peek_next_token()
		
		self.next_token() # discard the bracket
		args = [class_kw, class_name, self.left_curly_bracket_token] + class_body + [self.right_curly_bracket_token]
		return ParseTree("class", *args)
	def compile_statements(self):
		statement_kw_corpsd = {
			"let": lambda self: self.compile_let_stmt(),
			"if": lambda self: self.compile_if_stmt(),
			"while": lambda self: self.compile_while_stmt(),
			"do": lambda self: self.compile_do_stmt(),
			"return": lambda self: self.compile_return_stmt()
		}
		stmts = []
		nxt_tk = self.next_token()
		compile_fn = statement_kw_corpsd.get(nxt_tk.attr, False)
		while compile_fn != False:
			stmts.append(compile_fn(self))
			nxt_tk = self.next_token()
			compile_fn = statement_kw_corpsd.get(nxt_tk.attr, False)
		# put back the token that's not a statement keyword
		self.put_back_token(nxt_tk) 
		if stmts == []:
			return ParseTree("statements", "")
		return ParseTree("statements", *stmts)
	
	# 'let' varName ('[' expr ']')? '=' expr ';'
	def compile_let_stmt(self):
		let_kw = Token("keyword", "let")
		var_name = self.parse_identifier()

		curr_tkn = self.next_token()
		if curr_tkn == self.left_square_bracket_token:
			opt_expr = self.compile_expression()

			if self.next_token() != self.right_square_bracket_token:
				raise Exception(f"let statement expects ]")
			if self.next_token() != self.equal_token:
				raise Exception(f"let statement expects =, not {curr_tkn}")
			expr = self.compile_expression()
			if self.next_token() != self.semicolon_token:
				raise Exception(f"let statement expects ending ;")
			return ParseTree("letStatement", let_kw, var_name, self.left_square_bracket_token, opt_expr, self.right_square_bracket_token, self.equal_token, expr, self.semicolon_token)
		
		if curr_tkn != self.equal_token:
			raise Exception(f"let statement expects =, not {curr_tkn}")
		expr = self.compile_expression()
		if self.next_token() != self.semicolon_token:
				raise Exception(f"let statement expects ending ;")
		return ParseTree("letStatement", let_kw, var_name, self.equal_token, expr, self.semicolon_token)
	
	# left compiler() right
	def parse_enclosed_helper(self, compiler, pair, caller):
		if self.next_token() != pair[0]:
				raise Exception(f"{caller} expects {pair[0]} here")
		res = compiler()
		if self.next_token() != pair[1]:
			raise Exception(f"{caller} expects {pair[1]} here")
		return [pair[0], res, pair[1]]

	# 'if' '(' expr ')' '{' statements '}' ( 'else' '{' statements '}')
	def compile_if_stmt(self):
		if_kw = Token("keyword", "if")
		cond_expr = self.parse_enclosed_helper(self.compile_expression, self.bracket_token_pair, "if expression")
		stmts = self.parse_enclosed_helper(self.compile_statements, self.curly_bracket_token_pair, "if statements")
		args = [if_kw] + cond_expr + stmts
		if self.peek_next_token() == Token("keyword", "else"):
			else_kw = self.next_token()
			else_stmts = self.parse_enclosed_helper(self.compile_statements, self.curly_bracket_token_pair, "else statements")
			args += [else_kw] + else_stmts
		return ParseTree("ifStatement", *args)
	
	# 'while' '(' expr ')' '{' statements '}'
	def compile_while_stmt(self):
		while_kw = Token("keyword", "while")
		cond_expr = self.parse_enclosed_helper(self.compile_expression, self.bracket_token_pair, "while expression")
		stmts = self.parse_enclosed_helper(self.compile_statements, self.curly_bracket_token_pair, "while statements")
		args = cond_expr + stmts
		return ParseTree("whileStatement", while_kw, *args)

	# 'do' subroutineCall ';'
	def compile_do_stmt(self):
		do_kw = Token("keyword", "do")
		subroutine_call = self.compile_subroutine_call()
		nxt_tk = self.next_token()
		if nxt_tk != self.semicolon_token:
			raise Exception(f"do statement expects ending ; not {nxt_tk}")
		return ParseTree("doStatement", do_kw, subroutine_call, self.semicolon_token)

	# 'return' expression? ';'
	def compile_return_stmt(self):
		ret_kw = Token("keyword", "return")
		if self.peek_next_token() != self.semicolon_token:
			expr = self.compile_expression()
			if self.next_token() != self.semicolon_token:
				raise Exception("no ending ; after return statment")
			
			return ParseTree("returnStatement", ret_kw, expr, self.semicolon_token)
		
		return ParseTree("returnStatement", ret_kw, self.next_token())
	
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

	# term (op term)*
	def compile_expression(self):
		first_term = self.compile_term()
		nxt_tk = self.peek(0)
		if self.is_op(nxt_tk):
			return ParseTree("expression", first_term, self.next_token(), self.compile_term())
		else:
			return ParseTree("expression", first_term)
		
	# contain too many cases (8), pls refer to doc
	def compile_term(self):
		tk = self.peek(0)
		if tk.type == "integerConstant" or tk.type == "stringConstant" or self.is_keyword_constant(tk): 
			return ParseTree("term", self.next_token())
		# '(' expr ')'
		elif tk == self.left_bracket_token:
			self.next_token() # skip bracket
			expr = self.compile_expression()
			if self.next_token() != self.right_bracket_token:
				raise Exception("compile_term error expects right bracket")
			return ParseTree("term", self.left_bracket_token, expr, self.right_bracket_token)
		# unaryOp term
		elif self.is_uni_op(tk):
			return ParseTree("term", self.next_token(), self.compile_term())

		nxt_tk = self.peek_next_token()
		# varName'[' expr ']'
		if nxt_tk == self.left_square_bracket_token:
			var_name = self.parse_identifier()
			self.next_token()
			expr = self.compile_expression()
			if self.next_token() != self.right_square_bracket_token:
				raise Exception("array variable expected ending ]")
			return ParseTree("term", var_name, self.left_square_bracket_token, expr, self.right_square_bracket_token)
		# subroutine_call
		elif nxt_tk == self.left_bracket_token or nxt_tk == self.dot_token: 
			return ParseTree("term", self.compile_subroutine_call())
		else: # this complicates the compile_expression
			return ParseTree("term", self.parse_identifier())
	
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
			# subroutineCall type
			return ParseTree("", obj_name, self.dot_token, subroutine_name, self.left_bracket_token, expr_li, self.right_bracket_token) 
		elif curr_tkn == self.left_bracket_token:
			return ParseTree("", subroutine_name, self.left_bracket_token, self.compile_expr_list(), self.right_bracket_token) 
		else:
			raise Exception(f"compile_subroutine_call error {curr_tkn}")


	# doesn't return enclosed
	# (expr (',' expr)*)?
	def compile_expr_list(self): 
		expr_li = []
		curr_tk = self.peek_next_token()
		if curr_tk != self.right_bracket_token:
			expr_li.append(self.compile_expression())
			curr_tk = self.next_token()
			while curr_tk != self.right_bracket_token and curr_tk == self.comma_token:
				expr_li.append(curr_tk)
				expr_li.append(self.compile_expression())
				curr_tk = self.next_token()
		if expr_li == []:
			self.next_token() # discard the bracket
			return ParseTree("expressionList", "")
		return ParseTree("expressionList", *expr_li)
