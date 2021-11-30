===============
Developer Notes
===============

1. Split the code in modules
2. Update the code to only Python3 (python2 has been withdrawn even)
3. Get rid of the retvalused hack
4. Turn constants to CAPITALS
5. Improve reporting errors from within YASARA to the plugin.
6. Use f-strings as much as possible (speed-up)


``YASARA`` Plugins
===================

* YASARA publishes a `yasara.py` at `<YASARA_HOME_DIRECTORY>/plg` that plugins should import prior to executing any commands.
* `yasara.py` disguises itself as an API when it is really only two functions:
  * `runretval()` Or "Run and return a value"
  * `retvalused()` to receive a "traceback" object.
* All other commands from `yasara.py` are convenience functions that are there only to create specific messages, pass them back 
  to YASARA and retrieve their "effect".

* When YASARA launches a plugin, it basically launches Python with the plugin file as an argument (as one process) and then pipes the standard streams
  back to the main process.




The link between YASARA and Python
==================================

* The full specification of the way YASARA communicates with Python plugins is available in :ref:`the original 
  docstring docs of the yasara.py module <.. _source_module_doc:>`

  
* Open questions:

   * Is it possible / required to have more than one plugins active at the same time?
   * Does yasara launch each process in its own thread and communications?
   * These questions would help in determining if having a single RPC instance would be alright
   
   
* Structure of `yasara.py`
  * `plg_in` A "plugin class" which yasara uses to "package" information about a plugin
  * `num_descriptor, obj_descriptor, mod_descriptor, res_descriptor, atom_descriptor, sel_descriptor` Simple containers 
    for selections, etc.
  * `yasara_communicator` Handles the `YASARA --> Plugin` branch of the communication (See section *"Plugins can start additional programs that control YASARA, like a Python module"*
    as well).
  * `runretval(), retvalused()` functions that handle the `Plugin --> YASARA` branch of the communication.
  * From that point onwards, all functions are the "exposed YASARA Python API". In actual fact, all of these functions
    are constructing a suitable *"string"* which they pass to `runretval()`.     
    * Some of these API functions return values, others do not.
      * When a function needs something to be returned from YASARA it will raise a "server", pass the port of the server
        to YASARA (as part of the command) and then YASARA will connect to that port and dump its return value.
        
* Initialisation
  * `yasara.py` runs some initialisation the last part of which (loading persistent data form a previous run)
    might be problematic when executed through a single RPC.
    
    
* `RPC Initialisation`

  1. Try to start a registry:
     * If you get `Address already in use` then the registry already runs which means that the RPC part is running 
       and you only have to connect to it.
     * If the registry service **IS** started, then this is the first time the plugin is activated.
       * Create the *Service*
       * Create and connect a client to the *Service*
       * Have `retval, runretval` to connect to the *Service*
       
  2. After step #1 is succesful, launch the kernel, connect to the kernel
  
  3. Once in the python console, re-import the yasara.py plugin (this now connects to the existing instance).
  
* The relay service touches 3 points:
  * Initialisation of the yasara.py module
  * `runretval()`
  * `StopPlugin()`

       
     
    


