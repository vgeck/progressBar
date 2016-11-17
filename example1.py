#!/usr/bin/env python
# encoding: utf-8

# for python 2.7
from __future__ import print_function  
from __future__ import unicode_literals
from builtins import range

import random
from progressbarsimple import ProgressBar
import time

print("\nexample 1:")
print("a simple progress bar showing the progress of a silly 'for'-loop \n\n")


print("'for'-loop without subpressing the print inside the 'for'-loop out: \n")
# initializing progress bar
progressBar = ProgressBar(nElements = 35, nIterations = 10, subpressPrint = False)

for i in range(10):
    time.sleep(random.random()*0.4)
    # as the print out is no subpressed the printout is shown after right away
    # and the process bar is moved down
    print("eval {}".format(i))
    # feed the progress bar with the necessary progress information
    progressBar.progress(i)
    
print("\n'for'-loop subpressing the print inside the 'for'-loop out: \n")
# initializing progress bar
progressBar = ProgressBar(nElements = 35, nIterations = 10, subpressPrint = True)

for i in range(10):
    time.sleep(random.random()*0.4)
    # as stdout is redirected print outs here will be saved and 
    # shown after the for-loop is finished
    print("eval {}".format(i))
    # feed the progress bar with the necessary progress information
    progressBar.progress(i)
