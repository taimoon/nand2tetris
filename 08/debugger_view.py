def read_file(path):
	res = ""
	with open(path, "r") as f:
		res = f.read()
	return res

def numerise(asm):
	from itertools import count
	gen = count()
	lines = [line for line in asm.split("\n") if line != ""]
	for idx, line in enumerate(lines):
		if line[0] not in ["\n", "/", "("]:
			lines[idx] = f"{next(gen)} ##### {lines[idx]}"
	
	return "\n".join(lines)

def debugise(path):
	name_of_file = lambda f : f[:f.rfind('.')]
	rel_path = path[:path.rfind("\\")]
	input_name = path[path.rfind("\\")+1:]
	input_name = name_of_file(input_name)
	output_name = input_name
	output_name = "DEBUG_"+output_name+".txt"
	with open(rel_path+"\\"+output_name, "w") as f:
		f.write(numerise(read_file(path)))
	return rel_path+"\\"+output_name
path = r"C:\Programming\nand2tetris\projects\08\FunctionCalls\FibonacciElement\FibonacciElement.asm"
debugise(path)