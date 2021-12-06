===============
Developer Notes
===============

YaPyCon is basically doing two things:

1. It launches a `QT Console for Jupyter <https://qtconsole.readthedocs.io/en/stable/>`_ **in its own process**.
2. It launches a Remote Procedure Call "server" (**in its own thread**) and links the context of the console with the
   context of the plugin.

The most "challenging" part is #2 and the main reason why YaPyCon works and "looks" the way it does.

But first, why would anyone want to do any of this?

Motivation
==========

YASARA is an excellent piece of software to carry out a large (and ever expanding) number of bio-informatics related
tasks...and more. Its acronym *"Yet Another Scientific Reality Application"* is not at all a marketing inspired
"creative exaggeration". It really does, to the extent that it is possible and accurate, turn a computer
(or more), into a virtual laboratory.

And just as it happens in a real research laboratory, sometimes the available tools have to be tweaked slightly to
achieve certain objectives. Perhaps a sensor needs to be sampled at a higher frequency, a parameter monitored and
subsequently triggering other events or measurements and so on.

YASARA enables its users to adapt its existing functionality to their needs in a number of different ways:

1. It has its own macro language, called `Yanaconda <http://www.yasara.org/yanaconda.htm>`_ [#]_ and that language
   *already has a console* within YASARA, accessible by hitting Space:

   .. thumbnail:: resources/figures/fig_yanaconda_console.png

   At the very least, Yanaconda will allow you to try out constructing a new "experiment" within YASARA, right from
   the console or by running a macro (i.e. A yanaconda script saved to a file).

   Yanaconda is remotely similar to Python and if you already have some background in programming, its syntax might
   seem a bit alien at first, especially if you try to employ data structures that are slightly more complicated than
   a simple variable.

2. It has very simple (and effective) support for launching **and interfacing** with Python plugins.
   YASARA will basically launch a new Python process (selecting the currently active Python interpreter), that executes
   the plugin script.

   Everything within the plugin script is familiar Python code and the script itself can import other modules and data
   to achieve its objectives.

   **All** of the commands that are exposed to Yanaconda are also available to the plugin via the ``yasara.py``
   Python module, with some syntactic differences and some (minor) semantic differences as well. Here is an
   illustrative example using the ``ShowMessage()`` function from the earlier screenshot:

   * **Yanaconda:**

     ::

         > ShowMessage "Hello World"

     *or*

     ::

        > ShowMessage Text="Hello World"

   * **Python:**

     ::

        ShowMessage("Hello World")

     *or*

     ::

        ShowMessage(text="Hello World")

In addition to this, YASARA also defines a Domain Specific Language (DSL) that is parsed from the plugin docstrings that
allows a YASARA plugin to:

1. Modify the YASARA menu structure (e.g. create a new menu entry to launch a particular plugin)
2. Launch standard YASARA system dialogs (e.g. select a subset of objects already loaded in a YASARA scene **and then**
   launch the plugin on that particular selection).
3. Allow plugins to create whole user interfaces to collect information that is then made available to a plugin when
   launching it.

...and, that is it.

So, what is the "problem"?
--------------------------

The specific problem that YaPyCon solves is that of the overhead required to develop a YASARA Python plugin in its
current form.

This overhead is demonstrated here through a number of illustrative notes:

1. The documentation is primarily geared towards Yanaconda.

   * Although the documentation is doing a very good job at explaining the different forms of a command and how
     it may appear whether in Yanaconda or Python, there is some slight vagueness about the exact result of a command.

   * A prime example of this is the ``ListHBo<Atom|Res|Mol|Obj>()`` command(s). The command that queries all data
     available to YASARA about the hydrogen bonds of a molecule at the level of atoms, residues, molecules or objects.

   * The in-program documentation describes its Yanaconda version in great detail. When it comes to the explanation
     of the ``results`` parameter, it reads:

     *"The Results parameter defines the number of results to be returned per hydrogen bond (it does not affect the
     printout in the console). The number of available results depends on the final selection unit:"*

     So, given a ``results=5`` and 100 bonds returned by this command, does this mean that the list of returned
     results is a list of 100 elements, each of them a list of 5 numbers each? ...Or, 500 elements where it is
     implied that elements ``0..4`` belong to the first bond, elements ``5..8`` belong to the second bond and so on?

     The second case is the correct answer here. YASARA will return a **single list** with
     ``number_of_bonds * results`` long and it is up to the user to "unwind" or repackage it into something a bit more
     readable in Python.

     This is not exactly clear from that explanation and is only "clarified" in the in-program documentation example
     provided along with that command.


