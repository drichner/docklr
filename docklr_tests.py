__author__ = 'drichner'
"""
 docklr -- docklr_tests.py
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
import run as docklr
import unittest
from appinit import db
from docklrapp.models import Config

class FlaskrTestCase(unittest.TestCase):


    def setUp(self):
        docklr.app.config['TESTING'] = True
        docklr.app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///docklr-test.db"
        db.create_all()
        self.app = docklr.app.test_client()


    def tearDown(self):
        os.remove('docklr-test.db')


    def test_page(self):
        rv = self.app.get('/')
        assert 'Docklr Home' in rv.data

    def test_etcd(self):
        rv = self.app.get('/etcd/')
        assert 'etcd Start' in rv.data

    def test_add_config(self):
        config = Config()
        config.cluster_name = "Test Cluster"
        config.cluster_etcd_locator_url = "https://discovery.etcd.io/50347750807ecec710d21b67e6b63c88"
        db.session.add(config)
        db.session.commit()
        assert len(Config.query.all()) == 1
        rv = self.app.get('/')
        assert 'Test Cluster' in rv.data



   


# helper methods

    def getConfigRecord(self):
        testconfig = Config.query.first()
        if not testconfig:
            config = Config()
            config.cluster_name = "Test Cluster"
            config.cluster_etcd_locator_url = "https://discovery.etcd.io/50347750807ecec710d21b67e6b63c88"
            db.session.add(config)
            db.session.commit()
            return self.getConfigRecord()
        return testconfig


if __name__ == '__main__':
    unittest.main()