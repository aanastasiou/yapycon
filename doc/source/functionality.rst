========================
Working with ``YaPyCon``
========================


The Python Console
==================

Assuming an uneventful :ref:`installation process <.._install_quickstart>`, you can now launch ``YaPyCon`` which 
gives you a familiar console window.

This is identical to an IPython session, provinding a Python language shell which can interpret Python directly.

This console however has minor knowledge of the fact that it was launched as a ``YASARA`` plugin, until you have
imported the ``yasara_kernel.py`` module.

This is usually the first thing to import in the console with a simple:

::

    > import yasara_kernel
    
    



Accessing the Jupyter Kernel
============================

* Launch a Jupyter notebook on the same computer
* Try to connect to an existing kernel
* Choose the one that is suggested by the notebook.
* You are now connected to the same kernel (and its context) via the jupyter notebook.
