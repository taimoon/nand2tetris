from os.path import dirname, splitext,basename, isdir
import shutil
# this python file is to rename the compiled vm file by tools
# useful for direct comparison
def rename(input_path):
	if isdir(input_path):
		from os import listdir
		rel_path = input_path
		ext_of_file = lambda f : f[f.rfind('.')+1:]
		vm_files = [f for f in listdir(input_path) if ext_of_file(f) == "vm"]
		for input_file in vm_files:
			vm_file_src = f"{rel_path}\\{input_file}"
			name_of_file = lambda f : f[:f.rfind('.')]
			dest = f"{rel_path}\\{name_of_file(input_file)}_EXPECTED.txt"
			shutil.copy(vm_file_src, dest)
	else: #TODO
		rel_path = dirname(input_path)
		input_file_name = splitext(basename(input_path))[0]
		dest = f"{rel_path}\\{input_file_name}.vm"
rename(r"C:\Programming\nand2tetris\projects\11\Pong")
