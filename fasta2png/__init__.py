
from PIL import Image, ImageDraw
import math


def _generate_png(seq,
        out_file,
        pixel_size, 
        aspect_width, 
        aspect_height, 
        bg_color, 
        colortable):
    im_unit = math.floor(math.sqrt(len(seq)/(aspect_width*aspect_height)))
    w = im_unit * aspect_width
    h = im_unit * aspect_height
    while len(seq) > (w*h):
        h = h + 1
    im_width = w * pixel_size
    im_height = h * pixel_size
    im = Image.new('RGBA', (im_width, im_height), color=bg_color)
    draw = ImageDraw.Draw(im)
    curr = 0
    for y in range(0, h):
        for x in range(0, w):
            if curr == len(seq):
                break
            base = seq[curr]
            x0 = x * pixel_size
            y0 = y * pixel_size
            draw.rectangle([x0, 
                y0, 
                x0+pixel_size, 
                y0+pixel_size],
                fill=colortable.get(base, colortable['n']))
            curr = curr + 1
    del draw
    im.save(out_file, 'PNG')
