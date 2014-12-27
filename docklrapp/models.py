__author__ = 'drichner'
"""
 docklr -- models.py
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
from appinit import db
import json


class Config(db.Model):

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)

    cluster_name = db.Column(db.String(128))

    cluster_etcd_locator_url = db.Column(db.String(256))

    private_key = db.Column(db.Text(1100))

    @property
    def dict(self):
        return {'id':self.id,'cluster_name':self.cluster_name,'cluster_etcd_locator_url':self.cluster_etcd_locator_url}