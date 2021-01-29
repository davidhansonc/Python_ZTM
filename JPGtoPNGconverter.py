# -*- coding: utf-8 -*-
# @Author: davidhansonc
# @Date:   2021-01-07 12:04:59
# @Last Modified by:   davidhansonc
# @Last Modified time: 2021-01-07 15:50:40
import os, sys, re
from PIL import Image

def converter(infile, in_path, out_path):
    f, e = os.path.splitext(infile)
    outfile = f + ".png"
    if infile != outfile:
        if not os.path.exists(out_path):
            os.mkdir(out_path)
        infile = in_path + infile
        outfile = out_path + f + ".png"
        try:
            with Image.open(infile) as im:
                im.save(outfile)
        except OSError:
            print("cannot convert", infile)


osrig_dir = sys.argv[1]
new_dir = sys.argv[2]

for filename in os.listdir(orig_dir):
    jpg_check = re.compile("(\S+)(\.jpg)")  # Filters for only jpeg files
    if jpg_check.match(filename):
        converter(filename, orig_dir, new_dir)
    else:
        continue