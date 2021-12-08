.. _devnotes:

===============
Developer Notes
===============

YaPyCon is basically doing two things:

1. It launches a `QT Console for Jupyter <https://qtconsole.readthedocs.io/en/stable/>`_ **in its own process**.
2. It launches a Remote Procedure Call "server" (**in its own thread**) and links the context of the console with the
   context of the plugin.

Having a program launch a Python console to provide scripting capabilities to another program is the least difficult
part of this endeavour, thanks to projects like `qtconsole <https://qtconsole.readthedocs.io/en/stable/>`_.

The most "challenging" part is #2 and the main reason why YaPyCon works and "looks" the way it does.

To understand why, it is essential to understand how YASARA launches a plugin and how does that plugin communicate
back with the main process that launched it.


YASARA - Plugin communications
==============================

Let us first have a look at what happens when YASARA launches a plugin. Here is a diagram with all the key actors
involved:

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

Remarks
-------
The key points to note here are:

1. YASARA accepts commands about what to do via the ``stdout`` of the plugin process.
2. YASARA returns command results back to the plugin via a a local socket server
   that is launched as part of the initialisation process. [#]_
3. A *"YASARA command"* always implies a *Yanaconda command*.
   There are *"no actual Python bindings"*. All of the functions in ``yasara.py`` are very simple adapters that
   format a string with the equivalent Yanaconda command and pass it back to YASARA. This communication is handled
   by ``runretval()`` of the ``yasara.py`` module. Every one of the Python functions is structured along the following
   template:
   ::

       def some_function(p1, p2, pn=None):
           # Build the equivalent Yanaconda command
           yanaconda_string = f"SomeFunction parameter1={p1}, parameter2={p2}"
           if pn is not None:
               yanaconda_string += f" pn={pn}"
           # Send it to YASARA
           command_result = runretval(yanaconda_string)
           # Return the value to the Python code
           return command_result

   And here is a (simplified) view of what happens within ``runretval()``:

   ::

       def runretval(command):
           global com
           # If the Local_Socket_Server has not been initialised yet, initialise it here.
           if (com==None):
              com = yasara_communicator()

           # Use stdout to send the command to YASARA and use the Local_Socket_Server
           # port p to return the results.
           sys.stdout.write('ExecRV%d: '%com.port+command+'\n')
           sys.stdout.flush()
           # Accept the connection immediately
           com.accept()
           return(com.receivemessage(com.RESULT))

   At this point, try not to worry too much about "Pythonisms" or optimisations and focus on understanding
   the round-trip from Python function call to returning any results.


When is this not working?
=========================

This process works (has worked) sufficiently well as long as ``yasara.py`` is imported by **the same process that
launched the plugin**. In that case, the ``stdout`` that ``yasara.py`` is using is the exact same ``stdout`` that the
plugin "sees" as well and everything works well.

But, what is different when ``yasara.py`` is imported by a process that is **different** than the plugin process?

Just as it happens in the case of YaPyCon, the plugin itself launches the Python Console as a separate process [#]_.
This creates a complete mismatch in two points:

1. The ``stdout`` stream of the new processes is *entirely unrelated* to the ``stdout`` that YASARA is connected to.

   * For example, in the case of the Python Console, the ``stdout`` is simply redirected to the console itself.

2. Importing ``yasara.py`` from that separate process, will still go through the initialisation process
   (*"Initialise plugin variables"*), it will re-discover a completely different port ``p`` (launching yet another
   ``Local_Socket_Server``) and will attempt to pass that port information back to YASARA.
   **That** step will fail, because ``stdout`` **is not pointing back to YASARA**. At that point, the whole plugin
   hangs waiting for a response from the main YASARA program (that is now not even aware that a Yanaconda command
   was sent to it).

These two conditions render any subsequent use of ``import yasara`` from other processes entirely useless [#]_.

.. thumbnail:: resources/figures/fig_mermaid_when_comms_break.png


.. .. mermaid::
..     :caption: Simplified sequence diagram of importing ``yasara`` from a "secondary" process.
..
..     sequenceDiagram
..         autonumber
..         participant YASARA
..         participant Plugin
..         participant yasara.py_1
..         participant Local_Socket_Server_1
..         participant Python_Console
..         participant yasara.py_2
..         participant Local_Socket_Server_2
..
..         YASARA ->>Plugin: Launch plugin with <br/>request (r), listen on <br/>stdout for <br/>Yanaconda commands.
..         Plugin ->>yasara.py_1: import yasara
..         yasara.py_1 ->>yasara.py_1: Initialise plugin variables
..         yasara.py_1 ->>yasara.py_1: Discover a free port (p)
..         yasara.py_1 ->>Local_Socket_Server_1: Launch on port p <br/>
..         yasara.py_1 ->>YASARA: Pass p back to YASARA <br/> (as part of calling ``LoadStorage``)
..         yasara.py_1 ->>Plugin: Import complete, <br/> return to plugin <br/> code execution
..         Plugin->>Plugin: Examine (r)
..         Plugin->>Python_Console: Launch console
..         Python_Console->>yasara.py_2: import yasara
..         yasara.py_2 ->>yasara.py_2: Initialise plugin variables
..         yasara.py_2 ->>yasara.py_2: Discover a free port (p2)
..         yasara.py_2 ->>Local_Socket_Server_2: Launch on port p2 <br/>
..         rect rgb(232,88,88)
..         yasara.py_2 --xYASARA: Pass p2 back to ...
..         end

In this sequence, that last step is getting lost in the "pipework".

Remarks
-------

1. There is no need to launch a new local server because the plugin has already started one. That is
   not too problematic in itself, after all, YASARA only needs to know which server to send its response to.

2. The connection to the processes' ``stdout`` has been lost. Therefore, the ``runretval()`` of ``yasara.py`` *as
   imported from the console process* cannot communicate with the original YASARA process.


Adding Remote Procedure Calling
===============================

The solution to this situation was to find a way to "propagate" the already initialised variables, from
``yasara.py`` to any subsequent processes.

And this way was Remote Procedure Calling (RPC), via the `rpyc <https://rpyc.readthedocs.io/en/latest/>`_ module.

``rpyc`` provides a convenient mechanism for a Python program to call functions or access memory as if it was part of
the context of one process but in actual fact these residing elsewhere (in a different process or even different
computer). This solution is similar to launching yet another socket server but acting in an almost transparent way to
coordinate calls across the network.


Adding the ``yasara_kernel.py`` module
======================================

In a typical YASARA plugin, ``yasara.py`` must be the first module to be imported by a plugin for it to be able to
communicate with the main YASARA program.

Similarly, from within the Python console, the first thing to do is to import ``yasara_kernel.py``.

The two modules are *almost* identical. However, in developing YaPyCon it was quickly realised that:

1. For backwards compatibility and the stability of YASARA, it was not possible to alter the existing ``yasara.py`` at
   all.
2. ``yasara.py`` provided access to a number of functions that could work in a "self-destructing" way if launched from
   within YaPyCon. For example, allowing ``Exit()`` could lead to "zombie" processes where the
   Python Console could still go on after having sent a command to YASARA to close.
3. Decoupling ``yasara_kernel.py`` from ``yasara.py`` provided an additional flexibility to modify the structure of
   the module without worrying about the effect of these modifications to existing plugins.

   * Part of these modifications was to add functions for "unpacking" certain result types as returned by YASARA, for
     convenience. In any case, such "unpacking" is expected to commonly occur in a given plugin, apart from trivial
     cases.



How YaPyCon works
=================

Having described all this, a simplified view of the main actors in the communications between the YASARA Python Console
and the main process of YASARA now looks like this:

.. thumbnail:: resources/figures/fig_mermaid_yapycon_operation.png


.. .. mermaid::
..     :caption: Simplified sequence diagram of the most important actors in the communications between the Python
..               Console and YASARA.
..
..     sequenceDiagram
..         autonumber
..         participant YASARA
..         participant YaPyCon_Plugin
..         participant yasara.py
..         participant Local_Socket_Server
..         participant Python_Console
..         participant yasara_kernel.py
..         participant RPC_Server
..
..
..         YASARA ->>YaPyCon_Plugin: Launch plugin with <br/>request (r), listen on <br/>stdout for <br/>Yanaconda commands.
..         YaPyCon_Plugin ->>yasara.py: import yasara
..         yasara.py ->>yasara.py: Initialise plugin variables
..         yasara.py ->>yasara.py: Discover a free port (p)
..         yasara.py ->>Local_Socket_Server: Launch on port p <br/>
..         yasara.py ->>YASARA: Pass p back to YASARA <br/> (as part of calling ``LoadStorage``)
..         yasara.py ->>YaPyCon_Plugin: Import complete, <br/> return to plugin <br/> code execution
..         YaPyCon_Plugin->>YaPyCon_Plugin: Examine (r)
..         YaPyCon_Plugin->>RPC_Server: Launch server at 18861
..         YaPyCon_Plugin->>Python_Console: Launch console
..         Python_Console->>yasara_kernel.py: import yasara_kernel
..         yasara_kernel.py->>RPC_Server: Connect
..         yasara_kernel.py->>RPC_Server: Get proxy <br/>objects from yasara.py
..         RPC_Server->>YaPyCon_Plugin: Get proxy objects
..         YaPyCon_Plugin->>RPC_Server: Return proxy objects
..         RPC_Server->>yasara_kernel.py:Return proxy objects
..         yasara_kernel.py->>yasara_kernel.py: Initialise local <br/> plugin variables
..         yasara_kernel.py->>Python_Console:Continue execution
..         Python_Console->>Python_Console:Enter Read-Eval-Print Loop

For more details about each of the points mentioned in this section, please see :ref:`api`

-----

.. [#] This process is simplified here for economy of space. More accurately, the discovery of a free port and the
       socket server binding are handled by class ``yasara_communicator`` that is "constructed" as part of the
       ``LoadStorage()`` command. The latter is called as part of the ``yasara.py`` initialisation of variables.

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
