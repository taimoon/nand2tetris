from itertools import count
def read_file(path):
    res = ""
    with open(path, "r") as f:
        res = f.read()
    return res


def is_command(token):
    return token[0] == '//'


def tokenize(vm_script):
    def rm_cmd(line):
        if line.find('//') != -1:
            return line[0:line.find('//')]
        return line
    lines = [rm_cmd(line) for line in vm_script.split('\n')]
    lines = [i.strip() for i in lines if i != '']
    lines = [line.split() for line in lines]
    return lines


def analyze(token, bool_counter:count):
    is_same_tag = lambda tkn, tag: tkn[0] == tag
    if is_same_tag(token, "push"):
        return push_prog(token[1], token[2])
    elif is_same_tag(token, "pop"):
        return pop_prog(token[1], token[2])
    else:
        return arithmetic_prog(token[0], bool_counter)


def arithmetic_prog(op, bool_counter:count):
    prog = ""
    bi_op_corspd = {"add": "+", "sub": "-","and": "&","or" : "|"}
    uni_op_corspd = {"neg":"-","not":"!"}
    if op in bi_op_corspd:
        prog = f"""
            @SP
            M=M-1	// SP = SP--
            A=M		// A = SP
            D=M		// D = *SP (second arg)
            A=A-1	// A = SP-1 (first arg)
            M=M{bi_op_corspd[op]}D	// *SP + *(SP-1)
        """
    elif op in uni_op_corspd:
        prog = f"""
            @SP
            A=M-1	// A = SP-1
            M={uni_op_corspd[op]}M
        """
    elif op in ["eq","lt", "gt"]:
        bool_n = next(bool_counter)
        jmp_inst = "J"+op.upper()
        prog = f"""
            @SP
            M=M-1	// SP = SP--
            A=M		// A = SP
            D=M		// D = *SP (second arg)
            A=A-1	// A = SP-1 (first arg)
            D=M-D
            @__BOOL{bool_n}
            D;{jmp_inst}
            @SP
            A=M-1
            M=0 // 0 represent false value
            @__ENDBOOL{bool_n}
            0;JMP
            (__BOOL{bool_n})
            @SP
            A=M-1
            M=-1
            (__ENDBOOL{bool_n})
        """
    else:
        raise(op)
    return prog.replace("\t","").strip()

seg_corspd = {"local":"LCL", "argument":"ARG", "this":"THIS", "that":"THAT"}
def push_prog(seg,val):
    val = int(val)
    if seg == "constant":
        return push_const_prog(val)
    elif seg == "temp":
        return push_temp_prog(val)
    elif seg == "pointer":
        return push_ptr_prog(val)
    elif seg == "static":
        return push_static_prog(val)
    elif seg in seg_corspd:
        return push_seg_prog(seg,val)
    
def push_const_prog(val):
    "IDEA: *SP = val, SP++"
    return f"""
    @{val} // A = val
    D=A
    @SP // A = SP
    A=M // A = RAM[A]
    M=D // RAM[A] = D
    @SP // A = SP
    M=M+1	// SP++ 
    """.replace("\t","").strip()
def push_temp_prog(val):
    "addr = 5+i, *SP = *addr, SP++"
    return f"""
    @5
    D=A
    @{val}
    A=A+D	// A = addr = 5 + val
    D=M		// D = *addr
    @SP // A = &SP
    A=M // A = SP
    M=D // *SP = D
    @SP // A = &SP
    M=M+1	// SP++ 
    """.replace("\t","").strip()


def push_seg_prog(seg,pos):
    "addr=seg+pos, *SP=*addr, SP++"
    seg = seg_corspd[seg]
    prog = f'''
        @{seg}
        D=M		// D={seg}
        @{pos}
        A=D+A	// A={seg}+{pos}
        D=M		// D=*({seg}+{pos})
        @SP
        A=M		// A = SP
        M=D		// *SP = D
        @SP
        M=M+1	// SP++
    '''.replace("\t","").strip()
    return prog

ptr_insts_tbl = ["THIS","THAT"]
def push_ptr_prog(n):
    "*SP = THIS/THAT, SP++"
    return f"""
    @{ptr_insts_tbl[n]}
    D=M	// D=THIS/THAT
    @SP
    A=M // A=SP
    M=D	// *SP = THIS/THAT
    @SP
    M=M+1	// SP++
    """.replace("\t","").strip()


def push_static_prog(pos):
    return f"""
    @{pos+16}
    D=M	// D=RAM[pos+16]
    @SP 
    A=M // A=SP
    M=D	// *SP = D
    @SP
    M=M+1	// SP++
    """.replace("\t","").strip()


def pop_prog(seg, pos):
    pos = int(pos)
    if seg in seg_corspd:
        return pop_seg_prog(seg,pos)
    elif seg == "temp":
        return pop_temp_prog(pos)
    elif seg == "pointer":
        return pop_ptr_prog(pos)
    elif seg == "static":
        return pop_static_prog(pos)


def pop_temp_prog(val):
    "addr=5+val, SP--, *addr=*SP"
    return f"""
    @5
    D=A
    @{val}
    D=A+D	// A = addr = 5 + val
    @SP
    M=M-1	// SP--
    A=M+1	// A = SP+1
    M=D		// *(SP+1) = addr
    @SP
    A=M		// A=SP
    D=M		// D=*SP
    @SP
    A=M+1	// A = SP+1
    A=M		// A = *(SP+1) = addr
    M=D		// *addr = *SP
    """.replace("\t","").strip()


def pop_seg_prog(seg,pos):
    "addr=seg+pos, SP--, *addr=*SP"
    seg=seg_corspd[seg]
    return f'''
        @{seg}
        D=M		// D={seg}
        @{pos}
        D=D+A	// D={seg}+{pos}=addr
        @SP
        M=M-1	// SP--
        A=M+1	// A = SP+1
        M=D		// *(SP+1) = addr
        @SP
        A=M		// A = SP
        D=M		// D = *SP
        @SP
        A=M+1	// A = SP+1
        A=M		// A = *(SP+1) = addr
        M=D		// *addr = *SP
    '''.replace("\t","").strip()


def pop_ptr_prog(n):
    "SP--, THIS/THAT = *SP"
    return f"""
    @SP
    M=M-1 	// SP--
    A=M		// A=SP
    D=M		// D=*SP
    @{ptr_insts_tbl[n]}
    M=D		// THIS/THAT = *SP
    """.replace("\t","").strip()


def pop_static_prog(pos):
    return f"""
    @SP
    M=M-1	// SP--
    A=M		// A=SP
    D=M		// D=*SP
    @{pos+16}
    M=D		// RAM[POS+16] = D = *SP
    """.replace("\t","").strip()


def translate(vm_script):
    tokens = tokenize(vm_script)
    bool_counter = count()
    return '\n'.join([analyze(token, bool_counter) for token in tokens])


def writer(path):
    rel_path = path[:path.rfind("\\")]
    output_name = path[path.rfind("\\")+1:]
    output_name = output_name[:output_name.rfind(".")]+".asm"
    translated = translate(read_file(path))
    translated = translated
    with open(rel_path+"\\"+output_name, "w") as f:
        f.write(translated)
    return rel_path+"\\"+output_name

if __name__ == "__main__":
    from sys import argv
    if len(argv) != 2:
        raise Exception("Unknown argv")
    print(writer(argv[1]))
    