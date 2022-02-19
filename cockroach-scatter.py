def cockroaches(room):
    # Your code here!
    BUG_SCATTER = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    
    holes_u = {x:int(h) for x,h in enumerate(room[0]) if h not in "+-"}
    holes_d = {x:int(h) for x,h in enumerate(room[-1]) if h not in "+-"}
    holes_l = {x:int(h) for x,h in enumerate(list(zip(*room))[0]) if h not in "+|"}
    holes_r = {x:int(h) for x,h in enumerate(list(zip(*room))[-1]) if h not in "+|"}
    cockroach_yx={"U":[], "D": [], "L":[], "R":[]}
    for y,row in enumerate(room):
        for x, c in enumerate(row):
            if c in "UDLR":
                cockroach_yx[c].append((y,x))
    
    for bug_y,bug_x in cockroach_yx["U"]:
        hole_x = max([x for x in holes_u.keys() if x <= bug_x], default=None )
        if hole_x != None:
            hole = holes_u[hole_x]
            BUG_SCATTER[hole] += 1
            continue
        hole_y = min(holes_l.keys(), default=None)
        if hole_y != None:
            hole = holes_l[hole_y]
            BUG_SCATTER[hole] += 1
            continue
        hole_x = min(holes_d.keys(), default=None)
        if hole_x != None:
            hole = holes_d[hole_x]
            BUG_SCATTER[hole] += 1
            continue
        hole_y = max(holes_r.keys(), default=None)
        if hole_y != None:
            hole = holes_r[hole_y]
            BUG_SCATTER[hole] += 1
            continue
        hole_x = max(holes_u.keys(), default=None)
        if hole_x != None:
            hole = holes_u[hole_x]
            BUG_SCATTER[hole] += 1
            continue

    for bug_y,bug_x in cockroach_yx["L"]:
        hole_y = min([y for y in holes_l.keys() if y >= bug_y], default=None )
        if hole_y != None:
            hole = holes_l[hole_y]
            BUG_SCATTER[hole] += 1
            continue
        hole_x = min(holes_d.keys(), default=None)
        if hole_x != None:
            hole = holes_d[hole_x]
            BUG_SCATTER[hole] += 1
            continue
        hole_y = max(holes_r.keys(), default=None)
        if hole_y != None:
            hole = holes_r[hole_y]
            BUG_SCATTER[hole] += 1
            continue
        hole_x = max(holes_u.keys(), default=None)
        if hole_x != None:
            hole = holes_u[hole_x]
            BUG_SCATTER[hole] += 1
            continue
        hole_y = min(holes_l.keys(), default=None)
        if hole_y != None:
            hole = holes_l[hole_y]
            BUG_SCATTER[hole] += 1
            continue

    for bug_y,bug_x in cockroach_yx["D"]:
        hole_x = min([x for x in holes_d.keys() if x >= bug_x], default=None )
        if hole_x != None:
            hole = holes_d[hole_x]
            BUG_SCATTER[hole] += 1
            continue
        hole_y = max(holes_r.keys(), default=None)
        if hole_y != None:
            hole = holes_r[hole_y]
            BUG_SCATTER[hole] += 1
            continue
        hole_x = max(holes_u.keys(), default=None)
        if hole_x != None:
            hole = holes_u[hole_x]
            BUG_SCATTER[hole] += 1
            continue
        hole_y = min(holes_l.keys(), default=None)
        if hole_y != None:
            hole = holes_l[hole_y]
            BUG_SCATTER[hole] += 1
            continue
        hole_x = min(holes_d.keys(), default=None)
        if hole_x != None:
            hole = holes_d[hole_x]
            BUG_SCATTER[hole] += 1
            continue

    for bug_y,bug_x in cockroach_yx["R"]:
        hole_y = max([y for y in holes_r.keys() if y <= bug_y], default=None )
        if hole_y != None:
            hole = holes_r[hole_y]
            BUG_SCATTER[hole] += 1
            continue
        hole_x = max(holes_u.keys(), default=None)
        if hole_x != None:
            hole = holes_u[hole_x]
            BUG_SCATTER[hole] += 1
            continue
        hole_y = min(holes_l.keys(), default=None)
        if hole_y != None:
            hole = holes_l[hole_y]
            BUG_SCATTER[hole] += 1
            continue
        hole_x = min(holes_d.keys(), default=None)
        if hole_x != None:
            hole = holes_d[hole_x]
            BUG_SCATTER[hole] += 1
            continue
        hole_y = max(holes_r.keys(), default=None)
        if hole_y != None:
            hole = holes_r[hole_y]
            BUG_SCATTER[hole] += 1
            continue

    return BUG_SCATTER

expected = [1,2,2,5,0,0,0,0,0,0]
room=["+----------------0---------------+",
      "|                                |",
      "|                                |",
      "|          U        D            |",
      "|     L                          |",
      "|              R                 |",
      "|           L                    |",
      "|  U                             1",
      "3        U    D                  |",
      "|         L              R       |",
      "|                                |",
      "+----------------2---------------+"]

print(cockroaches(room), expected)
