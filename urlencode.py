#!/usr/bin/python
# -*- coding: utf8 -*-
#  Url Encode Plugin
#
#  Copyright (C) 2013 Ariel Allon
#
#  Credit where it's due: 
#    - Micah Carrick's invaluable tutorial (http://www.micahcarrick.com/writing-plugins-for-gedit-3-in-python.html)
#    - Marco Cripa's Convert Special gedit plugin. (http://krypt77.altervista.org/download/gedit/Convert_special_3_0.zip)
#      Structure below apapted from that plugin.
#
#  This program is free software: you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation, either version 3 of the License, or
#  (at your option) any later version.
#
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#
#  You should have received a copy of the GNU General Public License
#  along with this program.  If not, see <http://www.gnu.org/licenses/>.

from gi.repository import GObject, Gedit, Gtk, Gdk
import urllib

ui_str = """
<ui>
  <menubar name="MenuBar">
    <menu name="EditMenu" action="Edit">
      <placeholder name="EditOps_6">
        <menu name="UrlCharacters" action="UrlCharacters">
          <menuitem name="UrlEncode" action="UrlEncode"/>
          <menuitem name="UrlDecode" action="UrlDecode"/>
        </menu>
      </placeholder>
    </menu>
  </menubar>
</ui>
"""

class UrlEncodePlugin(GObject.Object, Gedit.WindowActivatable):
    __gtype_name__ = "UrlEncode"
    window = GObject.property(type=Gedit.Window)
    
    def __init__(self):
        GObject.Object.__init__(self)
    
    def do_activate(self):
        """Add the controls to the menu."""
        actions = [
          ('UrlCharacters',None, 'Url Characters'),
          ('UrlEncode',None, 'Url encode','<Control><Alt>u','Url encode selected text',self.UrlEncode),
          ('UrlDecode',None, 'Url decode','<Control><Alt>v','Url decode selected text',self.UrlDecode)
          ]
          
        self._actions = Gtk.ActionGroup("UrlEncodePluginActions")
        self._actions.add_actions(actions)

        manager = self.window.get_ui_manager()
        manager.insert_action_group(self._actions)

        self._ui_merge_id = manager.add_ui_from_string(ui_str)
        manager.ensure_update()

    def do_deactivate(self):
        manager = self.window.get_ui_manager()
        manager.remove_ui(self._ui_merge_id)
        manager.remove_action_group(self._actions)
        manager.ensure_update()

    def do_update_state(self):
        view = self.window.get_active_view()
        self._actions.set_sensitive(bool(view and view.get_editable()))
        
    def UrlEncode(self, action):
        """Get selected text, url-encode it, and replace it instead of selection."""
        doc = self.window.get_active_document()
        bounds = doc.get_selection_bounds()
        if not bounds: return
        text = doc.get_text(bounds[0], bounds[1], False)
        text = urllib.quote_plus(text)
        doc.begin_user_action()
        doc.delete(*bounds)
        doc.insert_at_cursor(text)
        doc.end_user_action()
        
    def UrlDecode(self, action):
        """Get selected text, url-decode it, and replace it instead of selection."""
        doc = self.window.get_active_document()
        bounds = doc.get_selection_bounds()
        if not bounds: return
        text = doc.get_text(bounds[0], bounds[1], False)
        text = urllib.unquote_plus(text)
        doc.begin_user_action()
        doc.delete(*bounds)
        doc.insert_at_cursor(text)
        doc.end_user_action()
        