2. Trying out the effect of a command requires the user to write a complete plugin.

   * If you are new to YASARA and you are reading the in-program documentation for a particular command, the first
     thing you might want to do is "try it out" in **Python**.

     * But, to do this, you first have to *write a complete plugin skeleton script*.

       * And to do this, you really have to understand **exactly** how plugins work, **BEFORE** you are able to run
         even a plain simple "Hello World".

   * This is not exactly trivial (and also complicated by point #3, below). To get an idea about what this involves,
     please see the actual YASARA plugin documentation at the Appendix of YaPyCon's documentation,
     `here <source_module_doc>`_

3. Writing plugins in an "interactive" way (rapid prototyping) is time consuming:

   * Let's assume that you have gone through the basics of setting up a plugin and you now have a working
     skeleton that you use to quickly test ideas.

   * At its very minimum, this process involves:

     1. Starting YASARA
     2. Launching the plugin
     3. Examining its output
     4. Shutting down the plugin
     5. Altering the code
     6. Going back to step 2, until requirement is not met.

   * Because of the way YASARA launches and handles plugins, it might "hang" or fail to launch a particular plugin
     without returning enough information to the console about the nature of the error.

   * For example, if for any reason your source file has been "corrupted" by an editor that ignores Python's formatting
     requirements or one of the imported modules has failed to load, the plugin might hang at an exception that does not
     find its way back to YASARA. This might cause the plugin to execute partially, *before* hitting the
     ``yasara.plugin.end()`` statement that is required by all plugins to terminate gracefully. As a result of this,
     we now have to restart YASARA itself, effectively losing any unsaved progress up to that point.

The Yasara Python Console (YaPyCon)
-----------------------------------

YaPyCon was born out of these little "frustrations" the effect of which is amplified when the objective is **not** to
learn how to program in YASARA but to actually achieve a particular objective.

So, why not give YASARA a proper Python console?

YaPyCon Internals
=================

Having a program launch a Python console to provide scripting capabilities to another program is the least difficult
part of this endeavour, thanks to projects like `qtconsole <https://qtconsole.readthedocs.io/en/stable/>`_.

The key problem that YaPyCon had to solve was "simulating" the effect of ``yasara.py`` **from a separate process**.

YASARA - Plugin communications
------------------------------

To understand better the challenges behind this point, let's have a look at what happens when YASARA launches a plugin:

.. mermaid::
    :caption: Simplified sequence diagram of the plugin launching process.

    sequenceDiagram
        participant YASARA
        participant Plugin
        participant yasara.py
        participant Local_Socket_Server
        YASARA ->>Plugin: Launch plugin with <br/>request (r), listen on <br/>stdout for <br/>Yanaconda commands.
        Plugin ->>yasara.py: import yasara
        yasara.py ->>yasara.py: Initialise plugin variables
        yasara.py ->>yasara.py: Discover a free port (p)
        yasara.py ->>Local_Socket_Server: Launch on port p <br/>
        yasara.py ->>YASARA: Pass p back to YASARA <br/> (as part of calling ``LoadStorage``)
        yasara.py ->>Plugin: Import complete, <br/> return to plugin <br/> code execution
        Plugin ->>Plugin: Examine (r), <br/>proceed accordingly.

And, having described the initialisation part, let us now try to "call" a YASARA command from within Python, for example
``ListAtom()`` :

.. mermaid::
    :caption: Simplified sequence diagram of "calling" a YASARA command with return results.

    sequenceDiagram
        participant YASARA
        participant Plugin
        participant yasara.py
        participant Local_Socket_Server

        Plugin->>yasara.py: yasara.ListAtom("all")
        yasara.py->>yasara.py: Create equivalent <br/>Yanaconda ListAtom <br/> command (c)
        yasara.py->>YASARA: Send c via stdout
        YASARA->>YASARA: Execute ListAtom, obtain result (r)
        YASARA->>Local_Socket_Server: Connect to p,  send r
        yasara.py->>Local_Socket_Server: Read r
        yasara.py->>Plugin: return r

The key points to note here are:

1. YASARA accepts commands about what to do via the ``stdout`` of the plugin process.
2. When YASARA wants to pass results back to the plugin process, it connects to a local socket server
   that is launched as part of the initialisation process. [#]_
3. There are *"no actual Python bindings"*. All of the functions in ``yasara.py`` are very simple interfaces that
   format a string with the equivalent Yanaconda command and pass it back to YASARA. This is a subtle point but useful
   in explaining a particular behaviour that occurs later on, when you forget to close the yanaconda console from
   within YASARA.

Where things break
------------------
This process works (has worked) remarkably well as long as ``yasara.py`` is imported by **the same process that launched
the plugin**. In that case, ``stdout`` is ``stdout``, ``stderr`` is ``stderr`` and everything works well.

But, what is different when ``yasara.py`` is imported by a process that is **different** than the plugin process?

Just as it happens in the case of YaPyCon, the plugin itself launches the Python Console as a separate process [#]_.
This creates a complete mismatch in two points:

1. The ``stdout`` stream of the new processes is *entirely unrelated* to the ``stdout`` that YASARA is connected to.

   * For example, in the case of the Python Console, the ``stdout`` is simply redirected to the console itself.

2. ``yasara.py`` will still go through the initialisation process (*"Initialise plugin variables"*), it will
   re-discover a completely different port ``p`` (launching yet another ``Local_Socket_Server``) and will attempt
   to pass that port information back to YASARA but will fail because ``stdout`` **is not pointing back to YASARA**.

These two conditions render any subsequent use of ``import yasara`` from other processes entirely useless [#]_.

.. mermaid::
    :caption: Simplified sequence diagram of importing ``yasara`` from a "secondary" process.

    sequenceDiagram
        participant YASARA
        participant Plugin
        participant yasara.py_1
        participant Local_Socket_Server_1
        participant Python_Console
        participant yasara.py_2
        participant Local_Socket_Server_2

        YASARA ->>Plugin: Launch plugin with <br/>request (r), listen on <br/>stdout for <br/>Yanaconda commands.
        Plugin ->>yasara.py_1: import yasara
        yasara.py_1 ->>yasara.py_1: Initialise plugin variables
        yasara.py_1 ->>yasara.py_1: Discover a free port (p)
        yasara.py_1 ->>Local_Socket_Server_1: Launch on port p <br/>
        yasara.py_1 ->>YASARA: Pass p back to YASARA <br/> (as part of calling ``LoadStorage``)
        yasara.py_1 ->>Plugin: Import complete, <br/> return to plugin <br/> code execution
        Plugin->>Plugin: Examine (r)
        Plugin->>Python_Console: Launch console
        Python_Console->>yasara.py_2: import yasara


.. [#] Absolutely no relationship to `Anaconda <https://www.anaconda.com/>`_, Yanaconda's acronym means
       *"Yet ANother Abridged COding 'N' Development Approach"* (YANACONDA), anything else is a plain reptile species
       wordplay confusion.

.. [#] This process is simplified here for economy of space. More accurately, the discovery of a free port and the
       socket server binding are handled by class ``yasara_communicator`` that is "constructed" as part of the
       ``LoadStorage()`` command.

.. [#] Again, this is a simplification for economy of space and scope. In actual fact, the Python console is launched as
       a set of processes, threads and communication channels because of the way the Jupyter protocol operates. A full
       description of that would be out of the scope of this document but mich more information is available at the
       `Messaging in Jupyter section <https://jupyter-client.readthedocs.io/en/stable/messaging.html>`_ in the main
       ``jupyter_client`` documentation.

.. [#] This is not unknown to the YASARA developers. In fact, ``yasara.py`` includes a workaround that allows one
       to take control of YASARA from a browser. This is solved via launching yet another ``Local_Socket_Server`` and
       more information is available at :ref:`plugin_plumbing`



.. It would not be an exaggeration if
.. It has been in development since 1993 (in one form or another)
..
..
.. 1. Split the code in modules
.. 2. Update the code to only Python3 (python2 has been withdrawn even)
.. 3. Get rid of the retvalused hack
.. 4. Turn constants to CAPITALS
.. 5. Improve reporting errors from within YASARA to the plugin.
.. 6. Use f-strings as much as possible (speed-up)
.. 7. SaveWob does'nt work in View?
.. 8. SaveSTL as well as a number of other formats does not exist in the Python version.
.. 9. Because of the way the plugin is initialised, it is impossible to use sphinx to document it.
.. 10. Provide a mechanism for plugins to call different functions internally (e.g. on_request(request_string) and
..     have that function call separate functions.


.. YASARA Plugins
.. ==============
..
.. * YASARA publishes a `yasara.py` at `<YASARA_HOME_DIRECTORY>/plg` that plugins should import prior to executing any commands.
.. * `yasara.py` disguises itself as an API when it is really only two functions:
..   * `runretval()` Or "Run and return a value"
..   * `retvalused()` to receive a "traceback" object.
.. * All other commands from `yasara.py` are convenience functions that are there only to create specific messages, pass them back
..   to YASARA and retrieve their "effect".
..
.. * When YASARA launches a plugin, it basically launches Python with the plugin file as an argument (as one process) and then pipes the standard streams
..   back to the main process.

.. The link between YASARA and Python
.. ==================================
..
.. * The full specification of the way YASARA communicates with Python plugins is available in :ref:`the original
..   docstring docs of the yasara.py module <source_module_doc>`
..
..
.. * Open questions:
..
..    * Is it possible / required to have more than one plugins active at the same time?
..    * Does yasara launch each process in its own thread and communications?
..    * These questions would help in determining if having a single RPC instance would be alright
..
..
.. * Structure of `yasara.py`
..   * `plg_in` A "plugin class" which yasara uses to "package" information about a plugin
..   * `num_descriptor, obj_descriptor, mod_descriptor, res_descriptor, atom_descriptor, sel_descriptor` Simple containers
..     for selections, etc.
..   * `yasara_communicator` Handles the `YASARA --> Plugin` branch of the communication (See section *"Plugins can start additional programs that control YASARA, like a Python module"*
..     as well).
..   * `runretval(), retvalused()` functions that handle the `Plugin --> YASARA` branch of the communication.
..   * From that point onwards, all functions are the "exposed YASARA Python API". In actual fact, all of these functions
..     are constructing a suitable *"string"* which they pass to `runretval()`.
..     * Some of these API functions return values, others do not.
..       * When a function needs something to be returned from YASARA it will raise a "server", pass the port of the server
..         to YASARA (as part of the command) and then YASARA will connect to that port and dump its return value.
..
.. * Initialisation
.. * `yasara.py` runs some initialisation the last part of which (loading persistent data form a previous run)
.. might be problematic when executed through a single RPC.
..
..
.. * `RPC Initialisation`
..
..   1. Try to start a registry:
..      * If you get `Address already in use` then the registry already runs which means that the RPC part is running
..        and you only have to connect to it.
..      * If the registry service **IS** started, then this is the first time the plugin is activated.
..        * Create the *Service*
..        * Create and connect a client to the *Service*
..        * Have `retval, runretval` to connect to the *Service*
..
..   2. After step #1 is succesful, launch the kernel, connect to the kernel
..
..   3. Once in the python console, re-import the yasara.py plugin (this now connects to the existing instance).
..
.. * The relay service touches 3 points:
..   * Initialisation of the yasara.py module
..   * `runretval()`
..   * `StopPlugin()
