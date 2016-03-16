#!/usr/bin/env python
# encoding: utf-8

import numpy as np
from progressBar import ProgressBar
import time

print "example 1 for a simple progress bar showing the progress of a silly for loop"

# initializing progress bar
progressBar = ProgressBar(nElements = 35, nIterations = 10)

for i in xrange(10):
    time.sleep(np.random.rand()*0.4)
    # as stdout is redirected print outs here will be saved and shown after the for-loop is finished
    print "eval",i
    # feed the progress bar with the necessary progress information
    progressBar.progress(i)