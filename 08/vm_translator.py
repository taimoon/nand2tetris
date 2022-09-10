from itertools import count
'''
Implementation order.
push const val, arithmetic, logical operation
push/pop local, argument, this, that
push/pop pointer, temp
push/pop static
label, goto, ifgoto
call, function, return

conventions:
SP always points the null end of the stack
0 is treated false value, otherwise true

Tips:
    where SP points to, can be recycled as temp variable.
Previous statement is not always true.
This causes a nasty bug during returning,
because it doesn't consider 0 argument case.
It will overwrite the return address.
If it is 0 args, then the ARG points to the return address.
Therefore, R13,R14 and R15 are general purpose registers can be used to stored temp values.
'''
'''
Implement 3 commands that helps function
VM cmd:
1. call
2. function
3. return
'''
class naive_tally_counter:
    def __init__(self):
        self.book = {}
    def tally(self, obj):
        if obj not in self.book:
            self.book[obj] = count(0)
        return next(self.book[obj])

def ignore_first_tab_eachline(prog):
    prog = prog.split("\n")
    prog = [ln.lstrip() for ln in prog]
    return "\n".join(prog)

def read_file(path):
    res = ""
    with open(path, "r") as f:
        res = f.read()
    return res

def tokenize(vm_script):
    def rm_cmd(line):
        if line.find('//') != -1:
            return line[0:line.find('//')]
        return line
    lines = [rm_cmd(line) for line in vm_script.split('\n')]
    lines = [i.strip() for i in lines if i != '']
    lines = [line.split() for line in lines]
    return lines
    
def translate(vm_script, env, fn_call_counter):
    if len(env) == 1:
        file_scope = env[0]
    else:
        file_scope = env[1]
    tokens = tokenize(vm_script)
    bool_counter = count()
    asm_prog = [analyze(token, bool_counter, env, fn_call_counter, file_scope) for token in tokens]
    return '\n\n'.join(asm_prog)

def analyze(token, bool_counter:count, env, fn_call_counter, file_scope):
    corpsd = {
        "push": lambda tkn: push_prog(tkn[1],tkn[2], file_scope),
        "pop": lambda tkn: pop_prog(tkn[1],tkn[2], file_scope),
        "label": lambda tkn: label_prog(tkn[1], env),
        "goto": lambda tkn: goto_prog(tkn[1], env),
        "if-goto": lambda tkn: ifgoto_prog(tkn[1], env),
        "function": lambda tkn: function_prog(tkn[1], int(tkn[2]), env),
        "call" : lambda tkn: call_prog(tkn[1],int(tkn[2]), fn_call_counter, env),
        "return": lambda tkn: return_prog(env)
    }
    fn = corpsd.get(token[0], # corspd[token[0]]
                    lambda tkn:arithmetic_prog(tkn[0], bool_counter))
    return fn(token)

def bootstrap_code(fn_call_counter):
    return f"""
        @256
        D=A
        @SP
        M=D
        {translate("call Sys.init 0", ["__BOOTSTRAP"], fn_call_counter)}
    """.replace("\t","").strip()

