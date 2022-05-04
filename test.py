from colormap import hex2rgb
import sys
from color import gen
import random


greens = gen(10)


def get_color_escape(r, g, b, background=False):
    return '\033[{};2;{};{};{}m'.format(48 if background else 38, r, g, b)

RESET = '\033[0m'


