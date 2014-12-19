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

from flask import Blueprint, render_template, request
from models import Config
from forms import MyForm
from appinit import db
import json
import etcd
import requests
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
    mform = MyForm()
    return render_template('index.html', configs=getAllConfigs(),form=mform)


@home_page.route('clusterinfo/<id>')
def get_cluster_info(id):
    conf = Config.query.get(id)
    r = requests.get(conf.cluster_etcd_locator_url)
    return r.text

@home_page.route('clusterconfig', methods=['GET', 'POST'])
def login():
    print request
    if request.method == 'POST':
        #save a new config
        nc=Config()
        nc.cluster_name = request.form['cluster_name']
        nc.cluster_etcd_locator_url = request.form['cluster_etcd_locator_url']
        db.session.add(nc)
        db.session.commit()
        return json.dumps({'status':'OK'});
    else:
        print request