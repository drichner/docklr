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

from flask import Blueprint, render_template, abort
from models import Config
from jinja2 import TemplateNotFound

home_page = Blueprint('home_page', __name__,
                        template_folder='templates',
                        static_folder='static')


# helpers
def getAllConfigs():
    return Config.query.all()

# remderers

@home_page.route('/')
def index():

    return render_template('index.html', configs=getAllConfigs())
