from functools import partial
import numpy as np

from numpy._typing import NDArray
from vispy.scene.visuals import SurfacePlot
from wrapper import Shape

PRINGLE_COLOUR = "#EECA7F"

IMAGE_SHAPE = (600, 800)  # (height, width)
CANVAS_SIZE = (800, 600)  # (width, height)
NUM_LINE_POINTS = 1000
A = -15
B = 15
T = np.linspace(A, B, NUM_LINE_POINTS)


def create_hyperbolic_paraboloid(a, b):
    x_grid, y_grid = np.meshgrid(T, T)

    z_grid = ((x_grid**2) / a) - ((y_grid**2) / b)

    return x_grid, y_grid, z_grid


def define_ellipse_domain(
    x_grid: NDArray[np.floating], y_grid: NDArray[np.floating], a, b
):
    """
    Create the cookie cutout. assumes a >= b
    """

    domain = partial(np.where, ((x_grid**2) / a) + ((y_grid**2) / b) > 5, np.nan)
    return domain(x_grid), domain(y_grid)


# Add a 3D axis

x_grid, y_grid, z_grid = create_hyperbolic_paraboloid(22, 13)
x_grid, y_grid = define_ellipse_domain(x_grid, y_grid, 7, 5)

plot = SurfacePlot(x_grid, y_grid, z_grid, color=PRINGLE_COLOUR)


if __name__ == "__main__":
    pringle_can = Shape(plot)
    pringle_can.show(visible=True, run=True)
