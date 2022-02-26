from rich import print


def podium_code():
    cmds = """
:345**/.87vv98,:<>
v/*52:,+2*<>**-  |
>6%.:52*%.1+:25*^@
""".splitlines()
    cmds = cmds[1:]
    #            RIGHT         LEFT          UP             DOWN
    REFLECT_V = {
        (0, 1): (0, -1),
        (0, -1): (0, 1),
        (-1, 0): (-1, 0),
        (1, 0): (1, 0),
    }  # |
    REFLECT_D = {
        (0, 1): (-1, 0),
        (0, -1): (1, 0),
        (-1, 0): (0, 1),
        (1, 0): (0, -1),
    }  # /
    dir = (-1, 0)
    ipx, ipy = len(cmds[0])-1, len(cmds)-1
    stack = []
    c = cmds[ipy][ipx]
    while c != " ":
        print(f"{c=}")

        if c == ".":
            try:
                print(stack[-1])
            except:
                print("?")
        elif c in "0123456789":
            stack.append(int(c))
        elif c == " ":
            pass
        elif c == "^":
            dir = (-1, 0)
        elif c == "v":
            dir = (1, 0)
        elif c == ">":
            dir = (0, 1)
        elif c == "<":
            dir = (0, -1)
        elif c == "/":
            dir = REFLECT_D[dir]
        elif c == "|":
            if dir == (0,1):
                break
            dir = REFLECT_V[dir]
        elif c == "*":
            res = stack[-2] * stack[-1]
            stack = stack[:-2] + [res]
        elif c == "+":
            res = stack[-2] + stack[-1]
            stack = stack[:-2] + [res]
        elif c == "-":
            res = stack[-2] - stack[-1]
            stack = stack[:-2] + [res]
        elif c == ",":  # division
            res = stack[-2] / stack[-1]
            stack = stack[:-2] + [res]
        elif c == "%":
            res = stack[-2] % stack[-1]
            stack = stack[:-2] + [res]
        elif c == ":":
            #stack = []
            print(stack[-1])
        else:
            pass


        ipy += dir[0]
        ipx += dir[1]

        ipy = len(cmds) - 1 if ipy < 0 else ipy
        ipy = 0 if ipy > (len(cmds) - 1) else ipy
        ipx = 0 if ipx > (len(cmds[0]) - 1) else ipx
        ipx = len(cmds[0]) - 1 if ipx < 0 else ipx

        c = cmds[ipy][ipx]


podium_code()
