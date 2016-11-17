progressbar-simple
==================

Another simple progress bar to show the progress of a for loop iteration process
in python working also for multiprocessing.

The progress bar has the following look::

	[###########		]

Installation
------------

Installation should be straight forward::

	pip install progressbar-simple

From Source
~~~~~~~~~~~

Alternativly, to get the most current version, the code can be installed from github as follows::

	git clone git@github.com:vgeck/progressBar.git
	cd progressBar
	pip install -r requirements.txt
	python setupy.py install

The last command might need sudo prefix, depending on your python setup.

Usage
-----

Assume a for loop with 100 iterations calling the function foo::

    for i in range(100):
        foo()

To monitor the process of the for loop we consider a progress bar with 10 
elements for the 100 iterations.
The progress bar is initialized with::
    
    from progressbarsimple import ProgressBar
    
    myProgressBar = ProgressBar(nElements = 10, nIterations = 100)
    
The progressBar is updated within the for loop with the iterator i::

    myProgressBar.progress(i)

The full code for the examples is::

    from progressbarsimple import ProgressBar
    
    myProgressBar = ProgressBar(nElements = 10, nIterations = 100)
    for i in range(100):
        foo()
        myProgressBar.progress(i)
    
For more information on how to use the progressbarsimple see the 2 example files.
