# Program for playing the game of Life
from gameoflife.lifegrid import LifeGrid

# Define the initial configuration of live cells.
init_config = [(1, 1), (1, 2), (2, 2), (3, 2)]

# Set the size of the grid
grid_width = int(input("Enter grid WIDTH not lower than 4: "))
grid_height = int(input("Enter HEIGHT not lower than 4: "))

# Indicate the number of generations
num_gens = int(input("Enter quantity of generations: "))


def main():
    '''
    Constructs the game grid and configure it
    '''
    grid = LifeGrid(grid_width, grid_height)
    grid.configure(init_config)

    # Plays the game.
    draw(grid)
    for i in range(num_gens):
        evolve(grid)
        draw(grid)


# Generates the next generation of organisms
def evolve(grid):
    '''
    List for storing the live cells of the next gen
    '''
    live_cells = []

    # Iterate over the elements of the grid
    for i in range(grid.num_rows()):
        for j in range(grid.num_cols()):

            # Determine the number of live neighbors for this cell
            neighbors = grid.num_live_neighbors(i, j)

            # Add the (i,j) tuple to liveCells if this cell contains
            if (neighbors == 2 and grid.is_live_cell(i, j)) or (neighbors == 3):
                live_cells.append((i, j))

    # Reconfigure the grid using the liveCells coord list
    grid.configure(live_cells)


# Prints a text based representation of the game grid
def draw(grid):
    print(grid)

