path = [
    r"add\Add.asm",
    # r".\max\Max.asm",
    # r".\rect\Rect.asm",
    # r".\pong\Pong.asm"
]
import os 
import sys
assembler_path = r"hack_assembler.py"
assembler_full_path = os.path.join(sys.path[0], assembler_path)
for p in path:
    p = os.path.join(sys.path[0], p)
    print(p)
    exec(open(assembler_full_path).read(),{'argv':[p]})