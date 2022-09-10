str_comp_corspd = """0 101010
1 111111
-1 111010
D 001100
A 110000 M
!D 001101
!A 110001 !M
-D 001111
-A 110011 -M
D+1 011111
A+1 110111 M+1
D-1 001110
A-1 110010 M-1
D+A 000010 D+M
D-A 010011 D-M
A-D 000111 M-D
D&A 000000 D&M
D|A 010101 D|M"""

comp_corspd = [inst.split(' ') for inst in str_comp_corspd.split('\n')]
a0_corspd = {inst[0]:'0'+inst[1] for inst in comp_corspd}
a1_corspd = {inst[-1]:'1'+inst[1] for inst in comp_corspd if len(inst) == 3}
COMP_INSTRUCTION_CORSPD = a0_corspd | a1_corspd

JMP_INSTRUCTION_CORSPD = "NULL JGT JEQ JGE JLT JNE JLE JMP".split()
JMP_INSTRUCTION_CORSPD = {inst:bin(idx)[2:].zfill(3) for idx,inst in enumerate(JMP_INSTRUCTION_CORSPD)}

PREDEFINED_SYMBOL_TBL = {}
REG_COUNT = 16
PREDEFINED_SYMBOL_TBL["SCREEN"] = 16384
PREDEFINED_SYMBOL_TBL["KBD"] = 24576
VAR_ADDR_OFFSET = REG_COUNT
VAR_NUM_MAX = PREDEFINED_SYMBOL_TBL["SCREEN"]-REG_COUNT+1
for addr, sym in enumerate("SP LCL ARG THIS THAT".split()):
    PREDEFINED_SYMBOL_TBL[sym] = addr
for addr in range(REG_COUNT):
    PREDEFINED_SYMBOL_TBL[f"R{addr}"] = addr 
'''
refer to chap 4 for additional infomation
A-instruction := @value
bin: 0vvv vvvv vvvv vvvv 
will be store to A register

C-instruction := dest=comp;jump
bin: 111a cccc ccdd djjj
a := mnemonic pair
cccc cc := computation code
ddd := dest
jjj := jmp
dest or jump may be empty
if dest is empty, the "=" is omitted
if jump is empty, the ";" is omitted

if a == 0, then it is about between A and D
if a == 1, then it is about between D and M

ddd = [A,M,D] 
where if d_i == 1, 
then the value will be stored to register

D - name of register; where data lies
A - name of register; can be used to address
M - memory location addressed by A such that M[A]
'''

def read_file(path):
    res = ""
    with open(path, "r") as f:
        res = f.read()
    return res

def parse(str_prog):
    def rm_cmd(line):
        if line.find('//') != -1:
            return line[0:line.find('//')]
        return line
    str_prog = str_prog.split("\n")
    str_prog = list(map(rm_cmd,str_prog))
    str_prog = [i.strip().replace(' ', '').replace('\t','') for i in str_prog if i != '']
    return str_prog

def filter_scan_symbol(tokens):
    from itertools import count
    is_label = lambda line : line[0] == '(' and line[-1] == ')'
    label = lambda str : str[1:-1]
    symbol = lambda line: line[1:]
    sym_tbl = PREDEFINED_SYMBOL_TBL
    lbl_counter = count()
    sym_tbl =  sym_tbl | {label(sym):pc-next(lbl_counter) for pc,sym in enumerate(tokens) if is_label(sym)}
    var_counter = count(VAR_ADDR_OFFSET)
    for line in tokens:
        if line[0] == '@' and not line[1:].isdigit() and symbol(line) not in sym_tbl:
            sym_tbl[symbol(line)] = next(var_counter)
    res = [line for line in tokens if not is_label(line)]
    return sym_tbl, res

def analyze(token, env):
    if token[0] == '@': 
        val = token[1:]
        if val.isdigit():
            val = int(val)
        else:
            val = env[val]
        val = bin(val)[2:]
        return val.zfill(16)
    else:
        return analyze_c_instruction(token)

def analyze_c_instruction(token):
    jmp = "000"
    dest = "000"
    comp = ""
    comp_start = 0
    comp_end = len(token)
    if token.find("=") != -1:
        dest = dest2bin(token[0:token.find("=")])
        comp_start = token.find("=")+1
    if token.find(";") != -1:
        jmp = jmp2bin(token[token.find(';')+1:])
        comp_end = token.find(";")
    comp = comp2bin(token[comp_start:comp_end])
    return '111'+comp+dest+jmp

def jmp2bin(jmp):
    return JMP_INSTRUCTION_CORSPD[jmp]

def comp2bin(comp):
    if 'A' in comp and 'M' in comp:
        raise("ambigous A and M")
    commutative_ops = ["+", "&", "|"]
    for op in commutative_ops:
        if op+"D" in comp:
            comp = comp[-1]+op+comp[0]
            break
    return COMP_INSTRUCTION_CORSPD[comp]

def dest2bin(dest):
    b = [0 for _ in range(3)]
    if 'A' in dest:
        b[0] = 1
    if 'D' in dest:
        b[1] = 1
    if 'M' in dest:
        b[2] = 1
    b = [str(i) for i in b]
    return ''.join(b)

def assemble(str_prog):
    str_prog = parse(str_prog)
    sym_tbl, str_prog = filter_scan_symbol(str_prog)
    hack_txt = list(map(lambda line:analyze(line,sym_tbl),str_prog))
    hack_txt = '\n'.join(hack_txt)
    return hack_txt

def writer(path):
    rel_path = path[:path.rfind("\\")]
    output_name = path[path.rfind("\\")+1:]
    output_name = output_name[:output_name.rfind(".")]+".hack"
    hack_txt = assemble(read_file(path))
    with open(rel_path+"\\"+output_name, "w") as f:
        f.write(hack_txt)


if __name__ == "__main__":
    from sys import argv
    if len(argv) != 2:
        raise Exception("Unknown argv")
    writer(argv[1])
