def debug_print(item):
	print(item)
	return item

keywords = ['class', 'constructor', 'function', 'method', 'field', 'static', 'var', 'int', 'char', 'boolean', 'void', 'true', 'false', 'null', 'this', 'let', 'do', 'if', 'else', 'while', 'return']
keywords_grp_regex = "(" + "|".join(keywords) + ")"

symbols = ['{', '}', '(', ')', '[', ']', '.', ',', ';',':', '+', '-', '*', '/', '&', '|', '<', '>', '=', '~']
symbols_grp_regex = "".join([f"\\{symbol}" for symbol in symbols])
symbols_grp_regex = f"[{symbols_grp_regex}]"

'''
Tokenizing lexical elements:
	there is no exception in skipping whitespaces
	integerConstant: a decimal number in the range 0 ... 32767
	StringConstant: '"' a sequence of Unicode characters,
	not including double quote or newline '"'
	identifier:
	a sequence of letters, digits, and underscore 
	not starting with a digit
	cannot contains symbols
'''
# writing grammar rules, correspondences
# terminals

def read_file(path):
	res = ""
	with open(path, "r") as f:
		res = f.read()
	return res

class Token:
	# escape_corpsd = {
	# 	"<" : "&lt;",
	# 	">" : "&gt;",
	# 	"&" : "&amp;"
	# }
	def __init__(self, type, attr):
		self.type = type
		self.attr= attr
		# if attr in self.escape_corpsd:
		# 	self.attr = self.escape_corpsd[attr]
	def tagging(self, tag, content):
		return f"<{tag}> {content} </{tag}>"
	def to_xml(self):
		return self.tagging(self.type, self.attr)
	def __str__(self):
		return self.to_xml()
	def __repr__(self) -> str:
		return self.to_xml()
	def __eq__(self, __o: object) -> bool:
		return self.type == __o.type and self.attr == __o.attr

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
				res = f"{res}\n{attr}"
		if self.type == "":
			return res.lstrip()
		return f"<{self.type}> {res}\n</{self.type}>"
	def __repr__(self):
		return self.to_xml()
	def __str__(self):
		return self.to_xml()



def tokenizer(prog):
	import re
	# the order is particularly important here; from left to right; from up to bottom
	token_spec = [
		("multiline_comment", r"/\*[^*]*\*+(?:[^/*][^*]*\*+)*/"),
		("comment", r"//.+"),
		("skip", r"\s+"),
		("integerConstant", r"\d+"),
		("stringConstant", r'\"(.+)\"'),
		("keyword", keywords_grp_regex),
		("identifier", r"\w[\w\d]*"),
		("symbol", symbols_grp_regex),
		("mismatch", r".+")
	]
	tok_regex = "|".join("(?P<%s>%s)" % corspd for corspd in token_spec)
	for tkn in re.finditer(tok_regex, prog):
		kind = tkn.lastgroup
		val = tkn.group()
		if kind in set(["skip", "comment", "multiline_comment"]):
			continue
		elif kind == "mismatch":
			raise RuntimeError(f"{val!r}  unexpected token")
		elif kind == "stringConstant":
			yield Token(kind, val[1:-1])
		else:
			yield Token(kind, val)

