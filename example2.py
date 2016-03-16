#!/usr/bin/env python
# encoding: utf-8

from progressBar import ProgressBar
import multiprocessing, time

def foo(uselessInput):
    """
    Function foo running a silly for loop to waste some time
    
    Args:
	uselessInput (any): not used input, just needed for the pool map function
    
    Returns:
        minutesSolve: minutes needed for iterating through the for-loop
        secsSolve: seconds needed for iterating through the for-loop
    """
    timeStart = time.clock()
    for i in xrange(1000):
        i+100*i
    time.sleep(0.2)
    timeSolverSolve = time.clock()-timeStart
    minutesSolve = int(timeSolverSolve/60.)
    secsSolve = timeSolverSolve-minutesSolve*60.
    return minutesSolve,secsSolve


# start timing of the hole process
timeStartBatch = time.time()

# define a batch data list iterator
batchDataList = range(100)
numberWorkers = multiprocessing.cpu_count()
# create a multiprocess iterator named "results"
pool = multiprocessing.Pool(numberWorkers)
results = pool.imap_unordered(foo, batchDataList)
pool.close() 

# create a loading bar 
nElements = 50
nSteps = len(batchDataList)
progressBar = ProgressBar(nElements, nSteps)

print '====================================='
print '------Multiprocessing Batch Job------'
print 'numberWorkers:   {}'.format(numberWorkers)
print 'numberOfEval.:   {}'.format(len(batchDataList))

# run the batch jobs
while (True):
    completed = results._index
    # feed the progress bar with the necessary progress information
    progressBar.progress(completed)
    if (completed == len(batchDataList)): break
pool.join()

# print the results of all the batch simulations
print '====================================='
for batchJobIndex,[minutesSolve,secsSolve] in enumerate(results):
    print '____________Batch   {:5} ___________'.format(batchJobIndex+1) 
    print 'Runtime:        {} min {} sec'.format(minutesSolve,secsSolve)
print '====================================='
# print the time needed for the hole process
timeBatchJob= time.time()-timeStartBatch
minutesBatch = int(timeBatchJob/60.)
secsBatch = timeBatchJob-minutesBatch*60.
print 'total runtime:  {} min {} sec'.format(minutesBatch,secsBatch)
print '====================================='
