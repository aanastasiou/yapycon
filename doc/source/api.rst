===========
Plugin code
===========


``yapycon.py``
==============

This section includes the entirety of the main plugin code
with all of its explanatory inline comments.

.. .. literalinclude:: ../../src/yapycon.py

.. automodule:: src.yapycon
    :members: YasaraContextRelayService, RpcServerThread

``yasara_kernel.py``
====================

.. automodule:: src.yasara_kernel
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
