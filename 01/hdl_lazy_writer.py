prog = ""
bits = 16
for i in range(bits):
    prog += f"Not(in=in[{i}], out=out[{i}]);\n"

def write_arr_boolean(op_txt, n = 16):
    prog = ""
    for i in range(n):
        prog += f"{op_txt}(a=a[{i}], b=b[{i}], out=out[{i}]);\n"
    return prog