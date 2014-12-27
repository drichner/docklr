__author__ = 'drichner'
"""
 docklr -- forms.py
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

from flask_wtf import Form
from wtforms import StringField,TextAreaField
from wtforms.validators import DataRequired

class AddConfig(Form):
    cluster_name = StringField('Config Name', validators=[DataRequired()])
    cluster_etcd_locator_url = StringField('Config URL',  validators=[DataRequired()])
    primary_key = TextAreaField('Private Key')

class NewConfig(Form):
    cluster_name = StringField('Config Name', validators=[DataRequired()])

# CRUD Test
class ConfigForm(Form):
    cluster_name = StringField('Config Name', validators=[DataRequired()])
    cluster_etcd_locator_url = StringField('Config URL',  validators=[DataRequired()])
    private_key = TextAreaField('Private Key',  validators=[DataRequired()])