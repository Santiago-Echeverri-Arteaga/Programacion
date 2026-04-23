import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation


def step_numpy(grid):
    """
    grid: np.ndarray de 0/1
    Calcula vecinos con sumas de 'roll' (toroide: wrap-around).
    """
    neighbors = (
        np.roll(np.roll(grid,  1, 0),  1, 1) + np.roll(grid,  1, 0) + np.roll(np.roll(grid,  1, 0), -1, 1) +
        np.roll(grid,  1, 1) + np.roll(grid, -1, 1) +
        np.roll(np.roll(grid, -1, 0),  1, 1) + np.roll(grid, -1, 0) +
        np.roll(np.roll(grid, -1, 0), -1, 1)
    )

    # Reglas:
    # nace si vecinos==3
    # sobrevive si (viva & vecinos==2) o vecinos==3
    return ((neighbors == 3) | ((grid == 1) & (neighbors == 2))).astype(np.uint8)


def life(grid, steps=None):
    """
    Generador de generaciones. Si steps=None, infinito.
    """
    t = 0
    while steps is None or t < steps:
        yield grid
        grid = step_numpy(grid)
        t += 1


def seed_glider(grid, top, left):
    pattern = np.array([
        [0, 1, 0],
        [0, 0, 1],
        [1, 1, 1]
    ], dtype=np.uint8)
    h, w = pattern.shape
    grid[top:top+h, left:left+w] = pattern


# ----- Demo -----
H, W = 80, 120
grid0 = (np.random.rand(H, W) < 0.30).astype(np.uint8)

# Un par de patrones bonitos
seed_glider(grid0, 5, 5)
seed_glider(grid0, 30, 40)

gen = life(grid0)  # generador infinito

fig, ax = plt.subplots()
im = ax.imshow(next(gen), interpolation="nearest")
ax.set_title("Juego de la Vida — NumPy + Matplotlib")
ax.set_axis_off()


def update(_):
    im.set_data(next(gen))
    return (im,)


ani = FuncAnimation(fig, update, interval=50, blit=True)

# Tip: cerrar con la X o con 'q' en la ventana según backend
plt.show()
