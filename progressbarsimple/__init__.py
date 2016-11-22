# encoding: utf-8
"""
Another simple progress bar

progress bar to show the progress of a loop iteration process in python
working also for multiprocessing with the following look:

    [###########         ]

Examples:

    a simple progress bar showing the progress of a silly 'for'-loop
    without suppressing the print inside the 'for'-loop out::

    progressBar = ProgressBar(nElements=2, nIterations=2, suppressPrint=False)
    progressBar.showEmptyBar()
    print("This message will be shown right away")

    for i in range(2):
         # as the printout is not suppressed the printout is shown right away
         # and the progress bar is moved down
         print("eval {}".format(i))
         # tell the progress bar that the next iteration was done
         progressBar.progress()
"""

import sys
import io

#for python 2.7
from builtins import range


def progressBarStringGenerator(nElements):
    '''
    Create progress bar with eCount #-elements

    Args:
        eCount (int): number of #-elements to write

    Yields:
        str: the progress bar with next amount of #-elements

    Examples:
        genearte a progressBarStringGenerator for 2 elements, and
        progress it through
        >>> pBSG = progressBarStringGenerator(2)
        >>> next(pBSG)
        '[  ]'
        >>> next(pBSG)
        '[# ]'
        >>> next(pBSG)
        '[##]'
    '''
    eCount = 0
    while eCount < nElements + 1:
        yield "[{}]".format(("#"*int(eCount)).ljust(nElements))
        eCount += 1

def progressBarGenerator(nElements,
                         nIterations,
                         outputBuffer,
                         stdoutHandle,
                         suppressPrint):
    """
    Progress bar generator function.

    Args:
        nElements (int): number of progress bar #-elements
        nIterations (int): number of loop-iterations
        outputBuffer (StringIO): StringIO file instance in which sys.stdout
        was redirected
        stdoutHandle (sys.stdout): local handle of sys.stdout
        suppressPrint (bool): show print outs of loop-function after or while
        looping.

    Examples:
        generate a progressBarGenerator for 2 elements, and
        check all iterations
        >>> pBG = progressBarGenerator(2,2,io.StringIO(),sys.stdout,False)
        >>> next(pBG) == u'\\x08 \\x08\\x08 \\x08\\x08 \\x08\\x08 \\x08[  ]'
        True
        >>> print('suppressPrint is False')
        suppressPrint is False
        >>> next(pBG) == u'\\x08 \\x08\\x08 \\x08\\x08 \\x08\\x08 \\x08[# ]'
        True
        >>> next(pBG) == u'\\x08 \\x08\\x08 \\x08\\x08 \\x08\\x08 \\x08[##]\\n\\n'
        True
    """
    currentIteration = 0.
    eCount = 0.
    localProgressBarStringGenerator = progressBarStringGenerator(nElements)
    nIterations = nIterations + 1
    while currentIteration < nIterations:
        progressBarOutputString = ""
        # completed tasks of the process in percent
        loopPercentage = currentIteration / (nIterations - 1)
        # completed shown progress in percent
        barPercentage = eCount / nElements
        while barPercentage <= loopPercentage:
            progressBarOutputString += '\b \b' * (nElements + 2)
            if suppressPrint is False:
                progressBarOutputString += outputBuffer.getvalue()
                outputBuffer.truncate(0)
            progressBarOutputString += next(localProgressBarStringGenerator)
            eCount += 1.
            barPercentage = eCount / nElements

        if loopPercentage >= 1.:
            progressBarOutputString += ("\n" + outputBuffer.getvalue() + "\n")
            # redirect stdout
            sys.stdout = stdoutHandle
            # close outputBuffer
            outputBuffer.close()

        yield progressBarOutputString
        currentIteration += 1

class ProgressBar(object):
    """
    progress bar to show the progress of a loop iteration process in python
    working also for multiprocessing with the following look:

    [###########         ]

    """
    def __init__(self, nElements, nIterations, suppressPrint=True):
        """
        Initialization of the the progress bar, prints out the brackets of
        the progress bar immediately

        All outputs to stdout will be captured and displayed after the
        progress bar is fully loaded.

        Args:
            nElements (int): number of elements of the progress bar
            nIterations (int): number of iterations of the process which
            progress should be displayed
            suppressPrint (bool): subpress print out statements of function
            in the function which is looped
        """
        # handle for stdout
        self.stdout = sys.stdout
        # buffer for stdout outputs
        outputBuffer = io.StringIO()
        # redirect system stdout to buffer
        sys.stdout = outputBuffer

        self.currentIterationMultiprocessing = 0
        self.emptyShowed = False

        self.progressBarGenerator = progressBarGenerator(nElements,
                                                         float(nIterations),
                                                         outputBuffer,
                                                         self.stdout,
                                                         suppressPrint)

    def showEmptyBar(self):
        """
        shows the empty progress bar
        if not called by the user, it is done automatically
        """
        self.emptyShowed = True
        self.progress()

    def progress(self):
        """
        checks the progress of the adjoin process, and advances the progress
        bar # if necessary
        """
        if self.emptyShowed is False: self.showEmptyBar()
        progressBar = next(self.progressBarGenerator)
        self.stdout.write(progressBar)
        self.stdout.flush()

    def progressMultiprocessing(self, iterationStatus):
        """
        checks the progress of the adjoin process, and advances the progress
        bar # if necessary

        Args:
            iterationStatus (int): index of the current iteration in the extern loop
        """
        if iterationStatus != self.currentIterationMultiprocessing:

            while iterationStatus - self.currentIterationMultiprocessing > 0:
                progressBar = next(self.progressBarGenerator)
                self.currentIterationMultiprocessing += 1

            self.stdout.write(progressBar)
            self.stdout.flush()

if __name__ == '__main__':
    import doctest
    doctest.testmod()
