__author__ = 'drichner'
"""
 docklr -- run.py
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


from docklrapp.views import simple_page
from flask import Flask
from flask_bootstrap import Bootstrap

app = Flask(__name__, instance_relative_config=True)
Bootstrap(app)
app.config.from_object('config')
#app.config.from_pyfile('config.py')
app.register_blueprint(simple_page,url_prefix='/pages')
print simple_page.root_path

if __name__ == '__main__':
    app.run()

