# YASARA PLUGIN
# TOPIC:       Utilities
# TITLE:       YaPyCon
# AUTHOR:      Athanasios Anastasiou
# LICENSE:     GPL
# DESCRIPTION: YASARA Python Console
# PLATFORMS:   Windows

"""
MainMenu: Window
  PullDownMenu after Update frequency: PythonConsole
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

def init_asyncio_patch():
    if sys.platform.startswith("win") and sys.version_info >=(3, 8) and tornado.version_info < (6, 1):
        import asyncio
        try:
            from asyncio import (
            WindowsProactorEventLoopPolicy,
            WindowsSelectorEventLoopPolicy)
        except ImportError:
            pass
        else:
            if type(asyncio.get_event_loop_policy()) is WindowsProactorEventLoopPolicy:
                asyncio.set_event_loop_policy(WindowsSelectorEventLoopPolicy())
                
def stop():
    kernel_client.stop_channels()
    kernel_manager.shutdown_kernel()
    app.exit()
    yasara.plugin.end()
    

if (yasara.request == "YaPyCon"):
    app = guisupport.get_app_qt4()
    
    # Create the in-process kernel
    kernel_manager = QtInProcessKernelManager()
    kernel_manager.start_kernel()
    
    kernel = kernel_manager.kernel
    kernel.gui='qt4'
    kernel_client = kernel_manager.client()
    kernel_client.start_channels()
    
    control = RichIPythonWidget()
    control.kernel_manager = kernel_manager
    control.kernel_client = kernel_client
    control.exit_requested.connect(stop)
    control.show()
    guisupport.start_event_loop_qt4(app)
    yasara.plugin.end()
