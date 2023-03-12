#!/usr/bin/env/python

from gcmt_ndk_parser import ParseNDKtoGCMT
import os



print(os.listdir("./data"))
parse = ParseNDKtoGCMT("./data/GCMTcatalogue_ndk_end2012.txt")

parse = parse.read_file()
# print(parse.data)

# with open('/home/bwwj/gcmt_tools/gcmt/data/GCMTcatalogue_ndk_end2012.txt', 'r') as f:
#     print(f.readlines())