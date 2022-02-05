from string import ascii_uppercase

ROWS = 6
COLS = 7
grid = [list(" ") * COLS for _ in range(ROWS)]


def add_to_grid(grid, move):
    letter, player = move.split("_")
    col = ascii_uppercase.index(letter)
    for row, line in enumerate(grid[:]):
        if line[col] == " ":
            grid[row][col] = player
            break
    else:
        raise ValueError  # full column
    return row, col, player


def check_4_wins(grid, row, col):
    c_min, c_max = max(0, col - 3), min(COLS - 1, col + 3)
    r_min, r_max = max(0, row - 3), min(ROWS - 1, row + 3)

    line_hori = "".join([grid[row][c] for c in range(c_min, c_max + 1)])
    line_vert = "".join([grid[r][col] for r in range(r_min, r_max + 1)])

    # how many top-down-diagonal positions are within the grid (before and after current pos)
    top = min(row - r_min, col - c_min)
    low = min(r_max - row, c_max - col)
    line_topdown = "".join(
        [grid[row - top + i][col - top + i] for i in range(top + low + 1)]
    )

    # how many bottom-up-diagonal positions are within the grid (before and after current pos)
    low = min(r_max - row, col - c_min)
    top = min(c_max - col, row - r_min)
    line_bottomup = "".join(
        [grid[row + low - i][col - low + i] for i in range(low + top + 1)]
    )

    four = grid[row][col] * 4
    return (
        line_hori.find(four) != -1
        or line_vert.find(four) != -1
        or line_bottomup.find(four) != -1
        or line_topdown.find(four) != -1
    )


pieces_position_list = [
    "A_Red",
    "B_Yellow",
    "A_Red",
    "B_Yellow",
    "A_Red",
    "B_Yellow",
    "F_Red",
    "C_Yellow",
]

# check_4_wins(grid, 0, 0)
# check_4_wins(grid, 1, 1)
# check_4_wins(grid, ROWS//2, COLS//2)
# check_4_wins(grid, ROWS - 1, COLS - 1)

# You should return "Yellow", "Red" or "Draw" accordingly.

winner = "Draw"
for move in pieces_position_list:
    row, col, player = add_to_grid(grid, move)
    if check_4_wins(grid, row, col):
        winner = player
        break

print(winner)
