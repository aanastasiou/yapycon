.. _api:

==================
Code documentation
==================

The plugin functionality is split in two files:

1. ``yapycon.py``

   * For the actual code of the plugin.


2. ``yasara_kernel.py``

   * For all YASARA functionality available within YaPyCon.



``yapycon.py``
==============

.. note::
    The description of the ``yapycon`` plugin code in the following parts of the documentation,
    might show up as a random collection of ``MainMenu, PullDownMenu``, etc, statements.

    It is not.

    YASARA uses the docstring of a plugin to determine where in its menu hierarchy to position
    the option to run the plugin, whether the plugin needs to be launched over a particular selection
    and other parameters that are passed to it when YASARA launches it.

    For more details about how this works and why the docstring of ``yapycon`` looks the way it does here,
    please see the following sections:

    * :ref:`moddoc_header_info`; and
    * :ref:`moddoc_docstring_details`

.. automodule:: yapycon.yapycon
    :members: YasaraContextRelayService, RpcServerThread


``yasara_kernel.py``
====================

.. automodule:: yapycon.yasara_kernel
    :members: yapycon_get_connection_info,
              yapycon_reformat_atominfo_returned,
              yapycon_reformat_bondinfo_returned,
              yapycon_access_image_returned,
              SavePNG,
              RayTrace,
              LoadPNG,
              ListAtom,
              LoadPDB,
              ShowMessage,


.. Unfortunately, including the complete ``yasara_kernel.py`` in this page
.. makes it impractically long.
..
.. You can still review the code, either through github or by
.. :download:`downloading it from this link. <../../src/yasara_kernel.py>`
