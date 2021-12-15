==========
Motivation
==========

The primary motivation behind developing YaPyCon was the long overhead time associated with rapidly prototyping plugins
and "experiments" within YASARA.

To understand better what this overhead "problem" is, it is essential to understand some key concepts around YASARA.


YASARA and its scripting capability
-----------------------------------

YASARA is an excellent piece of software to carry out a large (and ever expanding) number of bio-informatics tasks.
Its acronym *"Yet Another Scientific Reality Application"* is not at all a marketing
"creative exaggeration". It really does, to the extent that it is possible and accurate, turn a computer or cluster
of computers, into a virtual laboratory. A laboratory where the user has direct access to a long list of methods
often developed by original research carried out by YASARA Biosciences staff [#]_.

Just as it happens in a real research laboratory and environment, sometimes the available tools have to be tweaked
slightly to achieve certain objectives. Perhaps a sensor needs to be sampled at a higher frequency, a parameter
monitored to trigger another event or measurement and so on.

YASARA enables its users to adapt its existing functionality to their needs via its own macro language,
called `Yanaconda <http://www.yasara.org/yanaconda.htm>`_ [#]_ for which *an interactive console already exists* within
YASARA, accessible by hitting Space:

.. thumbnail:: resources/figures/fig_yanaconda_console.png

At the very least, Yanaconda will allow you to try out constructing a new "experiment" within YASARA, right from
the console or by running a macro (i.e. A yanaconda script saved to a file), to direct YASARA to carry out a series of
actions.

Yanaconda is remotely similar to Python and if you already have some background in programming, its syntax might
seem alien at first, especially if you try to employ data structures that are slightly more complicated than
a simple variable.

YASARA also has a very simple (and effective) support for launching **and interfacing** with Python plugins. This
capability however is tightly coupled with Yanaconda.

YASARA will basically launch a new Python process (selecting the currently active Python interpreter), that executes
the plugin script. Everything within the plugin script is familiar Python code and the script itself can import other
modules and data to achieve its objectives. **All** of the commands that are exposed to Yanaconda are also available
to the plugin via the ``yasara.py`` Python module, with minor syntactic differences.

Here is an illustrative example using the ``ShowMessage()`` function from the earlier screenshot:

* **In Yanaconda:**

  ::

     > ShowMessage "Hello World"

  *or*

  ::

    > ShowMessage Text="Hello World"

* **In Python:**

  ::

    ShowMessage("Hello World")

  *or*

  ::

    ShowMessage(text="Hello World")

YASARA also defines a Domain Specific Language (DSL) that is parsed from the plugin docstrings and that
allows a YASARA plugin to:

1. Modify the YASARA menu structure (e.g. create a new menu entry to launch a particular plugin)
2. Launch standard YASARA system dialogs (e.g. select a subset of objects already loaded in a YASARA scene **and then**
   launch the plugin on **that** particular selection).
3. Allow plugins to create whole user interfaces to collect information that is then made available to a plugin when
   launching it.

...and, that is it.

The "problem"
-------------

The specific problem that YaPyCon solves is that of the overhead required to develop a YASARA Python plugin in its
current form.

This overhead is demonstrated here through a number of illustrative notes:

1. The documentation is primarily geared towards Yanaconda.

   * Although the documentation is doing a very good job at explaining the different forms of a command and how
     it may appear whether in Yanaconda or Python, there is some slight vagueness about the parameters or behaviour
     of a command.

   * A prime example of this is the ``ListHBo<Atom|Res|Mol|Obj>()`` command(s). The command that queries all data
     available to YASARA about the hydrogen bonds of a molecule at the level of atoms, residues, molecules or objects.

   * The in-program documentation describes its Yanaconda version in great detail and when it comes to the explanation
     of the ``results`` parameter, it reads:

     *"The Results parameter defines the number of results to be returned per hydrogen bond (it does not affect the
     printout in the console). The number of available results depends on the final selection unit:"*

     So, given a ``results=5`` and 100 bonds returned by this command, does this mean that the list of returned
     results is a list of 100 elements, each of them a list of 5 numbers each? ...Or, 500 elements where it is
     implied that elements ``0..4`` belong to the first bond, elements ``5..8`` belong to the second bond and so on?

     The correct answer here is the latter. That is, YASARA will return a **single list** with
     ``number_of_bonds * results`` elements and it is up to the user to "unwind" or repackage it into something more
     readable (or usable) in Python.

     This is not exactly clear from that explanation and is only hinted at in the example (Yanaconda) code that is
     provided along with that command.


2. Trying out the effect of a command requires the user to write a complete plugin.

   * Continuing from point #1, if you are new to YASARA and you are reading the in-program documentation for a
     particular command, the first thing you might want to do is "try it out" in **Python**.

     * To do this, you first have to *write a complete plugin skeleton script*.

       * To do this, you really have to understand **exactly** how plugins work, **BEFORE** you are able to run
         even a plain simple "Hello World".

   * This is not exactly trivial (and also complicated by point #3, below). To get an idea about what it involves,
     please see the actual YASARA plugin documentation at the Appendix of YaPyCon's documentation,
     `here <source_module_doc>`_

     * *Please note:* An additional resource to address this point is the cookiecutter template YaPlTemp. For more
       information please `see here <https://github.com/aanastasiou/yapltemp>`_. In fact, YaPyCon was bootstrapped via
       YaPlTemp.

3. Writing plugins in an "interactive" way (rapid prototyping) is time consuming:

   * Continuing from point #2, let's assume that you have gone through the basics of setting up a plugin and you now
     have a working skeleton that you use to quickly test ideas.

   * At its very minimum, this process involves:

     1. Activating the Python environment
     2. Starting YASARA
     3. Launching the plugin
     4. Examining the output
     5. Shutting down the plugin gracefully
     6. Altering the code
     7. Going back to step 3, until requirements are met.

   * Because of the way YASARA launches and handles plugins, it might "hang" or fail to launch a particular plugin
     without returning enough information to the console about the nature of the error. These occurrences are rare
     and depend very much on the nature of the plugin but sooner or later become part of the intuition of working
     with YASARA.

   * For example, if for any reason your source file has been "corrupted" by an editor that ignores Python's formatting
     requirements or one of the imported modules has failed to load, the plugin might hang at an exception that does not
     find its way back to YASARA. This might cause the plugin to execute partially, *before* hitting the
     ``yasara.plugin.end()`` statement that is required by all plugins to terminate gracefully. As a result of this,
     we now have to restart YASARA itself, effectively losing any unsaved progress up to that point.

The Yasara Python Console (YaPyCon)
-----------------------------------

YaPyCon was born out of these little "frustrations" that are further amplified when the objective is **not** to
learn how to program YASARA but to actually achieve a particular objective.

The operation of YaPyCon is based on two big parts: A standard Python Console and a Remote Procedure Calling mechanism.
Developing the plugin was a really... fun experience with many twists and turns, all of which are explained in detail in
:ref:`devnotes`.

-----


.. [#] For more information please see `this list <http://www.yasara.org/sciencenews.htm>`_

.. [#] Absolutely no relationship to `Anaconda <https://www.anaconda.com/>`_, Yanaconda's acronym means
       *"Yet ANother Abridged COding 'N' Development Approach"* (YANACONDA), anything else is a plain reptile species
       wordplay confusion.


