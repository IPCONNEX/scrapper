#! /Users/omarelmohri/.venvs/lpthw/bin/python

__author__ = 'RicardoMoya'

from lib.ConnectionManager import ConnectionManager
import time

cm = ConnectionManager()
for j in range(5):
    for i in range(3):
        print ("\t\t" + str(cm.req("http://icanhazip.com/"))) # .read())
        time.sleep(3)
    cm.new_identity()