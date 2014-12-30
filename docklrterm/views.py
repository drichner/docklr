__author__ = 'drichner'
"""
 docklr -- views.py
Copyright (C) 2014  Dan Richner

This program is free software; you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation; either version 2 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License along
with this program; if not, write to the Free Software Foundation, Inc.,
51 Franklin Street, Fifth Floor, Boston, MA 02110-1301 USA.
"""

from gevent import monkey
monkey.patch_all()
from appinit import app
from flask import Flask, request, abort, render_template
from werkzeug.exceptions import BadRequest
import gevent
import wssh
from flask import Blueprint, render_template, request
from docklrapp.models import Config

term_page = Blueprint('term', __name__,
                      template_folder='templates',
                      static_folder='static')

@term_page.route('/frm/<hostname>/<id>')
def termform(hostname,id):
    return render_template('term.html', hostname=hostname)

@term_page.route('/connect/<hostname>/<id>')
def connect(hostname,id):

    # Abort if this is not a websocket request
    if not request.environ.get('wsgi.websocket'):
        app.logger.error('Abort: Request is not WebSocket upgradable')
        raise BadRequest()

    bridge = wssh.WSSHBridge(request.environ['wsgi.websocket'])
    try:
        config = Config.query.get(id)
        bridge.open(
            hostname=hostname,
            username='core',
            port=22,
            private_key=config.private_key,
            allow_agent=app.config.get('WSSH_ALLOW_SSH_AGENT', False))
    except Exception as e:
        app.logger.exception('Error while connecting to {0}: {1}'.format(
            hostname, e.message))
        request.environ['wsgi.websocket'].close()
        return str()
    bridge.shell()

    # We have to manually close the websocket and return an empty response,
    # otherwise flask will complain about not returning a response and will
    # throw a 500 at our websocket client
    request.environ['wsgi.websocket'].close()
    return str()
