#!/usr/bin/env python3

from fasta2png import _generate_png
import argparse
import sys
import math


def _main(in_file,
        out_file,
        pixel_size, 
        aspect_width, 
        aspect_height, 
        bg_color, 
        colortable):
    seq = ''
    with open(in_file, 'r') as f:
        first_seq_found = False
        while True:
            line = f.readline()
            # end of file ?
            if len(line) == 0:
                break
            # description ?
            elif line[0] == '>':
                # this program uses only the first sequence in the file
                if first_seq_found:
                    break
                print('seqdesc: %s' % line[1:].strip())
                first_seq_found = True
                continue
            # comment ?
            elif line[0] == ';':
                continue
            seq = seq + line.strip()
    seq = seq.lower()
    print('seqlen: %d' % len(seq))
    _generate_png(seq,
            out_file,
            pixel_size,
            aspect_width,
            aspect_height,
            bg_color,
            colortable)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--input', required=True, 
            help='input (fasta/fna) file name')
    parser.add_argument('--output', required=True, 
            help='output (rgba png) file name')
    parser.add_argument('--b-is', choices=['d', 'n'], default=False,
            help='use color of d or n as b, default is to use a different color')
    parser.add_argument('--j-is', choices=['l', 'i'], default=False,
            help='use color of l or i as j, default is to use a different color')
    parser.add_argument('--z-is', choices=['e', 'q'], default=False,
            help='use color of e or q as z, default is to use a different color')
    parser.add_argument('--pixel-size', type=int, default=1, 
        help='size of a (nucleotid) base in final png in pixels, default is 1')
    parser.add_argument('--aspect-ratio', type=int, nargs=2, default=[1, 1],
            help='aspect ratio, provide as two integers representing width and height, default is 1 1')
    parser.add_argument('--bg-color', 
            type=int, 
            nargs=4, 
            default=[0, 0, 0, 255],
            help='background color rgba, 4 integers, default is opaque black')
    args = parser.parse_args()

    # visually distinct palette
    # https://mokole.com/palette.html
    colortable = {}
    colortable['a'] = (0x69, 0x69, 0x69)
    colortable['b'] = (0x8b, 0x45, 0x13)
    colortable['c'] = (0x80, 0x80, 0x00)
    colortable['d'] = (0x48, 0x3d, 0x8b)
    colortable['e'] = (0x00, 0x80, 0x00)
    colortable['f'] = (0x00, 0x8b, 0x8b)
    colortable['g'] = (0x00, 0x00, 0x80)
    colortable['h'] = (0x7f, 0x00, 0x7f)
    colortable['i'] = (0xb0, 0x30, 0x60)
    colortable['j'] = (0xff, 0x45, 0x00)
    colortable['k'] = (0xff, 0x8c, 0x00)
    colortable['l'] = (0x00, 0x00, 0xcd)
    colortable['m'] = (0x00, 0xff, 0x00)
    colortable['n'] = (0xdc, 0x14, 0x3c)
    colortable['o'] = (0x00, 0xff, 0xff)
    colortable['p'] = (0x00, 0xbf, 0xff)
    colortable['q'] = (0xad, 0xff, 0x2f)
    colortable['r'] = (0xff, 0x00, 0xff)
    colortable['s'] = (0x1e, 0x90, 0xff)
    colortable['t'] = (0xf0, 0xe6, 0x8c)
    colortable['u'] = (0xff, 0xff, 0x54)
    colortable['v'] = (0xb0, 0xe0, 0xe6)
    colortable['w'] = (0x90, 0xee, 0x90)
    colortable['y'] = (0xff, 0x14, 0x93)
    colortable['z'] = (0xff, 0xa0, 0x7a)
    colortable['x'] = (0xee, 0x82, 0xee)
    colortable['*'] = (0xff, 0xc0, 0xcb)
    colortable['-'] = tuple(args.bg_color)

    if args.b_is is not None:
        if args.b_is == 'd':
            colortable['b'] = colortable['d']
        elif args.b_is == 'n':
            colortable['b'] = colortable['n']
    if args.j_is is not None:
        if args.j_is == 'l':
            colortable['j'] = colortable['l']
        elif args.j_is == 'i':
            colortable['j'] = colortable['i']
    if args.z_is is not None:
        if args.z_is == 'e':
            colortable['z'] = colortable['e']
        elif args.z_is == 'q':
            colortable['z'] = colortable['q']

    _main(args.input,
            args.output,
            args.pixel_size,
            args.aspect_ratio[0],
            args.aspect_ratio[1],
            tuple(args.bg_color),
            colortable)