class buffer_tokenizer(): # buffer that used queue data structure
	def __init__(self, prog):
		self.tokenizer = tokenizer(prog)
		self.buffer = []

	def put_back_token(self, tk:Token):
		self.buffer = [tk] + self.buffer

	def peek_next_token(self):
		self.buffer.append(next(self.tokenizer))
		return self.buffer[-1] # it is useful to see lastest push rather earliest

	def next_token(self):
		if self.buffer != []:
			return self.buffer.pop(0)
		else:
			return next(self.tokenizer)

	def __iter__(self):
		return self # what the hell
	
	def __next__(self):
		return self.next_token()
	
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
	
	def __init__(self, path):
		self.input_path = path
	
	def parse(self, symbol_tbl = None, str_prog = ""):
		if symbol_tbl is None:
			self.symbol_tbl = {}
		
		if str_prog == "":
			self.tokenizer = buffer_tokenizer(read_file(self.input_path))
		else:
			self.tokenizer = buffer_tokenizer(str_prog)
		
		self.prog = []
		try:
			while self.next_token() == Token("keyword", "class"):
				self.prog.append(self.compile_class())
		except StopIteration:
			return self.prog
	
	def write(self, path = ""):
		if path != "":
			self.input_path = path
		
		from os.path import dirname, basename, isdir
		name_of_file = lambda f : f[:f.rfind('.')]
		ext_of_file = lambda f : f[f.rfind('.')+1:]
		if isdir(self.input_path):
			from os import listdir
			
			rel_path = self.input_path
			jack_code_files = listdir(self.input_path)
			jack_code_files = [f for f in jack_code_files if ext_of_file(f) == "jack"]
			self.symbol_tbl = {}
			for input_file in jack_code_files:
				jack_code_file = f"{rel_path}\\{input_file}"
				dest = f"{rel_path}\\{name_of_file(input_file)}_COMPILED_TENGMAN.xml"
				with open(dest, "w") as f:
					for cls in self.parse(self.symbol_tbl, read_file(jack_code_file)):
						f.write(str(cls))
		else:
			rel_path = dirname(self.input_path)
			# input_file_name = splitext(basename(self.input_path))[0]
			input_file_name = name_of_file(basename(self.input_path))
			dest = f"{rel_path}\\{input_file_name}_TENGMAN.xml"
			with open(dest,"w") as f:
				for cls in self.parse():
					f.write(str(cls))

	def next_token(self) -> Token:
		return self.tokenizer.next_token()
	
	def peek_next_token(self) -> Token:
		return self.tokenizer.peek_next_token()

	class_var_decl_types = set("static field".split())
	def is_class_var_decl(self, tk:Token):
		return tk.attr in self.class_var_decl_types

	
	subroutine_decl_types = set("constructor function method".split())
	def is_subroutine_decl(self, tk:Token):
		return tk.attr in self.subroutine_decl_types
	
	# 'int' | 'char' | 'boolean' | className
	jack_data_types = set("int char boolean".split())
	def is_valid_data_type(self, tk:Token):
		return tk.type == "keyword" and tk.attr in self.jack_data_types or \
			self.is_identifier(tk) # class var
			# tk.attr in self.symbol_tbl and self.symbol_tbl[tk.attr] == "class_var"

	def compile_type(self):
		tk = self.next_token()
		if not self.is_valid_data_type(tk):
			raise Exception(f"Unkown data types {tk}")
		return tk
	
	def is_identifier(self, tk:Token):
		return tk.type == "identifier"

	def compile_identifier(self, is_new = False):
		tk = self.next_token()
		if not self.is_identifier(tk):
			raise Exception(f"Exepect identifier {tk}")
		if is_new == True:
			self.symbol_tbl[tk.attr] = "class_var"
		return tk
	
	def is_var_decl(self, tk:Token):
		return tk == Token("keyword", "var")

	#'var' type varName (',' varName)* ';'
	def compile_var_decl(self):
		var_kw = Token("keyword","var")
		dat_type = self.compile_type()
		vars = [self.compile_identifier()]
		curr_tkn = self.next_token()
		while curr_tkn != self.semicolon_token:
			if curr_tkn != self.comma_token:
				raise Exception(f"var declaration expects either , or ; but not {curr_tkn}")
			vars.append(curr_tkn)
			vars.append(self.compile_identifier())
		vars.append(self.semicolon_token)
		return ParseTree("varDec", var_kw, dat_type, *vars)
	
	# ( type varName, (',' type varName)* )?
	# doesn't return enclosed
	# possibly empty
	# return type1 var1, .., typeN varN
	def compile_parameter_list(self):
		curr_tkn = self.peek_next_token()
		params = []
		if curr_tkn == self.right_bracket_token:
			self.next_token() # discard bracket token
			return ParseTree("parameterList", "")
		params = [self.compile_type(), self.compile_identifier()]
		curr_tkn = self.next_token()
		while curr_tkn != self.right_bracket_token:
			if curr_tkn != self.comma_token:
				raise Exception(f"parameter list expects either ending ) or , but not {curr_tkn}")
			params.extend([curr_tkn, self.compile_type(), self.compile_identifier()])
			curr_tkn = self.next_token()
		return ParseTree("parameterList", *params)

	
	def is_valid_return_type(self, tk:Token):
		return self.is_valid_data_type(tk) or \
			tk == Token("keyword", "void") or \
			tk.attr in self.symbol_tbl
	# ('constructor'| 'function'| 'method') ('void'| type) subroutineName '(' parameterList ')' subroutineBody
	def compile_subroutine_decl(self):
		subroutine_decl_type = self.next_token()
		subroutine_return_type = self.next_token()
		if not self.is_valid_return_type(subroutine_return_type):
			raise Exception(f"Uknown return type {subroutine_return_type}")
		
		subroutine_name = self.compile_identifier()
		if self.next_token() != self.left_bracket_token:
			raise Exception(f"subroutine expects ( here")
		params = self.compile_parameter_list()
		body = self.compile_subroutine_body()
		return ParseTree("subroutineDec", subroutine_decl_type, subroutine_return_type, subroutine_name, 
						self.left_bracket_token, params, self.right_bracket_token, 
						body)

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
				self.next_token() # discard the token since compile_var_decl doesn't use it
				body.append(self.compile_var_decl())
				curr_tkn = self.peek_next_token() # next token might be statement
			else:
				body.append(self.compile_statements())
				curr_tkn = self.next_token() # compile_statements stops at non-statement token
		body.append(curr_tkn)
		return ParseTree("subroutineBody", self.left_curly_bracket_token, *body)

	# ('static' | 'field' ) type varName (',' varName)* ';'
	def compile_class_var_decl(self):
		lifetime_type = self.next_token()
		dat_type = self.compile_type()
		vars = [self.compile_identifier()]
		curr_tkn = self.next_token()
		while curr_tkn == self.comma_token and curr_tkn !=  self.semicolon_token:
			vars.append(curr_tkn)
			vars.append(self.compile_identifier())
			curr_tkn = self.next_token()
		vars.append(curr_tkn)
		return ParseTree("classVarDec", lifetime_type, dat_type, *vars)

	# 'class' className '{' classVarDec* subroutineDec* '}'
	def compile_class(self):
		class_kw = Token("keyword", "class")
		class_name = self.compile_identifier(is_new=True)
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
		self.tokenizer.put_back_token(nxt_tk)
		if stmts == []:
			return ParseTree("statements", "")
		return ParseTree("statements", *stmts)
	
	# 'let' varName ('[' expr ']')? '=' expr ';'
	def compile_let_stmt(self):
		let_kw = Token("keyword", "let")
		var_name = self.compile_identifier()
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
	
	# 'if' '(' expr ')' '{' statements '}' ( 'else' '{' statements '}')
	def compile_if_stmt(self):
		if_kw = Token("keyword", "if")
		if self.next_token() != self.left_bracket_token:
			raise Exception("if statement expects ( here")
		cond_expr = self.compile_expression()
		if self.next_token() != self.right_bracket_token:
			raise Exception("if statement expects ) here")
		if self.next_token() != self.left_curly_bracket_token:
			raise Exception(f"if statement expects {'{'} here")
		stmts = self.compile_statements()
		if self.next_token() != self.right_curly_bracket_token:
			raise Exception(f"if statement expects {'}'} here")
		args = [if_kw, 
				self.left_bracket_token, cond_expr, self.right_bracket_token, 
				self.left_curly_bracket_token, stmts, self.right_curly_bracket_token]
		if self.peek_next_token() == Token("keyword", "else"):
			else_kw = self.next_token()
			if self.next_token() != self.left_curly_bracket_token:
				raise Exception(f"else statement expects {'{'} here")
			else_stmts = self.compile_statements()
			if self.next_token() != self.right_curly_bracket_token:
				raise Exception(f"else statement expects {'}'} here")
			args.extend([else_kw, self.left_curly_bracket_token, else_stmts, self.right_curly_bracket_token])
		return ParseTree("ifStatement", *args)
	
	# 'while' '(' expr ')' '{' statements '}'
	def compile_while_stmt(self):
		while_kw = Token("keyword", "while")
		if self.next_token() != self.left_bracket_token:
			raise Exception("while statement expects ( here")
		cond_expr = self.compile_expression()
		if self.next_token() != self.right_bracket_token:
			raise Exception("while statement expects ) here")
		if self.next_token() != self.left_curly_bracket_token:
			raise Exception(f"while statement expects {'{'} here")
		stmts = self.compile_statements()
		if self.next_token() != self.right_curly_bracket_token:
			raise Exception(f"while statement expects {'}'} here")
		return ParseTree("whileStatement", while_kw, 
					self.left_bracket_token, cond_expr, self.right_bracket_token, 
					self.left_curly_bracket_token, stmts, self.right_curly_bracket_token)

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
		nxt_tk = self.peek_next_token()
		if self.is_op(nxt_tk):
			return ParseTree("expression", first_term, self.next_token(), self.compile_term())
		else:
			return ParseTree("expression", first_term)
		
	# contain too many cases (8), pls refer to doc
	def compile_term(self):
		tk = None
		if self.tokenizer.buffer != []: # if it has been peek, then use the first
			tk = self.tokenizer.buffer[0]
		else:
			tk = self.peek_next_token()
		# int and str constant
		if tk.type == "integerConstant" or tk.type == "stringConstant": 
			return ParseTree("term", self.next_token())
		# keyword constant
		elif self.is_keyword_constant(tk):
			return ParseTree("term", self.next_token())
		# '(' expr ')'
		elif tk == self.left_bracket_token:
			self.next_token() # skip bracket
			expr = self.compile_expression()
			if self.peek_next_token() != self.right_bracket_token:
				raise Exception("compile_term error expects right bracket")
			return ParseTree("term", self.left_bracket_token, expr, self.right_bracket_token)
		# unaryOp term
		elif self.is_uni_op(tk):
			return ParseTree("term", self.next_token(), self.compile_term())

		nxt_tk = self.peek_next_token()
		# varName'[' expr ']'
		if nxt_tk == self.left_square_bracket_token: 
			return ParseTree("term", tk, self.left_square_bracket_token, self.compile_expression(), self.right_square_bracket_token)
		# subroutine_call
		elif nxt_tk == self.left_bracket_token or nxt_tk == self.dot_token: 
			return ParseTree("term", self.compile_subroutine_call())
		else:
			return ParseTree("term", self.compile_identifier())
	
	# subroutineName '(' expressionList ') |
	# (className| varName) '.' subroutineName '(' expressionList ')'
	def compile_subroutine_call(self):
		subroutine_name = self.compile_identifier()
		curr_tkn = self.next_token()
		if curr_tkn == self.dot_token:
			obj_name = subroutine_name
			subroutine_name = self.compile_identifier()
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



def testTokenizer():
	path = r"C:\Programming\nand2tetris\projects\10\Square\Main.jack"
	path = r"C:\Programming\nand2tetris\projects\10\Square\Square.jack"
	path = r"C:\Programming\nand2tetris\projects\10\Square\SquareGame.jack"
	path = r"C:\Programming\nand2tetris\projects\10\ExpressionLessSquare\Main.jack"

	def write_tokens(path):
		from os.path import dirname, splitext, basename
		rel_path = dirname(path)
		input_file_name = splitext(basename(path))[0]
		dest = f"{rel_path}\\{input_file_name}T_TENGMAN.xml"
		with open(dest,"w") as f:
			f.write("<tokens>\n")
			for tkn in buffer_tokenizer(read_file(path)):
				f.write(str(tkn)+"\n")
			f.write("</tokens>")

	write_tokens(path)


path = r"C:\Programming\nand2tetris\projects\10\ExpressionLessSquare"
parser = Parser(path)
parser.write(path)
path = r"C:\Programming\nand2tetris\projects\10\Square"
parser.write(path)