def arithmetic_prog(op, bool_counter:count):
    prog = ""
    bi_op_corspd = {"add": "+", "sub": "-","and": "&","or" : "|", "gt":"-", "lt":"-", "eq":"-" }
    uni_op_corspd = {"neg":"-","not":"!"}
    if op in uni_op_corspd:
        prog = f"""
            // arithmetic {op}
            @SP
            A=M-1	// A = SP-1
            M={uni_op_corspd[op]}M
        """
    elif op in bi_op_corspd:
        prog = f"""
            // arithmetic {op}
            @SP
            AM=M-1	// SP = SP--
            D=M		// D = *SP (second arg)
            A=A-1	// A = SP-1 (first arg)
            MD=M{bi_op_corspd[op]}D	// *SP + *(SP-1)
        """ # note that the last line MD is necessary for boolean opearation if op is logical.
        if op in ["eq","lt", "gt"]:
            bool_n = next(bool_counter)
            jmp_inst = "J"+op.upper()
            prog += f"""@__BOOL{bool_n}
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
        print(op)
        raise()
    return prog.replace("\t","").strip()

seg_corspd = {"local":"LCL", "argument":"ARG", "this":"THIS", "that":"THAT"}
def push_prog(seg,val, curr_file_name=""):
    val = int(val)
    if seg == "static":
        return push_static_prog(val,curr_file_name)
    corspd = {"constant": push_const_prog, "temp": push_temp_prog, "pointer":push_ptr_prog, "static":push_static_prog}
    fn = corspd.get(seg, lambda val: push_seg_prog(seg,val))
    return fn(val)
    
def push_const_prog(val):
    "IDEA: *SP = val, SP++"
    return f"""
    // push const {val}
    @{val}
    D=A
    @SP
    A=M
    M=D
    @SP
    M=M+1
    """.replace("\t","").strip()

def push_temp_prog(val):
    "addr = 5+i, *SP = *addr, SP++"
    return f"""
        // push temp {val}
        @{val+5}	// A = addr = 5 + {val}	
        D=M		// D = *addr
        @SP 	// A = &SP
        A=M 	// A = SP
        M=D 	// *SP = D
        @SP 	// A = &SP
        M=M+1	// SP++ 
    """.replace("\t","").strip()

def push_seg_prog(seg,pos):
    "addr=seg+pos, *SP=*addr, SP++"
    seg = seg_corspd[seg]
    prog = f'''
        // push {seg} {pos}
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
    // push pointer {n}
    @{ptr_insts_tbl[n]}
    D=M	// D=THIS/THAT
    @SP
    A=M // A=SP
    M=D	// *SP = THIS/THAT
    @SP
    M=M+1	// SP++
    """.replace("\t","").strip()

def push_static_prog(pos, curr_file_name=""):
    return f"""
    // push static {pos}
    @{curr_file_name}.{pos}
    D=M
    @SP 
    A=M // A=SP
    M=D	// *SP = D
    @SP
    M=M+1	// SP++
    """.replace("\t","").strip()

def pop_prog(seg, pos, curr_file_name=""):
    pos = int(pos)
    if seg == "static":
        return pop_static_prog(pos,curr_file_name)
    corspd = {"temp": pop_temp_prog, "pointer":pop_ptr_prog, "static":pop_static_prog}
    fn = corspd.get(seg,lambda val:pop_seg_prog(seg,val))
    return fn(pos)

def pop_temp_prog(val):
    "addr=5+val, SP--, *addr=*SP"
    return f"""
    // pop temp {val}
    // addr = 5 + {val}
    @{val+5}
    D=A	// A = addr = 5 + val
    // store addr as temp var
    @SP
    A=M
    M=D
    @SP
    AM=M-1	// A=SP--
    D=M		// D=*SP
    A=A+1
    A=M		// A = *(SP+1) = addr
    M=D		// *addr = *SP
    """.replace("\t","").strip()

def pop_seg_prog(seg,pos):
    "addr=seg+pos, SP--, *addr=*SP"
    seg=seg_corspd[seg]
    return f'''
    // pop {seg} {pos}
    @{seg}
    D=M		// D={seg}
    @{pos}
    D=D+A	// D={seg}+{pos}=addr
    @SP		// *SP = addr+pos
    A=M
    M=D
    @SP
    AM=M-1	// A = SP--
    D=M		// D = *SP
    A=A+1	// A = SP+1
    A=M		// A = *(SP+1) = addr
    M=D		// *addr = *SP
    '''.replace("\t","").strip()

def pop_ptr_prog(n):
    "SP--, THIS/THAT = *SP"
    return f"""
    // pop pointer {n}
    @SP
    AM=M-1 	// SP--
    D=M		// D=*SP
    @{ptr_insts_tbl[n]}
    M=D		// THIS/THAT = *SP
    """.replace("\t","").strip()

def pop_static_prog(pos, curr_file_name):
    return f"""
    // pop static {pos}
    @SP
    AM=M-1	// SP--
    D=M		// D=*SP
    @{curr_file_name}.{pos}
    M=D		// RAM[pos+16] = D = *SP
    """.replace("\t","").strip()

# stage 2: branching and function
def label_prog(lbl, env):
    return f"""
    // label {lbl}
    ({"$".join(env)}${lbl})
    """.replace("\t","").strip()

def goto_prog(lbl, env):
    return f"""
    // goto {lbl}
    @{"$".join(env)}${lbl}
    0;JMP
    """.replace("\t","").strip()

