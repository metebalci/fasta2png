#!/usr/bin/env python3

from fasta2png import _generate_png
import argparse
import sys

def _main(in_file,
          out_file,
          multi_mode,
          pixel_size,
          aspect_width,
          aspect_height,
          bg_color,
          colortable):
    if multi_mode == 'f' or multi_mode == 'c':
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
                    print('seqdesc: %s' % line[1:].strip())
                    if out_file is None:
                        out_file = line[1:].strip() + '.png'
                    # if multi_mode == f, use the first only
                    # if multi_mode == c, combine all sequences in the file
                    if multi_mode == 'f' and first_seq_found:
                        break
                    first_seq_found = True
                # comment ?
                elif line[0] == ';':
                    pass
                else:
                    seqline = line.strip()
                    # ignore last * if there is one
                    if seqline[-1] == '*':
                        seqline = seqline[0:-1]
                    seq = seq + seqline
        seq = seq.lower()
        # u and t is same for the purpose of this program
        seq = seq.replace('u', 't')
        print('seqlen: %d' % len(seq))
        _generate_png(seq,
                out_file,
                pixel_size,
                aspect_width,
                aspect_height,
                bg_color,
                colortable)
    elif multi_mode == 's':
        seq = ''
        seqnum = 1
        current_out_file = None
        with open(in_file, 'r') as f:
            while True:
                line = f.readline()
                # end of file ?
                if len(line) == 0:
                    break
                # description ?
                elif line[0] == '>':
                    # save current seq
                    if len(seq) > 0:
                        seq = seq.lower()
                        # u and t is same for the purpose of this program
                        seq = seq.replace('u', 't')
                        print('seqlen: %d' % len(seq))
                        _generate_png(seq,
                                      current_out_file,
                                      pixel_size,
                                      aspect_width,
                                      aspect_height,
                                      bg_color,
                                      colortable)
                        seqnum = seqnum + 1
                        seq = ''
                    print('seqdesc: %s' % line[1:].strip())
                    if out_file is None:
                        current_out_file = line[1:].strip() + '.png'
                    else:
                        current_out_file = '%s%d.png' % (out_file, seqnum)
                # comment ?
                elif line[0] == ';':
                    pass
                else:
                    seqline = line.strip()
                    # ignore last * if there is one
                    if seqline[-1] == '*':
                        seqline = seqline[0:-1]
                    seq = seq + seqline
    else:
        raise Exception('invalid --multi-mode')

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--input', required=True,
            help='input (fasta/fna) file name')
    parser.add_argument('--output',
            help='output (rgba png) file name, if not given name/unique identifier in the file is used')
    parser.add_argument('--multi-mode',
            default="first",
            help='choose how to process multi-FASTA files, ' \
                 '[f]irst, [s]eparate or [c]ombined\n')
    parser.add_argument('--pixel-size',
                        type=int,
                        default=1,
                        help='size of a (nucleotid) base in final png in pixels, default is 1')
    parser.add_argument('--aspect-ratio',
                        type=int,
                        nargs=2,
                        default=[1, 1],
                        help='aspect ratio, provide as two integers representing width and height, default is 1 1')
    parser.add_argument('--bg-color',
                        type=int,
                        nargs=4,
                        default=[0, 0, 0, 255],
                        help='background color rgba, 4 integers, default is opaque black')
    # visually distinct colors
    # from https://mokole.com/palette.html
    parser.add_argument('--color-a',
                        type=int,
                        nargs=4,
                        default=[0xff, 0, 0, 0xff],
                        help='color of base Adenine, 4 integers, default is opaque red')
    parser.add_argument('--color-g',
                        type=int,
                        nargs=4,
                        default=[0, 0xff, 0, 0xff],
                        help='color of base Guanine, 4 integers, default is opaque lime')
    parser.add_argument('--color-c',
                        type=int,
                        nargs=4,
                        default=[0, 0, 0xff, 0xff],
                        help='color of base Cytosine, 4 integers, default is opaque blue')
    parser.add_argument('--color-t',
                        type=int,
                        nargs=4,
                        default=[0x87, 0xce, 0xfa, 0xff],
                        help='color of base Thymine (and Uracil), 4 integers, default is opaque light sky blue')
    parser.add_argument('--color-n',
                        type=int,
                        nargs=4,
                        default=[0xff, 0xff, 0xff, 0xff],
                        help='color of any other code in the sequence, 4 integers, default is opaque white')
    args = parser.parse_args()
    colortable = {}
    colortable['a'] = tuple(args.color_a)
    colortable['g'] = tuple(args.color_g)
    colortable['c'] = tuple(args.color_c)
    colortable['t'] = tuple(args.color_t)
    colortable['n'] = tuple(args.color_n)
    _main(args.input,
          args.output,
          args.multi_mode[0],
          args.pixel_size,
          args.aspect_ratio[0],
          args.aspect_ratio[1],
          tuple(args.bg_color),
          colortable)
