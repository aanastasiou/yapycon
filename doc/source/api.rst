===========
Plugin code
===========

The plugin code is split in two files:

1. ``yapycon.py`` For the actual code for the plugin.
2. ``yasara_kernel.py`` For all YASARA functionality available via the Python kernel.


``yapycon.py``
==============

.. note::
    The overall description of the ``yapycon`` plugin code in the following parts of the documentation,
    might appear puzzling and a bit random. It is not.

    YASARA uses the docstring of a plugin to determine where in its menu hierarchy to position
    the option to run the plugin, whether the plugin needs to be launched over a particular selection
    and other parameters.

    For more details about how this works and why the docstring of ``yapycon`` looks the way it does here,
    please check the full YASARA module documentation at the appendix, sections:

    * :ref:`moddoc_header_info`; and
    * :ref:`moddoc_docstring_details`

.. automodule:: yapycon.yapycon
    :members: YasaraContextRelayService, RpcServerThread


``yasara_kernel.py``
====================

.. note::
    ``yasara_kernel.py`` is *almost* identical to ``yasara.py``.

    The key differences are:

    1. ``yasara_kernel`` *excludes* certain YASARA functions that could bring the console in an indeterminate state
       (for example: ``StopPlugin(), Exit()``)
    2. ``yasara_kernel.py`` includes certain convenience functions that reformat the output of certain YASARA commands
       (such as: ``ListAtom(), ListBond()``
    1. Not all functions carry detailed documentation (e.g. via Sphinx's autodoc).

.. automodule:: yapycon.yasara_kernel
    :members: yapycon_get_connection_info,
              yapycon_reformat_atominfo_returned,
              yapycon_reformat_bondinfo_returned,
              yapycon_access_image_returned,
              SavePNG,
              LoadPNG,
              ListAtom,
              LoadPDB,
              ShowMessage,


.. Unfortunately, including the complete ``yasara_kernel.py`` in this page
.. makes it impractically long.
..
.. You can still review the code, either through github or by
.. :download:`downloading it from this link. <../../src/yasara_kernel.py>`
