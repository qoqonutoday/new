#!/usr/bin/env python3

import sys
import re

if not len(sys.argv) == 3:
        sys.stderr.write("USAGE: python3 %s < annotations file  > < data file >\n" % sys.argv[0])
        sys.exit(1)

annots_file = sys.argv[1]
data_file = sys.argv[2]

try:
    with open(annots_file) as f:
        pass
    with open(data_file) as f:
        pass
except FileNotFoundError:
    print("File(s) do(es) not exist or is not accessible!!!")
    sys.exit(1)

def construct_lookup_dict(annots_file):
    annotations_list = [line.rstrip('\n') for line in open(annots_file)]

    # get rid of header line
    annotations_list.pop(0)

    # build annotation dict
    lookup_annotation = {}
    for line in annotations_list:
        key,value = line.split('\t',1)
        lookup_annotation[ key ] = value

    return lookup_annotation

def annotate_data_file(data_file, lookup_annotation):
     with open(data_file) as f:
        while 1:
            line = f.readline().strip()
            if line == "":
                # Reached the end of the record or end of the file
                break

            fields = line.split()
            if lookup_annotation.get(fields[0],0):
                #print(fields[0], lookup_annotation[fields[0]])
                fields[0] = lookup_annotation[fields[0]]

            print('\t'.join(fields))


lookup_annotation = construct_lookup_dict(annots_file)
annotate_data_file(data_file, lookup_annotation)
