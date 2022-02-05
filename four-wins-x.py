def whoIsWinner(moves,con,sz):

    from string import ascii_uppercase, ascii_lowercase

    ROWS = sz
    COLS = sz
    CON = con-1
    COLUMNS = ascii_uppercase + ascii_lowercase
    
    grid = [list(" ") * COLS for _ in range(ROWS)]

    def add_to_grid(grid, move):
        letter, player = move.split("_")
        col = COLUMNS.index(letter)
        for row, grid_row in enumerate(grid):
            if grid_row[col] == " ":
                grid[row][col] = player
                break
        else:
            raise ValueError # full column
        return row,col,player

    def check_x_wins(grid, row, col):
        c_min, c_max = max(0, col - CON), min(COLS - 1, col + CON)
        r_min, r_max = max(0, row - CON), min(ROWS - 1, row + CON)

        line_hori = "".join([grid[row][c] for c in range(c_min, c_max + 1)])
        line_vert = "".join([grid[r][col] for r in range(r_min, r_max + 1)])
        
        # how many top-down-diagonal positions are within the grid (before and after current pos)
        top = min(row - r_min, col - c_min)
        low = min(r_max - row, c_max - col)
        line_topdown = "".join([grid[row - top + i][col - top + i] for i in range(top + low + 1)])

        # how many bottom-up-diagonal positions are within the grid (before and after current pos)
        low = min(r_max - row, col - c_min)
        top = min(c_max - col, row - r_min)
        line_bottomup = "".join([grid[row + low - i][col - low + i] for i in range(low + top + 1)])

        four = grid[row][col]*(CON+1)
        return line_hori.find(four)!=-1 or line_vert.find(four)!=-1 or line_bottomup.find(four)!=-1 or line_topdown.find(four)!=-1

    winner = "Draw"
    for move in moves:
        row, col, player  = add_to_grid(grid, move)
        if check_x_wins(grid,row,col):
            winner = player
            break

    return winner
