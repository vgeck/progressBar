# progressBar
Another simple progress bar to show the progress of a for loop iteration process
in python working also for multiprocessing.

The progress bar has the following look:

[###########         ]

Examples:
    create a progress bar with 20 elements for a loop with 200 iterations 
    and loop over the 200 iteration
    
    >>> progressBar = ProgressBar(20, 200)
    [                    ]
    
    >>> for i in range(200): progressBar.progress(i)
    [###################]
    <BLANKLINE>
    
    create a progress bar with 2 elements for a loop with 12 iterations 
    and loop over the 12 iterations
    
    >>> progressBar = ProgressBar(2, 12)
    [  ]
    >>> for i in range(12): progressBar.progress(i)
    [##]
    
    create a progress bar with 5 elements for a loop with 10 iterations 
    check the print out after iteration 5, 7 and 10 respectively
    
    >>> progressBar = ProgressBar(5, 10)
    [     ]
    >>> progressBar.progress(2)
    [#    ]
    >>> progressBar.progress(7)
    [##   ]
    >>> progressBar.progress(10)
    [#####]
    <BLANKLINE>
    
For more information on how to use the progress bar see the 2 example files.