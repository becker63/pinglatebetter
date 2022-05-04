#!/usr/bin/env python2.5
from colorsys import hsv_to_rgb
from random import randint, uniform
from colormap import rgb2hex
from colormap import hex2rgb
import random


def comparison(x,y)-> int:
    if x > y:
        result = f"{x} > {y}"
    elif x < y:
        result = f"{x} < {y}"
    elif x == y:
        result = f"{x} = {y}"
    return result

def get_color_escape(r, g, b, background=False):
    return '\033[{};2;{};{};{}m'.format(48 if background else 38, r, g, b)


def colorgen(it):
    it = it + 3
    out = []
    from colour import Color
    red = Color("black")
    colors = list(red.range_to(Color("red"),it))

    i = 0
    hexcolors = []
    while(i != len(colors)):
        color = colors[i]

        RESET = '\033[0m'

        if "#" in str(color):
            hexcolors.append(str(color))
            #print(color)
        i = i + 1

    i = 0
    i2 = 0
    returned = []
    while(i != len(hexcolors)):   
        color = hexcolors[i].replace("#", "")
        a = int(str(hexcolors[i - 1]).replace("#", ""), 16)
        b = int(str(hexcolors[i]).replace("#", ""), 16)

        #print(f"{str(a)[0]}..{len(str(a))}  :  {str(b)[0]}..{len(str(b))}")

        #print(comparison(a, b))

        if a < b:
            returned.append("#" + color)

        i = i + 1

    return returned
    #print(i2)


