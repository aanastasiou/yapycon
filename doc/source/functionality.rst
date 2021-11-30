========================
Working with ``YaPyCon``
========================


The Python Console
==================

Assuming an uneventful :ref:`installation process <.._install_quickstart>`, you can now launch ``YaPyCon``. This is
identical to an IPython session, providing a Python language shell which executes Python directly.

This console however has minor knowledge of the fact that it was launched as a ``YASARA`` plugin. You can still
execute arbitrary Python code in it (e.g. ``3+2``) but you cannot interact with ``YASARA``.

To achieve this, you should first import the ``yasara_kernel.py`` module. This is usually the first thing to import
with a simple:

::

    In [1]: import yasara_kernel

Or, if you do not want to prefix every command with ``yasara_kernel.``, import as:

::

    In [1]: from yasara_kernel import *

Assuming you have used the latter to import ``yasara_kernel``, you will find that you now have complete access to
the usual variables that are exposed to a  plugin by ``YASARA``.

For example, go ahead and check the ``owner`` information that is hard-coded in the software for you:

::

    In [3]: owner.familyname
    Out[3]: 'Anastasiou'

    In [4]: owner.firstname
    Out[4]: 'Athanasios'


And of course, you now also have complete access to the complete ``YASARA`` Python API with all the useful features
that the console offers, such as, auto-complete.

The console appears like any other application window, so, to close it, simply click on the ``X`` at the top right-hand
side of the window.



Accessing the Jupyter Kernel
============================

When you start the Python console, you are actually starting a Jupyter kernel and connect to it too. This kernel
is exposed to the system and it can be accessible via a Jupyter notebook too, which makes for some very useful ways
of interacting with ``YASARA``.

To connect your Jupyter notebook to a running instance of ``YASARA``:

1. Launch ``YASARA``
2. Launch the console
3. Launch a Jupyter notebook on the same computer
4. Try to connect to an existing kernel
5. Choose the one that is suggested by the notebook.
6. You are now connected to the same kernel (and its context) via the jupyter notebook.
