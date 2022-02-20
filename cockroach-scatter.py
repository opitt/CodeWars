def cockroaches(room):

    BUG_SCATTER = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

    HOLES = {
        "U": {x: int(h) for x, h in enumerate(room[0]) if h not in "+-"},
        "L": {x: int(h) for x, h in enumerate(list(zip(*room))[0]) if h not in "+|"},
        "D": {x: int(h) for x, h in enumerate(room[-1]) if h not in "+-"},
        "R": {x: int(h) for x, h in enumerate(list(zip(*room))[-1]) if h not in "+|"},
    }
    # collect the bugs based on the direction they look
    bugs_yx = {"U": [], "L": [], "D": [], "R": []}
    for y, row in enumerate(room):
        for x, c in enumerate(row):
            if c in "UDLR":
                bugs_yx[c].append(y if c in "LR" else x)

    # if a bug looks in direction "U" and if there is not hole at that wall, we need to go left to other walls
    BUG_DIR_WALLSEQUENCE = {"U":"LDRU",
                      "L": "DRUL",
                      "D": "RULD",
                      "R": "ULDR",
    }

    def first_left(wall, bug_pos=None):
        if wall in "UR":
            _, hole = max(
                [
                    (pos, hole)
                    for pos, hole in HOLES[wall].items()
                    if bug_pos == None or pos <= bug_pos
                ],
                key=lambda ph: ph[0],
                default=(None, None),
            )
        else:
            _, hole = min(
                [
                    (pos, hole)
                    for pos, hole in HOLES[wall].items()
                    if bug_pos == None or pos >= bug_pos
                ],
                key=lambda ph: ph[0],
                default=(None, None),
            )
        return hole

    for bug_dir in "ULDR":
        for pos in bugs_yx[bug_dir]:
            # check, if there is a hole left of my position towards the wall
            hole = first_left(bug_dir, pos)
            if hole != None:
                BUG_SCATTER[hole] += 1
                continue
            # find the first hole going LEFT wall
            for wall in BUG_DIR_WALLSEQUENCE[bug_dir]:
                hole = first_left(wall)
                if hole != None:
                    BUG_SCATTER[hole] += 1
                    break
            if hole != None:
                # next bug
                continue

    return BUG_SCATTER


expected = [1, 2, 2, 5, 0, 0, 0, 0, 0, 0]
room = [
    "+----------------0---------------+",
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
    "+----------------2---------------+",
]

print(cockroaches(room), expected)
