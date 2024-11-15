import click
import numpy as np
import pandas as pd
from numpy import pi


@click.group()
def cmd_group():
    pass


@cmd_group.command()
@click.option(
    "-n",
    "--steps",
    default=10,
    help="Number of steps between 0 and 2pi",
    show_default=True,  # show default in help
)
def sin(steps):
    """Gives a 2 lists of x and sinx in given steps between 0 and 2pi"""
    x = np.linspace(0, 2 * pi, steps)
    df = pd.DataFrame({"x": x, "sin (x)": np.sin(x)})
    print(df)


@cmd_group.command()
@click.option(
    "-n",
    "--steps",
    default=10,
    help="Number of steps between 0 and 2pi",
    show_default=True,  # show default in help
)
def tan(steps):
    """Gives a 2 lists of x and tanx in given steps between 0 and 2pi"""
    x = np.linspace(0, 2 * pi, steps)
    df = pd.DataFrame({"x": x, "tan (x)": np.tan(x)})
    print(df)


if __name__ == "__main__":
    cmd_group()
