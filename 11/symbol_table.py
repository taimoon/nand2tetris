class Jack_Variable:
	def __init__(self, name:str, type, kind, index = -1) -> None:
		self.name = name
		self.type = type
		self.kind = kind
		self.index = index
	def __repr__(self) -> str:
		return f"name = {self.name}, type = {self.type}, kind = {self.kind}, index = {self.index}" 


class Symbol_Table:
	
	def __init__(self, name = ""):
		self.name = name
		self.table = {}
		self.var_kind_tally = {kind:0 for kind in "static field arg var".split()}

	def add_symbol(self, name:str, type, kind):
		self.table[name] = Jack_Variable(name, type, kind, self.var_kind_tally[kind])
		self.var_kind_tally[kind] += 1

	def count_of(self, kind):
		return self.var_kind_tally[kind]

	def kind_of(self, name):
		res =  self.table.get(name, True)
		return None if res == True else res.kind
	
	def type_of(self, name):
		res =  self.table.get(name, True)
		return None if res == True else res.type

	def index(self, name):
		res =  self.table.get(name, True)
		return None if res == True else res.index
	
	def __repr__(self) -> str:
		res = f"table name = {self.name}"
		for sym in self.table.values():
			res += '\n{' + str(sym) + '}'
		return res
