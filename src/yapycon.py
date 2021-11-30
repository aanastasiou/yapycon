# YASARA PLUGIN
# TOPIC:       Utilities
# TITLE:       YaPyCon
# AUTHOR:      Athanasios Anastasiou
# LICENSE:     GPL
# DESCRIPTION: YASARA Python Console
# PLATFORMS:   Windows

"""
MainMenu: Window
  PullDownMenu after Update frequency: Python Console
    Request: YaPyCon
"""

import yasara
import IPython
from qtconsole.rich_ipython_widget import RichIPythonWidget
from qtconsole.inprocess import QtInProcessKernelManager
from IPython.lib import guisupport
import tornado
import sys
import time
import threading
from rpyc.utils.server import OneShotServer, ThreadedServer
from rpyc import Service

# Not applicable anymore 
# def init_asyncio_patch():
    # if sys.platform.startswith("win") and sys.version_info >=(3, 8) and tornado.version_info < (6, 1):
        # import asyncio
        # try:
            # from asyncio import (
            # WindowsProactorEventLoopPolicy,
            # WindowsSelectorEventLoopPolicy)
        # except ImportError:
            # pass
        # else:
            # if type(asyncio.get_event_loop_policy()) is WindowsProactorEventLoopPolicy:
                # asyncio.set_event_loop_policy(WindowsSelectorEventLoopPolicy())
                
class YasaraStdoutRelayService(Service):
    """
    An rpyc service that re-uses the stdout of the plugin process.
    """
    def __init__(self):
        super().__init__()
        self._my_stream = sys.stdout
        
    def exposed_stdout_relay(self, payload):
        # sys.stdout.write(payload)
        # sys.stdout.flush()
        self._my_stream.write(payload)
        self._my_stream.flush()
    
def start_rpc():
    """
    Starts yet another thread for the RPC server.
    
    Notes:
        * Unfortunately this is required here because .start() of rpyc blocks
    """
    
    q = OneShotServer(YasaraStdoutRelayService(), port=18861)
    q.start()
    
def stop():
    """
    Destructor callback for the kernel.
    """
    q.close()
    v.join()
    kernel_client.stop_channels()
    kernel_manager.shutdown_kernel()
    app.exit()    
    yasara.plugin.end()
    
v = None
q = None
if (yasara.request == "YaPyCon"):
    app = guisupport.get_app_qt4()
    
    # Launch RPC thread
    v = threading.Thread(target=start_rpc)
    v.start()
    
    # Create the in-process kernel
    kernel_manager = QtInProcessKernelManager()
    kernel_manager.start_kernel()
    
    kernel = kernel_manager.kernel
    kernel.gui='qt4'
    kernel_client = kernel_manager.client()
    kernel_client.start_channels()
    
    # This creates the widget (which is not strictly necessary, might have an option to turn it off).
    control = RichIPythonWidget()
    control.kernel_manager = kernel_manager
    control.kernel_client = kernel_client
    control.exit_requested.connect(stop)
    control.show()
    guisupport.start_event_loop_qt4(app)
    yasara.plugin.end()
