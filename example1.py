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


print("'for'-loop without suppressing the print inside the 'for'-loop out: \n")
# initializing progress bar
progressBar = ProgressBar(nElements=10, nIterations=10, suppressPrint=False)

progressBar.showEmptyBar()
print("This message will be shown right away")

for i in range(10):
    time.sleep(random.random() * 0.4)
    # as the printout is not suppressed the printout is shown right away
    # and the progress bar is moved down
    print("eval {}".format(i))
    # tell the progress bar that the next iteration was done
    progressBar.progress()

print("\n'for'-loop suppressing the print inside the 'for'-loop out: \n")
# initializing progress bar
progressBar = ProgressBar(nElements=35, nIterations=10, suppressPrint=True)

progressBar.showEmptyBar()
print("This message will be shown at the end")

for i in range(10):
    time.sleep(random.random() * 0.4)
    # as the printout is not suppressed, the printouts are saved and
    # shown after the for-loop is finished
    print("eval {}".format(i))
    # tell the progress bar that the next iteration was done
    progressBar.progress()
