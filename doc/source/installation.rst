============
Installation
============


.. _install_quickstart:

Quickstart
==========

Read this section if:

* You already have a working YASARA installation
* You already know what *"Python"* and *"virtual environment"* are 
  and you can start YASARA with a specific virtual environment activated first.

For more details on the installation process, please see section :ref:`installation_install_from_scratch`.


Installation
------------

1. Download the
   `latest release of YaPyCon <https://github.com/aanastasiou/yapycon/releases/latest/download/yapycon.zip>`_ (or
   `clone the repository <https://github.com/aanastasiou/yapycon/>`_).

2. Decompress ``yapycon.zip`` to a directory on your computer.

3. Create a new Python virtual environment that includes YaPyCon's requirements (see ``requirements.txt`` from
   ``yapycon.zip``).

   * Or ensure that the virtual environment of your choice includes the packages listed in ``requirements.txt``.

4. Ensure that the environment variable ``YASARA_HOME`` points to the top level directory where YASARA is installed.

   * This is the directory that you launch the YASARA executable (``yasara`` or ``yasara.exe``) from.
   * *In Linux*, this can be set with:
     ::

         > export YASARA_HOME=some/directory/yasara

   * *In MS Windows:* Bring up your "Environment Variables" dialog, from "System Properties" (Open your start menu
     and look for "Edit the system environment variables". That set of dialogs looks like this:

     .. thumbnail:: resources/figures/fig_win_env_vars_latest.png

5. Run ``install_plugin`` from the *decompressed* YaPyCon release archive.

6. Drop to a terminal, activate the Python environment and launch YASARA.

If everything has gone well, you will see a *"Python Console"* option added under the *"Window"* menu option:

.. thumbnail:: resources/figures/fig_showing_option.png


.. _installation_install_from_scratch:

Installing from scratch
=======================

A typical **full installation** process is divided into three parts:

Install YASARA
--------------

* Go to `this URL <http://www.yasara.org/viewdl.htm>`_ to download YASARA View. This is the entry level
  YASARA and freely available.
 
 * You will soon receive an email with a unique URL that leads to an installer executable. This installation process is
   identical for all "stages" of YASARA.
   
* The installer is a self-extracting executable that will install YASARA in a ``yasara/`` directory right
  in the *Current Working Directory*. This installation location is referenced throughout the documentation as 
  ``<YASARA_HOME_DIRECTORY>``.

* This installs the main piece of software but YASARA will attempt to pick up the *currently active* Python
  interpreter when it launches. It is now important to ensure that the *"currently active"* Python interpreter has the
  necessary pre-requisites installed. This is achieved in the following steps.
     

Install Python or a virtual environment
---------------------------------------

1. On **MS Windows:**, the quickest option would be to install some "flavour" of
   `conda <https://docs.conda.io/en/latest/index.html>`_
   
2. On **Linux:**, the quickest option would be to use `virtualenv <https://wiki.python.org/moin/Virtualenv>`_

3. Create a virtual environment making sure that all the packages mentioned in ``requirements.txt`` are included.

   * ``YaPyCon`` requires ``PyQt5, IPython, qtconsole, Sphinx, rpyc``
   
4. Activate the virtual environment that has the pre-requisites installed.

   * See `this link <https://docs.conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html>`_ for 
     ``conda`` or `this link <https://virtualenv.pypa.io/en/latest/index.html#>`_ for ``virtualenv``.
     

Install the ``YaPyCon`` plugin
------------------------------

If your system now includes a working YASARA installation with a properly prepared virtual environment, you are
now ready to install and launch ``YaPyCon``.

The steps to do this are identical to the description in :ref:`install_quickstart`


Removing YaPyCon
================

To uninstall YaPyCon, simply run the script ``uninstall_plugin`` from the *decompressed* YaPyCon release archive.

