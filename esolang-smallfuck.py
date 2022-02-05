def interpreter(code, tape):
    cmds = list(code)
    (*data,) = map(int, tape)
    pos_cmd = pos_data = 0
    POS_LAST_CMD = len(cmds) - 1
    POS_LAST_DATA = len(tape) - 1

    while 0 <= pos_cmd <= POS_LAST_CMD and 0 <= pos_data <= POS_LAST_DATA:
        c = cmds[pos_cmd]
        pos_cmd += 1
        if c == ">":   pos_data += 1
        elif c == "<": pos_data -= 1
        elif c == "*": data[pos_data] = int(not data[pos_data])
        elif c == "[":
            # possibly nested
            if data[pos_data] == 0:
                # find matching ] ... to the right of the current cmd position; POS_LAST_CMD is the highest index
                found = 1 #count the number of brackets. start with 1, the current. When 0 is reached, we found the last closing.
                p = pos_cmd
                while found and p<=POS_LAST_CMD:
                    if cmds[p]=="[": found+=1
                    if cmds[p]=="]": found-=1
                    p += 1
                pos_cmd = p # right after the ]
        elif c == "]":
            if data[pos_data] != 0:
                # find matching [ ... to the left of current cmd position; 0 is the smallest index
                found = 1
                p = pos_cmd-2 # search left of current [
                while found and p>=0:
                    if cmds[p]=="[": found-=1
                    if cmds[p]=="]": found+=1
                    p -= 1
                pos_cmd = p + 1
        else:
            # ignore other characters
            pass
    return "".join(list(map(str, data)))
    

for code, tape in [
    ("[[]*>*>*>]", "000"),
    ("*>>>*>*>>*>>>>>>>*>*>*>*>>>**>>**", "0000000000000000"),
    ("*", "00101100"),
    (">*>*", "00101100"),
    ("*>*>*>*>*>*>*>*", "00101100"),
    ("*>*>>*>>>*>*", "00101100"),
    (">>>>>*<*<<*", "00101100"),
]:
    print(code, interpreter(code, tape))
