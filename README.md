# progressBar
Another simple progress bar to show the progress of a for loop iteration process
in python working also for multiprocessing.

The progress bar has the following look:

[###########         ]

## Usage:

Assume a for loop with 100 iterations calling the function foo:

    for i in range(100):
        foo()

To monitor the process of the for loop we consider a progress bar with 5 
elements for the 100 iterations.
The progress bar is initialized with:
    
    from progressBar import ProgressBar
    progressBar = ProgressBar(nElements = 10, nIterations = 100)
    
Now the progressBar needs to know the current status of the for loop iterator,
within the for loop:

    progressBar.progress(i)

The full code for the examples is:

    progressBar = ProgressBar(nElements = 10, nIterations = 100)
    for i in range(100):
        foo()
        progressBar.progress(i)
    
For more information on how to use the progress bar see the 2 example files.