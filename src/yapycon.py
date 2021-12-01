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

              
class YasaraContextRelayService(Service):
    """
    An rpyc service that re-uses the stdout of the plugin process.
    """
    def __init__(self):
        super().__init__()
        self._my_stream = sys.stdout
        self._plugin = yasara.plugin
        self._request = yasara.request
        self._opsys = yasara.opsys
        self._version = yasara.version
        self._serialnumber = yasara.serialnumber
        self._stage = yasara.stage
        self._owner = yasara.owner
        self._permissions = yasara.permissions
        self._workdir = yasara.workdir
        self._selection = yasara.selection
        self._com = yasara.com

    def exposed_get_plugin(self):
        return self._plugin

    def exposed_get_request_str(self):
        return self._request

    def exposed_get_opsys(self):
        return self._opsys

    def exposed_get_version(self):
        return self._version

    def exposed_get_serialnumber(self):
        return self._serialnumber

    def exposed_get_stage(self):
        return self._stage

    def exposed_get_owner(self):
        return self._owner

    def exposed_get_permissions(self):
        return self._permissions

    def exposed_get_workdir(self):
        return self._workdir

    def exposed_get_selection(self):
        return self._selection

    def exposed_get_com(self):
        return self._com

    def exposed_stdout_relay(self, payload):
        # sys.stdout.write(payload)
        # sys.stdout.flush()
        self._my_stream.write(payload)
        self._my_stream.flush()


class RpcServerThread(threading.Thread):
    def __init__(self):
        super().__init__()
        self._serv_object = ThreadedServer(YasaraContextRelayService(),
                                           port=18861,
                                           protocol_config={"allow_public_attrs": True})

    def run(self):
        self._serv_object.start()

    def stop_server(self):
        self._serv_object.close()


if yasara.request == "YaPyCon":
    # Create the qt handle for the console "app"
    app = guisupport.get_app_qt4()

    # Launch RPC thread
    rpc_serv = RpcServerThread()
    rpc_serv.start()
    
    # Create the in-process kernel
    kernel_manager = QtInProcessKernelManager()
    kernel_manager.start_kernel()
    
    kernel = kernel_manager.kernel
    kernel.gui = "qt"
    kernel_client = kernel_manager.client()
    kernel_client.start_channels()
    
    # TODO: MID, Maybe have an option to turn the widget off and simply launch the kernel.
    # This creates the widget (which is not strictly necessary for the server)
    control = RichIPythonWidget()
    control.kernel_manager = kernel_manager
    control.kernel_client = kernel_client
    # Widget goes to visible
    control.show()
    # Start the event loop
    # This call blocks until the user closes the window of the application.
    guisupport.start_event_loop_qt4(app)
    # Application is shutting down.
    # Stop the RPC "bridge"
    rpc_serv.stop_server()
    # Stop the kernel
    kernel_client.stop_channels()
    kernel_manager.shutdown_kernel()
    # Signal the end of the plugin and get back to YASARA
    yasara.plugin.end()
