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
import os
from flask import Blueprint, render_template, request
from models import Config
from forms import MyForm
from appinit import db
from urlparse import urlparse
from common.DiscoveryClient import DiscoveryClient
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

def ping(host):


    hostname = host
    response = os.system("ping -c 1 -t 1 " + hostname)

    #and then check the response...
    if response == 0:
        return True
    else:
        return False

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

@home_page.route('clusterlayout/<id>')
def get_cluster_layout(id):
    conf = Config.query.get(id)
    r = requests.get(conf.cluster_etcd_locator_url)
    cluster_info = json.loads(r.text)
    hosts = []
    try:
        for node in cluster_info['node']['nodes']:
            host = {}
            u = urlparse(node['value'])
            host['name']=u.hostname
            host['status']='down'
            print u.hostname
            print u.port
            status = ping(u.hostname)
            host['durl']=node['key'].replace('/_etcd/registry/','')
            if status:
                host['status']='up'
                #check if node is master
                client = etcd.Client(host=u.hostname,port=4001)
                try:
                    t = client.leader
                    if urlparse(t).hostname == u.hostname:
                        host['status']='master'
                except Exception:
                    pass

            hosts.append(host)
    except KeyError:
        pass
    return render_template('cluster_layout.html', hosts=hosts)








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

@home_page.route('removenode/<path:ident>')
def removenode(ident):
    client = DiscoveryClient(host="discovery.etcd.io",port=443,protocol='https')
    client.delete("/"+ident)
    return json.dumps({'status':'OK'});