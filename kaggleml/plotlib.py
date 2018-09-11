"""
KaggleML to display loss in learning phase
"""

__authors__ = ['Orlando, Ding']

from IPython import display
from matplotlib import pyplot as plt

def semilogy(x_vals, y_vals, x_label, y_label, x2_vals=None, y2_vals=None,
             legend=None, figsize=(3.5, 2.5)):
    """
    Plot x and log(y).
    Access link - https://github.com/mli/gluon-tutorials-zh/tree/master/gluonbook/utils.py
    """
    set_figsize(figsize)
    plt.xlabel(x_label)
    plt.ylabel(y_label)
    plt.semilogy(x_vals, y_vals)
    if x2_vals and y2_vals:
        plt.semilogy(x2_vals, y2_vals, linestyle=':')
        plt.legend(legend)
    plt.show()

def set_figsize(figsize=(3.5, 2.5)):
    """
    Set matplotlib figure size.
    Access link - https://github.com/mli/gluon-tutorials-zh/tree/master/gluonbook/utils.py
    """
    use_svg_display()
    plt.rcParams['figure.figsize'] = figsize

def use_svg_display():
    """
    Use svg format to display plot in jupyter.
    Access link - https://github.com/mli/gluon-tutorials-zh/tree/master/gluonbook/utils.py
    """
    display.set_matplotlib_formats('svg')
