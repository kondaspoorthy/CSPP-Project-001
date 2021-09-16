"""Implementing the cat shell command in python.""".py
import sys
from lib.helper import cat, readfile
import requests

TEXT = None
ARG_CNT = len(sys.argv) - 1
#  This is a comment
if ARG_CNT == 0:
    TEXT = sys.stdin.read()

if ARG_CNT == 1:
    filename = sys.argv[1]
    TEXT = readfile(filename)

if ARG_CNT > 1:
    print(sys.argv[0], "doesn't handle more than one argument")

print(cat(TEXT))

