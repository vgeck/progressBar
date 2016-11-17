#!/usr/bin/env python
# encoding: utf-8

import sys
import io

#for python 2.7
from builtins import range

class ProgressBar(object):
    """
    progress bar to show the progress of a for loop iteration process in python
    working also for multiprocessing
    
    with the following look:
    
    [###########         ]
    
    Examples:
    
        create a progress bar with 20 elements for a loop with 200 iterations 
        and loop over the 200 iteration
        
        >>> progressBar = ProgressBar(20, 200)
        [                    ]
        
        >>> for i in range(200): progressBar.progress(i)
         \b\b \b\b \b\b \b\b \b\b \b\b \b\b \b\b \b\b \b\b \b\b \b\b \b\b \b\b \b\b \b\b \b\b \b\b \b\b \b\b \b\b \b\b[####################]
        <BLANKLINE>
        
        create a progress bar with 2 elements for a loop with 12 iterations 
        and loop over the 12 iterations
        
        >>> progressBar = ProgressBar(2, 12)
        [  ]
        
        >>> for i in range(12): progressBar.progress(i)
         \b\b \b\b \b\b \b\b[# ] \b\b \b\b \b\b \b\b[##]
        <BLANKLINE>
        
        create a progress bar with 5 elements for a loop with 10 iterations 
        check the print out after iteration 5, 7 and 10 respectively
        
        >>> progressBar = ProgressBar(5, 10)
        [     ]
        >>> progressBar.progress(2)
         \b\b \b\b \b\b \b\b \b\b \b\b \b\b[#    ] 
        >>> progressBar.progress(7)
         \b\b \b\b \b\b \b\b \b\b \b\b \b\b[###  ]
        >>> progressBar.progress(10)
         \b\b \b\b \b\b \b\b \b\b \b\b \b\b[#####] 
        <BLANKLINE>
        
        create a progress bar with 5 elements for a loop with 10 iterations 
        check the print out after iteration 5, 7 and 10 respectively
        
        >>> progressBar = ProgressBar(5, 10)
        [     ]
        >>> progressBar.clearScreen(5)
         \b\b \b\b \b\b \b\b \b\b
        >>> progressBar.writeProgress(2)
        [##   ]
          
    """
    def __init__(self, nElements, nIterations, subpressPrint = True):
        """
        Initialization of the the progress bar, prints out the brackets of 
        the progress bar immediately
        
        All outputs to stdout will be captured and displayed after the 
        progress bar is fully loaded.

        Args:
            nElements (int): number of elements of the progress bar
            nIterations (int): number of iterations of the process which 
            progress should be displayed
            subpressPrint (bool): subpress print out statements of function
            in the function which is looped
        """
        
        self.subpressPrint = subpressPrint
        # handle for stdout
        self.stdout = sys.stdout
        # buffer for stdout outputs
        self.outputBuffer = io.StringIO()
        # redirect system stdout to buffer
        sys.stdout = self.outputBuffer
        
        self.finished = False
        
        self.nElements = nElements
        self.nIterations = float(nIterations)
        self.eCount = 0.

        self.writeProgress(self.eCount)
        

    def clearScreen(self, dCount):
        """
        Clear the screen by writing ' \b\b' dCount times to stdout
        
        Args:
            dCount (int): number of elements to backspace
        """
        # write backspaces to the start of the loading bar
        backspacing = ''.join([' \b\b' for i in range(dCount)])
        self.stdout.write(backspacing)
        self.stdout.flush()


    def writeProgress(self, eCount):
        '''
        Writes the progress bar with eCount #-elements to stdout
        
        Args:
            eCount (int): number of #-elements to write
        '''
        if eCount > self.nElements: eCount = self.nElements
        spaces = int(self.nElements-eCount)
        prog = ''.join([''.join(['#' for i in range(int(eCount))]),\
                        ''.join([' ' for i in range(spaces)])])
        loadingBar = ''.join(['[',prog,']'])
        self.stdout.write(loadingBar)
        self.stdout.flush()
        

    def progress(self, currentIteration):
        """
        checks the progress of the adjoin process, and advances the progress 
        bar # if necessary
        
        Args:
            currentIteration (int): number of the current iterations of the 
            adjoin process
        """
        if self.finished == False:

            # completed tasks of the process in percent
            loopPercentage = currentIteration/(self.nIterations-1.) 
            # completed shown progress in percent
            barPercentage = self.eCount/self.nElements
            
            while (barPercentage <= loopPercentage):
                
                self.clearScreen(self.nElements+2)

                if self.subpressPrint == False:
                    toPrint = self.outputBuffer.getvalue()
                    self.stdout.write(toPrint)                
                    self.stdout.flush()
                    self.outputBuffer.truncate(0)

                self.writeProgress(self.eCount)
                self.eCount += 1.
                barPercentage = self.eCount/self.nElements
            
            if loopPercentage >= 1.:
                
                self.stdout.write("\n")
                self.stdout.flush()
                sys.stdout = self.stdout
                sys.stdout.write(self.outputBuffer.getvalue())
                sys.stdout.write("\n")
                self.outputBuffer.close() 
                self.finished = True
        
        
if __name__ == '__main__':
    import doctest
    doctest.testmod()
    
        
