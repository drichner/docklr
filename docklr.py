__author__ = 'drichner'
"""
 docklr -- docklr.py
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
from docklrapp.views import home_page
from etcdapp.views import etcd_page
from docklrterm.views import term_page
from appinit import app

# Resister the app modules

app.register_blueprint(home_page,url_prefix='/')
app.register_blueprint(etcd_page,url_prefix='/etcd')
app.register_blueprint(term_page,url_prefix='/term')
