EAST  = 0
NORTH = 1
WEST  = 2
SOUTH = 3

def PrintGrid(grid):
    for i in range(len(grid)):
        print(grid[i])
    print()

def Middle(SIZE, Clockwise):
    if SIZE % 2 == 1:
        row = col = SIZE // 2
    else:
        row = SIZE // 2
        col = SIZE // 2 - 1
        if Clockwise:
            row, col = col, row
    return (row, col)

def East(pos):
    row, col = pos
    return (row, col + 1)

def North(pos):
    row, col = pos
    return (row - 1, col)

def West(pos):
    row, col = pos
    return (row, col - 1)

def South(pos):
    row, col = pos
    return (row + 1, col)

Directions = {
    EAST: East,
    NORTH: North,
    WEST: West,
    SOUTH: South,
}

def GoInDirection(pos, dir):
    return Directions[dir](pos)

def ChangeDirection(dir, Clockwise):
    if Clockwise:
        dir = (dir - 1) % len(Directions)
    else:
        dir = (dir + 1) % len(Directions)
    return dir

def Spiral(SIZE, start = 1, Clockwise = False):
    grid = [[0 for x in range(SIZE)] for y in range(SIZE)]
    count = [(n + 1) // 2 for n in range(1, SIZE * 2)]
    direction = SOUTH if Clockwise else EAST
    row, col = Middle(SIZE, Clockwise)
    for x in count:
        for y in range(x):
            grid[row][col] = start
            row, col = GoInDirection((row, col), direction)
            start += 1
        direction = ChangeDirection(direction, Clockwise)
    PrintGrid(grid)

Spiral(9, 41)
