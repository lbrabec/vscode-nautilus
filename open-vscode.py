import os
import shlex
import gi

gi.require_version('Nautilus', '3.0')
gi.require_version('GConf', '2.0')

from gi.repository import Nautilus, GObject, GConf

# Python 2 and 3 compatibility hack
try:
    from urllib import unquote
except ImportError:
    from urllib.parse import unquote


class OpenVSCodeExtension(Nautilus.MenuProvider, GObject.GObject):
    def __init__(self):
        self.client = GConf.Client.get_default()

    def _open_vscode(self, locations):
        # remove file:// from uri and remove escapes
        locations = [unquote(location.get_uri()[7:]) for location in locations]

        # shell quote locations
        locations = [shlex.quote(location) for location in locations]

        os.system('code %s' % ' '.join(locations))

    def menu_activate_cb(self, menu, locations):
        self._open_vscode(locations)

    def menu_background_activate_cb(self, menu, location):
        self._open_vscode([location])

    def get_file_items(self, window, files):
        """
        right click on file(s)/dir(s)
        """

        # not sure if this method can be invoked with empty files param
        if len(files) == 0:
            return

        # check if selected items start with file://
        if any([f.get_uri_scheme() != 'file' for f in files]):
            return

        item = Nautilus.MenuItem(
            name='NautilusPython::openvscode_file_item',
            label='Open VS Code',
            tip='Open selected files with VS Code'
        )

        item.connect('activate', self.menu_activate_cb, files)
        return item,

    def get_background_items(self, window, file):
        """
        right click on background (black space in nautilus)
        """
        item = Nautilus.MenuItem(
            name='NautilusPython::openvscode_bg_item',
            label='Open VS Code',
            tip='Open this directory with VS Code'
        )

        item.connect('activate', self.menu_background_activate_cb, file)
        return item,