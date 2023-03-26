import numpy as np
import matplotlib.pyplot as plt 
import matplotlib.animation as animation

# Define the size of the grid
N = 100

# Create the initial grid randomly
grid = np.random.choice([0, 1], size=(N, N), p=[0.5, 0.5])

# Define the rules for updating the grid
def update(frame_num, grid, img):
    new_grid = grid.copy()
    for i in range(N):
        for j in range(N):
            # Count the number of live neighbors
            neighbors = (grid[i-1, j-1] + grid[i-1, j] + grid[i-1, (j+1)%N] +
                         grid[i, j-1] + grid[i, (j+1)%N] +
                         grid[(i+1)%N, j-1] + grid[(i+1)%N, j] + grid[(i+1)%N, (j+1)%N])
            # Apply the rules to update the cell state
            if grid[i, j] == 1 and (neighbors < 2 or neighbors > 3):
                new_grid[i, j] = 0
            elif grid[i, j] == 0 and neighbors == 3:
                new_grid[i, j] = 1
    # Update the grid and the image
    grid[:] = new_grid[:]
    img.set_data(grid)
    return img,

# Create the animation
fig, ax = plt.subplots()
img = ax.imshow(grid, cmap='binary')
ani = animation.FuncAnimation(fig, update, fargs=(grid, img), frames=100, interval=50, blit=True)

plt.show()
