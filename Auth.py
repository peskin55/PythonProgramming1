#!/usr/bin/python3.8
# -*- coding: utf-8 -*-
"""
 Copyright © 2017 Bilal Elmoussaoui <bil.elmoussaoui@gmail.com>

 This file is part of Authenticator.

 Authenticator is free software: you can redistribute it and/or
 modify it under the terms of the GNU General Public License as published
 by the Free Software Foundation, either version 3 of the License, or
 (at your option) any later version.

 Authenticator is distributed in the hope that it will be useful,
 but WITHOUT ANY WARRANTY; without even the implied warranty of
 MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 GNU General Public License for more details.

 You should have received a copy of the GNU General Public License
 along with Authenticator. If not, see <http://www.gnu.org/licenses/>.
"""

import argparse
import gettext
import locale
import sys
from os import path
from gettext import gettext as _
from gi import require_version
require_version('Gtk', '3.0')
require_version('Gdk', '3.0')
require_version("Handy", "0.0")
require_version('Secret', '1')
from gi.repository import Gio, Handy

sys.path.insert(1, '/usr/lib/python3.8/site-packages')

def prepare_locale():
    locale.bindtextdomain('Authenticator', '/usr/share/locale')
    locale.textdomain('Authenticator')
    gettext.bindtextdomain('Authenticator', '/usr/share/locale')
    gettext.textdomain('Authenticator')


if __name__ == "__main__":
    prepare_locale()

    parser = argparse.ArgumentParser(prog="Authenticator")
    parser.add_argument("--debug", "-d", action="store_true",
                        help=_("Start in debug mode"))
    args = parser.parse_args()

    resource = Gio.resource_load(path.join('/usr/share/com.github.bilelmoussaoui.Authenticator', 'com.github.bilelmoussaoui.Authenticator.gresource'))
    Gio.Resource._register(resource)

    from Authenticator.models import Logger
    level = Logger.ERROR
    if args.debug:
        level = Logger.DEBUG
        import faulthandler
        faulthandler.enable()

    Logger.set_level(level)
    try:
        Handy.init(None)
        from Authenticator.application import Application
        app = Application.get_default()
        app.props.profile = 'default'
        exit_status = app.run(None)
        sys.exit(exit_status)
    except KeyboardInterrupt:
        exit()
