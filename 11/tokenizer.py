class Token:
	escape_corpsd = {
		"<" : "&lt;",
		">" : "&gt;",
		"&" : "&amp;"
	}
	def __init__(self, type, attr):
		self.type = type
		self.attr= attr

	def tagging(self, tag, content):
		return f"<{tag}> {content} </{tag}>"
	
	def to_xml(self):
		content = self.escape_corpsd.get(self.attr, self.attr)
		return self.tagging(self.type, content)
	
	def __str__(self):
		return self.to_xml()
	
	def __repr__(self) -> str:
		return self.to_xml()
	
	def __eq__(self, __o: object) -> bool:
		return self.type == __o.type and self.attr == __o.attr
'''
Tokenizing lexical elements:
	there is no exception in skipping whitespaces
	integerConstant: 
		a decimal number in the range 0 ... 32767
	StringConstant: 
		'"' a sequence of Unicode characters,
		not including double quote or newline '"'
	identifier:
		a sequence of letters, digits, and underscore 
		not starting with a digit
'''
keywords = ['class', 'constructor', 'function', 'method', 'field', 'static', 'var', 'int', 'char', 'boolean', 'void', 'true', 'false', 'null', 'this', 'let', 'do', 'if', 'else', 'while', 'return']
match_whole_word_regex = lambda word: f"\\b{word}\\b"
keywords_grp_regex = "(" + "|".join([match_whole_word_regex(w) for w in keywords ]) + ")"

symbols = ['{', '}', '(', ')', '[', ']', '.', ',', ';',':', '+', '-', '*', '/', '&', '|', '<', '>', '=', '~']
symbols_grp_regex = "".join([f"\\{symbol}" for symbol in symbols])
symbols_grp_regex = f"[{symbols_grp_regex}]"
def tokenizer(prog):
	import re
	# the order is particularly important here; from left to right; from up to bottom
	token_spec = [
		("multiline_comment", r"/\*[^*]*\*+(?:[^/*][^*]*\*+)*/"),
		("comment", r"//.+"),
		("skip", r"\s+"),
		("integerConstant", r"\d+"),
		("stringConstant", r'\"(.+)\"'),
		("keyword", keywords_grp_regex), # BUG HERE
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
		elif kind == "stringConstant":
			yield Token(kind, val[1:-1])
		elif kind == "mismatch":
			raise RuntimeError(f"{val!r}  unexpected token")
		else:
			yield Token(kind, val)

class buffer_tokenizer: # buffer that used queue data structure
	def __init__(self, prog):
		self.tokenizer = tokenizer(prog)
		self.buffer = []

	def put_back_token(self, tk:Token):
		self.buffer = [tk] + self.buffer

	def peek_next_token(self):
		self.buffer.append(next(self.tokenizer))
		return self.buffer[-1] # it is useful to see lastest push rather earliest

	def peek(self, pos = -1):
	# pos = -1 -> push and see
		if pos == -1:
			return self.peek_next_token()
		for _ in range(pos+1-len(self.buffer)):
			self.peek_next_token()
		return self.buffer[pos]

	def next_token(self):
		if self.buffer != []:
			return self.buffer.pop(0)
		else:
			return next(self.tokenizer)

	def __iter__(self):
		return self # what the hell
	
	def __next__(self):
		return self.next_token()



# def tokenizer(prog):
# 	import re
# 	# the order is particularly important here; from left to right; from up to bottom
# 	token_spec = [
# 		("multiline_comment", r"/\*[^*]*\*+(?:[^/*][^*]*\*+)*/"),
# 		("comment", r"//.+"),
# 		("skip", r"\s+"),
# 		("integerConstant", r"\d+"),
# 		("stringConstant", r'\"(.+)\"'),
# 		("keyword", keywords_grp_regex),
# 		("identifier", r"\w[\w\d]*"),
# 		("symbol", symbols_grp_regex),
# 		("mismatch", r".+")
# 	]
# 	tok_regex = "|".join("(?P<%s>%s)" % corspd for corspd in token_spec)
# 	for tkn in re.finditer(tok_regex, prog):
# 		kind = tkn.lastgroup
# 		val = tkn.group()
# 		if kind in set(["skip", "comment", "multiline_comment"]):
# 			continue
# 		elif kind == "mismatch":
# 			raise RuntimeError(f"{val!r}  unexpected token")
# 		elif kind == "stringConstant":
# 			yield Token(kind, val[1:-1])
# 		else:
# 			yield Token(kind, val)

# class buffer_tokenizer: # buffer that used queue data structure
# 	def __init__(self, prog):
# 		self.tokenizer = tokenizer(prog)
# 		self.buffer = []

# 	def put_back_token(self, tk:Token):
# 		self.buffer = [tk] + self.buffer

# 	def peek_next_token(self):
# 		self.buffer.append(next(self.tokenizer))
# 		return self.buffer[-1] # it is useful to see lastest push rather earliest

# 	def peek(self, pos = -1):
# 	# pos = -1 -> push and see
# 		if pos == -1:
# 			return self.peek_next_token()
# 		for _ in range(pos+1-len(self.buffer)):
# 			self.peek_next_token()
# 		return self.buffer[pos]

# 	def next_token(self):
# 		if self.buffer != []:
# 			return self.buffer.pop(0)
# 		else:
# 			return next(self.tokenizer)

# 	def __iter__(self):
# 		return self # what the hell
	
# 	def __next__(self):
# 		return self.next_token()