def ifgoto_prog(lbl, env):
    "cond=pop; cond jump if pop"
    return f"""
    // if-goto {lbl}
    @SP
    M=M-1	// SP--
    A=M		// A=SP
    D=M		// D=*SP
    @{"$".join(env)}${lbl}
    D;JNE 	// jump if not false (ie.: not equal to 0)
    """.replace("\t","").strip()

def call_prog(name, nArgs, fn_call_counter:naive_tally_counter, env):
    push_helper = lambda ptr: f"""
        @{ptr}
        D=M
        @SP
        A=M
        M=D
        @SP
        M=M+1
    """
    fn_ret_lbl = "$".join(env) + f"${name}"
    ret_addr_str = f"{fn_ret_lbl}$ret.{fn_call_counter.tally(fn_ret_lbl)}"
    prog = f"""
    // call {name} {nArgs}
    // save the caller's frame
    @{ret_addr_str}
    D=A
    @SP
    A=M
    M=D
    @SP
    M=M+1
    {push_helper("LCL")}
    {push_helper("ARG")}
    {push_helper("THIS")}
    {push_helper("THAT")}
    @{nArgs+5} // ARG = SP - ({nArgs} + 5) ; reposition ARG
    D=A
    @SP
    D=M-D
    @ARG
    M=D		
    @SP		//  LCL = SP ; reposition LCL
    D=M
    @LCL
    M=D
    @{name}
    0;JMP
    ({ret_addr_str}) // translated-generated label
    // end of call {name} {nArgs}
    """
    return prog.replace("\t","").strip()

def function_prog(func_name, vars_n, env):
    env.pop()
    env.append(func_name)
    init_n_push = lambda : f"""
    @SP
    A=M
    M=0
    @SP
    M=M+1
    """
    init_str = '\n'.join([init_n_push() for _ in range(vars_n)])
    return f"""
    // function {func_name} {vars_n}
    ({func_name})
    {init_str}
    // end of initializing local variables
    """.replace("\t","").strip()

def return_prog(env):
    pop_n_restore = lambda seg: f"""
        @LCL
        AM=M-1
        D=M
        @{seg}
        M=D
    """
    segs = "THAT THIS ARG LCL".split()
    restore_prog = '\n'.join(pop_n_restore(seg) for seg in segs)
    return f"""
    // return
    // return the value to the caller
    // store retaddr as temp var at R13
    @5
    D=A
    @LCL
    A=M-D
    D=M
    @R13		// R13 = return address
    M=D
    @SP		// *ARG = pop()
    AM=M-1
    D=M		// return value
    @ARG
    A=M
    M=D
    // reposition SP of the caller
    @ARG	// SP = ARG + 1 
    D=M+1
    @SP
    M=D
    {restore_prog}
    @R13
    A=M
    0;JMP
    // end of returning
    """.replace("\t","").strip()

def writer(path):
    from os.path import isdir
    from os import listdir
    translated = ""
    rel_path = ""
    output_name = ""
    name_of_file = lambda f : f[:f.rfind('.')]
    ext_of_file = lambda f : f[f.rfind('.')+1:]
    fn_call_counter = naive_tally_counter()
    if isdir(path):
        rel_path = path
        output_name = path[path.rfind("\\")+1:]
        input_files = listdir(path)
        input_files = [f for f in input_files if ext_of_file(f) == "vm"]
        env = [output_name]
        for f in input_files:
            vm_script = read_file(rel_path+"\\"+f)
            translated += "\n"+translate(vm_script, env+[name_of_file(f)], fn_call_counter)
        translated = bootstrap_code(fn_call_counter)+translated
    else:
        rel_path = path[:path.rfind("\\")]
        input_name = path[path.rfind("\\")+1:]
        input_name = name_of_file(input_name)
        output_name = input_name
        translated = translate(read_file(path), [input_name], fn_call_counter)
        # translated = bootstrap_code(fn_call_counter)+translated
    output_name = output_name+".asm"
    with open(rel_path+"\\"+output_name, "w") as f:
        f.write(translated)
    return rel_path+"\\"+output_name

if __name__ == "__main__":
    from sys import argv
    if len(argv) != 2:
        raise Exception("Unknown argv")
    print(writer(argv[1]))